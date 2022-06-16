from pathlib import Path
import os

import pynvim
import pynvim.api


@pynvim.plugin
class Main:
    def __init__(self, nvim: pynvim.api.Nvim):
        self.nvim = nvim

    @pynvim.command("CargoAtCoderOpen", sync=True)
    def open_atcoder_problem_page(self):
        current_file_path_str: str = self.nvim.command_output('echo expand("%")')  # type: ignore
        if current_file_path_str == "":
            return

        current_file_path = Path(current_file_path_str)
        current_file_name = current_file_path.stem
        self.nvim.command(f'echo "{current_file_name}"')

        working_dir = os.getcwd()
        self.nvim.command(f'echo "{working_dir}"')
        # self.nvim.command('silent !open https://atcoder.jp')
        # self.nvim.command('!open https://atcoder.jp')
