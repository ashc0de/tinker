"VIM-PLUG AREA
call plug#begin('C:\Users\Name\AppData\Local\nvim\plugged')


"-----Python Semantic Syntax highlighting-------


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

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" " Use spaces instead of tabs
set expandtab
"
" " Be smart when using tabs ;)
set smarttab
"
" " 1 tab == 4 spaces
set shiftwidth=4
set softtabstop=4
set tabstop=4
"
" " Linebreak on 500 characters
" set lbr
" set tw=500
"
"Auto indent and  "Smart indent
set autoindent
set smartindent 

"keyremaps
:nnoremap <F9> :set number! relativenumber! <CR>
