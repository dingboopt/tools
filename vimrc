set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'majutsushi/tagbar'
Plugin 'scrooloose/nerdtree'
Plugin 'fholgado/minibufexpl.vim'
Plugin 'Valloric/YouCompleteMe'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

set bs=2
syntax on
set tags=tags

"-- Cscope setting --

if has("cscope")
  set csprg=/usr/bin/cscope 
  set csto=0 
  set cst 
  set cscopequickfix=s-,c-,d-,i-,t-,e- " 使用QuickFix窗口来显示cscope查找结果
  set nocsverb
  if filereadable("cscope.out") 
    cs add cscope.out
  elseif $CSCOPE_DB != "" 
    cs add $CSCOPE_DB
   endif
  set csverb
endif

map <F4> :cs add ./cscope.out .<CR><CR><CR> :cs reset<CR>

imap <F4> <ESC>:cs add ./cscope.out .<CR><CR><CR> :cs reset<CR>

nmap <F5> :cs find s <C-R>=expand("<cword>")<CR><CR>
nmap <F6> :cs find t <C-R>=expand("<cword>")<CR><CR>
nmap <F7> :cs find c <C-R>=expand("<cword>")<CR><CR>


"安装tagbar插件  
""设置tagbar使用的ctags的插件,必须要设置对  
let g:tagbar_ctags_bin='/usr/bin/ctags'  
"设置tagbar的窗口宽度  
let g:tagbar_width=30  
""设置tagbar的窗口显示的位置,为左边  
let g:tagbar_right=1  
"打开文件自动 打开tagbar  
autocmd BufReadPost *.cpp,*.c,*.h,*.hpp,*.cc,*.cxx call tagbar#autoopen()  
""映射tagbar的快捷键  
map <F8> :TagbarToggle<CR>  


autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

let NERDTreeWinSize=15
let NERDTreeShowLineNumbers=1
let NERDTreeAutoCenter=1


let g:miniBufExplMapWindowNavVim = 1   
let g:miniBufExplMapWindowNavArrows = 1   
let g:miniBufExplMapCTabSwitchBufs = 1   
let g:miniBufExplModSelTarget = 1  
let g:miniBufExplMoreThanOne=0

map <F11> :MBEbp<CR>
map <F12> :MBEbn<CR>

set mouse=a
