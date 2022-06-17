# cargo-atcoder.nvim

### Install

```vim
call plug#begin('~/.config/nvim/plugged')
  Plug 'himkt/cargo-atcoder.nvim'
call plug#end()
```

### Usage

- `:CargoAtcoderOpen` to open the problem page
- `:CargoAtcoderRun` to run the code (actually it is not `cargo-atcoder` feature)
- `:CargoAtcoderStatus` to view the stats
- `:CargoAtcoderSubmit` to make a submission
- `:CargoAtcoderSubmitForce` to make a submission even if the program is wrong on samples
- `:CargoAtcoderTest` to run the code on samples

### Developing

`vim-plug` can register the local plugin.

```vim
call plug#begin('~/.config/nvim/plugged')
  Plug 'file:///Users/himkt/work/github.com/himkt/cargo-atcoder.nvim'
call plug#end()
```

Don't forget to run `git commit`, `vim-plug` recognizes only committed files.
After installing the package by `:PlugInstall`, run `:UpdateRemotePlugins` as well.
