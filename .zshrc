#no problem with file's sizes
ulimit -c 0
#les couleurs pour le prompt
autoload -U colors
colors
#pour je sais pas encore quoi check it out
autoload -U compinit
compinit
#conf du prompt
# for libcurl
##     LDFLAGS:  -L/usr/local/opt/curl/lib
##    CPPFLAGS: -I/usr/local/opt/curl/include

RPS1="%{$fg_bold[yellow]%}%? %{$fg_bold[red]%}--%{$fg_bold[magenta]%}%T%{$fg_bold[red]%}--%{$reset_color%}"
PS1="%{$fg_bold[red]%}-%{$fg_bold[magenta]%}%n%{$fg_no_bold[blue]%}@%{$fg_bold[green]%}%M %{$fg_bold[cyan]%}%~%{$reset_color%} "
#fin de conf du prompt
#
alias codeList="/Volumes/2To WDC HFS+ case sensitive journalised/code/OLD"
alias vlc="/Applications/VLC.app/Contents/MacOS/VLC"
alias listusers="dscl . -list /Users"
alias clang="/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang"
alias 1="cd Code/formprotaxi"

export NODE_PATH="/usr/local/lib/node"
export PIP_USE_MIRRORS=true
#export LANG="it_IT.UTF-8"
#export LC_COLLATE="it_IT.UTF-8"
#export LC_CTYPE="it_IT.UTF-8"
#export LC_MESSAGES="it_IT.UTF-8"
#export LC_MONETARY="it_IT.UTF-8"
#export LC_NUMERIC="it_IT.UTF-8"
#export LC_TIME="it_IT.UTF-8"
export LC_ALL="fr_FR.UTF-8"

export GNUTERM="x11"
GNUTERM="x11"
export DATABASE_URL=postgres://guilbep@localhost/website
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh


export PAGER="less"
export EDITOR="emacs"
#export CFLAGS="-W -Wall -Werror -ansi -pedantic"
#export CFLAGS=""
export SHELL="/bin/zsh"
#
HISTSIZE=100000
SAVEHIST=1000
HISTFILE=~/.zshhist

#export PYTHON=/usr/local/bin/python

PATH=/usr/bin:$PATH
PATH=/bin:$PATH
PATH=/usr/sbin:$PATH
PATH=/sbin:$PATH
PATH=/usr/local/sbin:$PATH
PATH=/Users/guilbep/bin:$PATH
PATH=/usr/local/bin:$PATH
PATH=/Library/Frameworks/Maple.framework/Versions/Current/bin:$PATH
PATH=/Users/guilbep/Code/leadangelie3:$PATH
#PATH=/usr/local/Cellar/node/0.8.15/lib/node_modules/npm/bin:$PATH

export PYTHONPATH=/Library/Python/2.7/site-packages:$PYTHONPATH


MANPATH=/opt/local/share/man:\
/usr/local/mysql/man:\
/usr/local/pgsql/share/man/:\
/usr/local/apache2/man:\
/Library/Frameworks/Python.framework/Versions/2.7/share/man:\
$MANPATH
#alias list
#alias startdb="pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start"
alias stopdb="pg_ctl -D /usr/local/var/postgres stop -s -m fast"
alias startdb="pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log  start"
alias ss="script/server"
alias edit="emacs ~/.zshrc"
#alias tracks='cd ~/Applications/tracks-1.7 && ~/Applications/tracks-1.7/script/server -p 4321'
#alias twitt="twitter_update.pl"
#alias 1="cd ~/Desktop/website/"
alias reload="source ~/.zshrc"
alias activation="source venv/bin/activate"
alias ls='ls -G'
alias ll='ls -Glh'
alias la='ls -Gah'
alias lla='ls -Glah'
#alias news='emacs -nw -f gnus'
alias e='emacs -nw'
#alias bb='ssh guilbe_p@bernie.epita.fr'
#alias bernie='ssh guilbe_p@ssh.epita.fr'

# Lines configured by zsh-newuser-install
#setopt autocd
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
#zstyle :compinstall filename '/home/pierre/.zshrc'

#autoload -Uz compinit
#compinit
# End of lines added by compinstall
#envie de faire du tetris
#autoload -U tetris
#zle -N tetris
#bindkey KEYS tetris

#pour le son
#if [[ -n $DISPLAY ]] then
#    xset b off
#    xset r rate 200 80
#fi/usr/local/git/bin
