" truncated version of jake's vimrc for ishai
"
" NeoVim Python3 support requires installing 'pynvim' on your system Python3
" interpreter. If you have problems, try doing that.
"
" ~$ pip3 install pynvim

" Global config
let main_colorscheme = 'ayu'
let white_colorscheme = 'PaperColor'

if has('nvim')
    call plug#begin('~/.vim/plugged')
        " ~: the holy plugins :~
        Plug 'tpope/vim-commentary'
        Plug 'tpope/vim-fugitive'
        Plug 'tpope/vim-repeat'
        Plug 'tpope/vim-surround'
        " ~:  all hail tpope  :~

            Plug 'vim-scripts/indentpython.vim'

            " HTML/CSS/Jinja
            Plug 'glench/vim-jinja2-syntax'
            Plug 'mattn/emmet-vim'
            let g:user_emmet_settings = {
            \    'html' : {
            \        'indent_blockelement': 1,
            \    },
            \}
            " Use ,, to autocomplete HTML
            " Emmet uses CSS-style selectors for autocompletion. E.g...
            "   .profile-bio
            "   .person#jake
            "   img.avatar
            "   .avatar>img#profile-pic
            " You can also use multiplication
            " .container>p*5 <- Creates a div with class container containing
            " five paragraphs.
            " .item-$*10 <- Creates 10 divs with sequentially numbered classes

            " Markdown
            Plug 'plasticboy/vim-markdown'

        " Everybody loves fuzzy finding!
            Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
            Plug 'junegunn/fzf.vim'
            let g:fzf_layout = {'down': '~40%'}

        " Sentence plugins
            " Use indentation level as noun (i)
            Plug 'michaeljsmith/vim-indent-object'

        " Quality of life plugins
            Plug 'ntpeters/vim-better-whitespace'
            Plug 'AndrewRadev/splitjoin.vim'

        " Visual Plugins
            " Uniquely colored parens/brackets
            Plug 'luochen1990/rainbow'

            " Themes
            Plug 'NLKNguyen/papercolor-theme'
            Plug 'altercation/vim-colors-solarized'
            Plug 'Rigellute/rigel'
            Plug 'ayu-theme/ayu-vim'
            Plug 'colepeters/spacemacs-theme.vim'
            Plug 'dracula/vim'
            Plug 'gruvbox-community/gruvbox'
            Plug 'phanviet/vim-monokai-pro'
            Plug 'sainnhe/gruvbox-material'

            let g:solarized_termcolors=256
    call plug#end()
endif

syntax on
runtime macros/matchit.vim

command! Config e ~/.vimrc
command! Reload source ~/.vimrc
command! White set background=light | execute 'color ' . white_colorscheme
command! Light set background=light | execute 'color ' . main_colorscheme
command! Dark set background=dark | execute 'color ' . main_colorscheme
command! Run :call RunPython()
command! RunI :call RunPython(1)
command! RunT :call RunPython(2)
command! REPL :call PythonREPL()

let g:rainbow_active = 1
let mapleader = " "
let python_highlight_all=1

nmap <C-n> :noh<CR>
nmap Y y$
nmap <leader>q :bw<CR>:intro<CR>
nmap <leader>w <C-w>
nmap <leader>s :Lines<CR>
" Quick file open
nmap <C-p> :call FuzzyOpenFile()<cr>
" Quick execution of python buffers
" Go to next/previous results
nmap <leader>n :cnext<CR>
nmap <leader>p :cprev<CR>
nmap <leader>l :clast<CR>
nmap <leader>f :cfirst<CR>
" Quick comment toggles (Ctrl-/)
nmap <C-_> gcc
vmap <C-_> gc
nmap <leader>h :noh<CR>
" Python helpers
nmap <leader>pr :Run<CR>
nmap <leader>pi :RunI<CR>
nmap <leader>pt :RunT<CR>
nmap <leader>py :REPL<CR>


