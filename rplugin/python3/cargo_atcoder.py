import os

import pynvim


@pynvim.plugin
class Main:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("CargoAtCoderOpen", sync=True)
    def open_atcoder_problem_page(self):
        print(type(self.nvim))
        # self.nvim.command('silent !open https://atcoder.jp')
        self.nvim.command('!open https://atcoder.jp')
