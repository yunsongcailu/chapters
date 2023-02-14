### 安装git
```text
    windows: https://www.git-scm.com/download/win
    centos:  yum install -y git  ( sudo yum install -y git )
    ubuntu: sudo apt-get install git
    macOS: brew install git
```
### git配置
```zsh
    git config --list                                   # 显示当前的Git配置
    git config -e [--global]                            # 显示Git配置文件
    git config [--global] user.name "[name]"            # 设置提交代码时的用户名
    git config [--global] user.email "[email address]"  # 设置提交代码时的用户邮箱
    
    git config --global user.name "yunsongcailu"
    git config --global user.email "yunsongcialu2020@gmail.com"
```
### 本地同步git
```zsh
    # 当前目录下执行
    git init
    # 查看状态
    git status
    # 添加单个文件
    git add filename
    # 添加所有
    git add .
```
### 提交仓库
```zsh
    # 带文字说明提交 -m
    git commit -m '第一次提交,创建chapter'
```
### 代码回滚到:上一次commit版本
```zsh
    git reset --hard HEAD^
```
### 代码重置到指定 HEAD 
```zsh
    # 查看所有commit 上传记录点 获取 commit id  7a99148c897ddcf9186745617334290cee6eec76
    git log
    # 代码重置到指定head
    git reset --hard 7a99148
    # 取消缓存区的某个文件(已提交的) 回到未提交状态(从缓存区返回工作区)
    get reset HEAD filename
```
### 远程仓库
```zsh
    # github 为例
    # github 创建仓库
    # 本地项目根目录下执行
    git clone https://github.com/yunsongcailu/chapters.git
    # 进入项目目录 设置个人信息
    git config user.name "yunsongcailu"
    git config user.email "yunsongcailu2020@gmail.com"
    git status
```