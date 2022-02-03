"VIM-PLUG AREA
call plug#begin('C:\Users\AK-Win\AppData\Local\nvim\plugged')


"-----Python Semantic Syntax highlighting-------

Plug 'numirias/semshi', {'do' : ':UpdateRemotePlugins'}

"------Themes section------
Plug 'dracula/vim' , {'as' : 'dracula'}

Plug 'mhartington/oceanic-next'

Plug 'EdenEast/nightfox.nvim'

Plug 'morhetz/gruvbox'

call plug#end()


"My NVIM load time preferences
:set cursorline
:set scrolloff=10
:set number relativenumber
:set termguicolors
:colorscheme gruvbox
:syntax enable
:set ignorecase
:set nohlsearch
:set clipboard=unnamedplus

"keyremaps
:nnoremap <F9> :set number! relativenumber! <CR>
