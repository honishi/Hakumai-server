# Basic Setup

## Command

```shell
sudo yum update
sudo yum -y install tmux git
```

## Timezone

```shell
date
sudo cp /etc/localtime /etc/localtime.org
sudo ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
date
```
```shell
sudo cp /etc/sysconfig/clock /etc/sysconfig/clock.org
sudo vi /etc/sysconfig/clock
ZONE="Asia/Tokyo"
```

* `UTC=true` は [そのままにするもの](https://qiita.com/azusanakano/items/b39bd22504313884a7c3#comment-2cf06c33fb1247bef0e9) らしい。

# .bashrc 追加

## @remote

```shell
cd
mkdir -p dev/honishi
```

## @local

```shell
cd ~/dev/honishi/Hakumai-server/deploy
./deploy_all.sh
```

## @remote

```shell
vi ~/.bashrc
. ~/dev/honishi/Hakumai-server/shell/.bashrc
```

# Common yum install

```shell
sudo yum -y install \
  bzip2 \
  bzip2-devel \
  gcc \
  git \
  libffi-devel \
  make \
  openssl \
  openssl-devel \
  readline \
  readline-devel \
  sqlite \
  sqlite-devel \
  zlib-devel
```

# Ruby / rbenv

```shell
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
relogin
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-doctor | bash
```
```shell
rbenv versions
rbenv install 3.0.1
echo 3.0.1 > .ruby-version
rbenv versions
```

## Update rbenv

```shell
cd ~/.rbenv && git pull
cd ~/.rbenv/plugins/ruby-build && git pull
```

# Python / pyenv

```shell
# no sudo required
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

## Update pyenv

```shell
cd $(pyenv root) && git pull
```

# Configure Security

```shell
sudo visudo

# ↓ コメントアウトして `sudo -E xxx` で PATH が sudo 先に渡るようにする
# Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin
```

# Configure Project

```shell
cd ~/dev/honishi/Hakumai-server/server/
pyenv versions
pyenv install
pyenv versions
pip install -r requirements.txt
./start_server_prod.sh 
```

# tmuxinator

```shell
ln -s ~/dev/honishi/Hakumai-server/tmux/.tmux.conf ~/.tmux.conf
```
```shell
gem install tmuxinator
mkdir -p .config/tmuxinator/
ln -s ~/dev/honishi/Hakumai-server/tmuxinator/hakumai.yml ~/.config/tmuxinator/hakumai.yml
ls -l ~/.config/tmuxinator/
tmuxinator start hakumai
tmux a
```

# Appendix

## pyenv install 時の output メモ

```
# Add pyenv executable to PATH by adding
# the following to ~/.profile:

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# Load pyenv automatically by appending
# the following to ~/.bashrc:

eval "$(pyenv init -)"

# and the following to ~/.profile:

eval "$(pyenv init --path)"

# If your ~/.profile sources ~/.bashrc,
# the lines should be inserted before the part
# that does that.

# Make sure to restart your entire logon session
# for changes to ~/.profile to take effect.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"
```