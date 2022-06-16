# cargo-atcoder.nvim


### Developing

`vim-plug` can register the local plugin.

```vim
call plug#begin('~/.config/nvim/plugged')
  Plug 'file:///Users/himkt/work/github.com/himkt/cargo-atcoder.nvim'
call plug#end()
```

Don't forget to run `git commit`, `vim-plug` recognizes only committed files.
After installing the package by `:PlugInstall`, run `:UpdateRemotePlugins` as well.