function! FuzzyOpenFile()
    if has('nvim')
        silent! !git rev-parse --is-inside-work-tree
        if v:shell_error == 0
            :GFiles --cached --others --exclude-standard
        else
            :Files
        endif
    else
        :ex .
    endif
endfunction

" Create a function to open a neovim terminal in a small split window and run Python
function! RunPython(...)
if has('nvim')
    let run_mode = get(a:, 1, 0)
        echo run_mode
        if run_mode == 0
            exec winheight(0)/2."split" | terminal python3 %
        elseif run_mode == 1
                exec winheight(0)/2."split" | terminal python3 -i %
        elseif run_mode == 2
                exec winheight(0)/2."split" | terminal pytest %
        endif
        startinsert
    else
        echo "This command only works in NeoVim."
    endif
endfunction


function! PythonREPL()
    if has('nvim')
        exec winheight(0)/4."split" | terminal python3
        startinsert
    endif
endfunction

" Filetype specific settings
filetype on

" Sane splitting behaviour
set splitbelow
set splitright

set colorcolumn=80
set ttimeoutlen=50
set backspace=indent,eol,start
set tabstop=4 softtabstop=0 expandtab shiftwidth=4 smarttab
set autoindent
set number relativenumber
set scrolloff=10 sidescrolloff=5
set ignorecase smartcase
set ruler hlsearch
set showmatch
set encoding=utf8
set nowrap
set foldmethod=indent foldlevel=99

" Stop automatic unindentation of Python comments
set nosmartindent

" ERADICATE CARRIAGE RETURNS
set fileformat=unix
set fileformats=unix,dos

" Spelling
set spelllang=en

" Lower CursorHold time
set updatetime=300

" Filetype specific settings
" - Text-based files
au Filetype test,gitcommit,markdown,rst setlocal textwidth=80 wrap linebreak nolist spell
" - XML-based
au Filetype {h,xh,x}ml setlocal colorcolumn=120 textwidth=120
" - Python
au Filetype python setlocal colorcolumn=90

if has('nvim')
    set inccommand=nosplit

    " Colorscheme configuration
    set termguicolors
    let g:gruvbox_contrast_light='medium'
    let g:gruvbox_contrast_dark='hard'
    Dark

    " Enable coc.nvim bindings
    " source ~/.vim/coc-bindings.vim

    " Default Python locations
    if has('macunix')
        let g:python_host_prog='/usr/local/bin/python'
        let g:python3_host_prog='/usr/local/bin/python3'
    elseif has('win32')
        let g:python_host_prog='py'
        let g:python3_host_prog='py'
    elseif has('unix')
        let g:python_host_prog='/usr/bin/python'
        let g:python3_host_prog='/usr/bin/python3'
    endif

    if exists('g:started_by_firenvim')
        Dark
        set wrap linebreak nolist
    else
        " Airline Powerline symbols
        if $GLYPHS == "off"
            let g:airline_symbols_ascii = 1
            let g:airline_powerline_fonts = 0
        else
            let g:airline_powerline_fonts = 1
            let g:airline_left_sep = ''
            let g:airline_right_sep = ''
        endif

        " Auto-set dark/light modes
        if !empty($COLORSCHEME)
            if $COLORSCHEME == 'dark'
                Dark
            elseif $COLORSCHEME == 'light'
                White
            endif
        endif
    endif
" Old-Vim configuration
else
    " Install srcery
    if !filereadable('~/.vim/colors/srcery.vim')
        call system('curl https://raw.githubusercontent.com/srcery-colors/srcery-vim/master/colors/srcery.vim --create-dirs -o ~/.vim/colors/srcery.vim')
    endif
    color srcery

    " Increase search result contrast
    hi Search ctermfg=black ctermbg=254
    " Increase spelling error contrast
    hi SpellBad ctermfg=white ctermbg=darkred
    " Recolor the 80-character colomn
    highlight ColorColumn ctermbg=235
endif

