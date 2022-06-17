from pathlib import Path
from typing import Any, List, Optional, Tuple
import urllib.error
import urllib.request
import html.parser
import os

import pynvim
import pynvim.api


class AtCoderTaskPageParser(html.parser.HTMLParser):

    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.state = False
        self.target = True
        self.href: Optional[str] = None
        self.links = {}

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        if tag == "td":
            ret = sum(
                1 for k, v in attrs
                if k == "class" and isinstance(v, str) and "text-center" in v
            ) > 0

            if ret:
                self.state = True

        if tag == "a":
            self.target = True

        if self.state and self.target:
            for k, v in attrs:
                if k != "href":
                    continue
                self.href = v

    def handle_data(self, data: Any):
        if self.state and self.target and isinstance(self.href, str):
            self.links[data] = self.href[1:]

    def handle_endtag(self, tag: str):
        if tag == "td":
            self.state = False

        if tag == "a":
            self.target = False


@pynvim.plugin
class Main:
    def __init__(self, nvim: pynvim.api.Nvim):
        self.nvim = nvim
        self.base_url = "https://atcoder.jp"
        self.parser = AtCoderTaskPageParser()

    def get_current_file(self) -> Optional[str]:
        current_path_to_file: str = self.nvim.command_output("echo expand('%')")  # type: ignore
        if current_path_to_file == "":
            return None
        return Path(current_path_to_file).stem

    def get_working_dir(self) -> str:
        return Path(os.getcwd()).name

    @pynvim.command("CargoAtCoderOpen", sync=True)
    def open_atcoder_problem_page(self) -> None:
        working_dir_name = self.get_working_dir()
        problem_name = self.get_current_file()
        if problem_name is None:
            return

        task_url = f"{self.base_url}/contests/{working_dir_name}/tasks"
        request = urllib.request.Request(task_url)

        # NOTE Assume 200
        try:
            with urllib.request.urlopen(request) as response:
                body = response.read().decode("utf-8")
                self.parser.feed(body)
                href = self.parser.links[problem_name.upper()]
                problem_url = f"{self.base_url}/{href}"

        # NOTE Fallback (typically enters when 404.
        except urllib.error.HTTPError:
            problem_url = (
                f"{self.base_url}/contests"
                f"/{working_dir_name}/tasks"
                f"/{working_dir_name}_{problem_name}"
            )

        self.nvim.command(f"silent !open {problem_url}")

    @pynvim.command("CargoAtcoderStatus", sync=True)
    def open_atcoder_status_page(self) -> None:
        self.nvim.command("split | term cargo atcoder status")

    @pynvim.command("CargoAtcoderTest", sync=True)
    def test_atcoder_problem(self) -> None:
        problem_name = self.get_current_file()
        self.nvim.command(f"split | term cargo atcoder test {problem_name}")

    @pynvim.command("CargoAtcoderSubmit", sync=True)
    def submit_atcoder_problem(self) -> None:
        problem_name = self.get_current_file()
        self.nvim.command(f"split | term cargo atcoder submit {problem_name}")

    @pynvim.command("CargoAtcoderSubmitForce", sync=True)
    def force_submit_atcoder_problem(self) -> None:
        problem_name = self.get_current_file()
        self.nvim.command(f"split | term cargo atcoder submit --force {problem_name}")

    @pynvim.command("CargoAtcoderRun", sync=True)
    def run_atcoder_problem(self) -> None:
        problem_name = self.get_current_file()
        self.nvim.command(f"split | term cargo run --bin {problem_name}")
