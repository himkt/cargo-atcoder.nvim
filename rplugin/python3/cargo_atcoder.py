import os

import pynvim


@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command("Open", sync=True)
    def open(self):
        self.vim.command('echo "hello from DoItPython"')
        nvim = pynvim.attach('socket', os.environ['NVIM_LISTEN_ADDRESS'])
        print(nvim.current.buffer)
