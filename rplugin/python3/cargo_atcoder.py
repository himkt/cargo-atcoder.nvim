import os

import pynvim


@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command("CargoAtCoderOpen", sync=True)
    def open_atcoder_problem_page(self):
        self.vim.command('echo "hello from DoItPython"')
        print("hello")
        # nvim = pynvim.attach('socket', os.environ['NVIM_LISTEN_ADDRESS'])
        # print(nvim.current.buffer)
