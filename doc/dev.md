# 개발환경

## Ubuntu 18.04 LTS

### package update
```
# apt-get update && apt-get dist-upgrade
# apt-get autoclean
# apt-get autoremove
```

### locale
```
# locale-gen --purge en_US.UTF-8 ko_KR.UTF-8 th_TH.UTF-8
# update-locale LANG=en_US.UTF-8
# apt-get install gettext
```

### timezone
```
# timedatectl set-timezone Asia/Bangkok
# timedatectl set-ntp 1
```

### hostname
```
# hostnamectl set-hostname online-judge
# reboot
```

### users and groups
```
# groupadd devops
# useradd -g devops -G sudo,devops -b /home -m -s /bin/bash dev
# passwd dev
# useradd -g devops -b /home -m -s /bin/bash was
# dpkg-statoverride --update --add root sudo 4750 /bin/su
# dpkg-statoverride --update --add root sudo 4750 /usr/bin/sudo
# passwd -d -l root
# usermod -s /bin/false root
```

### vim
```
$ sudo update-alternatives --config editor
```

```
$ cat > ~/.vimrc
set nocompatible
set ruler
set wrap
set number

set tabstop=8
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class
set nocindent

set nobackup
set visualbell
set hlsearch
set background=dark
set termencoding=utf-8
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,euc-kr,latin1

filetype indent plugin on
```

### ssh
`/etc/ssh/sshd_config`

```
Port 22111
AddressFamily inet
PermitRootLogin no
StrictModes yes
AllowGroups devops
```

```
$ sudo service ssh restart
```

## Build Tools

```
$ sudo apt-get install build-essential python3 python3-dev openjdk-11-jdk php-cli
```

### PyEnv

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
$ pyenv install --list
```

Build Python

```
$ sudo apt-get install zlib1g-dev libffi-dev libbz2-dev libreadline-dev libssl-dev libsqlite3-dev
$ pyenv install 3.7.4
```

VirtualEnv

```
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.profile
```

### Github

```
$ ssh-keygen -t rsa -b 4096 -C "test@example.com"
$ eval `ssh-agent -s`
$ git clone git@github.com:pincoin/pincoin-online-judge.git poj
```

## Security
### UFW

### SECCOMP
```
$ sudo apt-get install libseccomp-dev
```

### Chroot

## Django

### Django

```
pip install django
```

### Redis

### Memcached

### RabbitMQ

### Maria DB

### NGINX

### Gunicorn

