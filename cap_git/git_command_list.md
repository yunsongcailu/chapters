## git常用命令列表
```text
#git新建代码
git init                         # 在当前目录新建一个Git代码库
git init [project-name]          # 在当前目录新建一个目录，将其初始化为Git代码库
git clone [url]                  # 下载一个项目和它的整个代码历史
　　
#git配置
git config --list                                   # 显示当前的Git配置
git config -e [--global]                            # 显示Git配置文件
git config [--global] [user.name](http://user.name) "[name]"            # 设置提交代码时的用户名
git config [--global] user.email "[email address]"  # 设置提交代码时的用户邮箱
　　
#git操作文件的增删改
git add [file1] [file2] ...               # 添加指定文件到暂存区
git add [dir]                             # 添加指定目录到暂存区，包括子目录
git add .                                 # 添加当前目录的所有文件到暂存区
git add -p                                # 添加每个变化前，都会要求确认，对于同一个文件的多处变化，可以实现分次提交
git rm [file1] [file2] ...                # 删除工作区文件，并且将这次删除放入暂存区
git rm --cached [file]                    # 停止追踪指定文件，但该文件会保留在工作区
git mv [file-originname] [file-newname]   # 改名文件，并且将这个改名放入暂存区
　　
#git 代码提交操作
git commit -m [message]                       # 提交暂存区到本地仓库
git commit [file1] [file2] ... -m [message]   # 提交暂存区指定文件到本地仓库
git commit -a                                 # 提交工作区自上次commit之后的变化，直接到本地仓库
git commit -v                                 # 提交时显示所有diff信息
git commit --amend -m [message]               # 使用一次新的commit，替代上一次提交，如果代码没有任何变化，则用来改写上一次commit的提交信息
git commit --amend [file1] [file2] ...        # 重做上一次commit，并包括指定文件的新变化
　　
#git远端操作
git fetch [remote]                    # 下载远程仓库的所有变动，注意这个时候是不会修改本地文件的
git pull [remote] [branch]            # 拉取远程仓库的变化，并与本地分支合并
git remote -v                         # 显示所有远程仓库
git remote show [remote]              # 显示某个远程仓库的信息
git remote add [shortname] [url]      # 增加一个新的远程仓库，并命名
git push [remote] [branch]            # 上传本地指定分支到远程仓库
git push [remote] --force             # 强行推送当前分支到远程仓库，即使有冲突
git push [remote] --all               # 推送所有分支到远程仓库
git push <remote> :<branch/tag-name>  # 删除远程分支或标签
git push --tags                       # 上传所有标签
　　
#git，push后的回退操作 谨慎使用
git reset --hrad HEAD         # 撤销工作目录中所有未提交文件的修改内容
git checkout HEAD <file>      # 撤销指定的未提交文件的修改内容
git revert <commit>           # 撤销指定的提交
git log --before="1 days"     # 退回到之前1天的版本
git checkout [file]           # 恢复暂存区的指定文件到工作区
git checkout [commit] [file]  # 恢复某个commit的指定文件到暂存区和工作区
git checkout .                # 恢复暂存区的所有文件到工作区
git reset [file]              # 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
git reset --hard              # 重置暂存区与工作区，与上一次commit保持一致
git reset [commit]            # 重置当前分支的指针未指定commit，同时重置暂存区，但工作区不变
git reset --hard [commit]     # 重置当前分支的HEAD未指定commit，同时重置暂存区和工作区，与指定commit一致
git reset --keep [commit]     # 重置当前HEAD未指定commit，但保持暂存区和工作区不变
　　
#git中查看操作信息
git status                                 # 查看当前工作区状态(与暂存区对比，增加删除或修改)
git log                                    # 显示当前分支的版本历史
git log --stat                             # 显示commit历史，以及每次commit发生变更的文件
git log -S [keyword]                       # 根据关键字搜索提交历史
git log [tag] HEAD --pretty=format:%s      # 显示某个commit之后的变动，每个commit占据一行。我记得--pretty=online也行
git log -p [file]                          # 显示指定文件相关的每一个diff
git log -5 --pretty --oneline              # 显示过去5次提交
git shortlog -sn                           # 显示所有提交过的用户，按提交次数排序
git blame [file]                           # 显示指定文件是什么人在什么时间修改过，这个blame很生动形象
git diff                                   # 显示暂存区和工作区的差异
git diff --cached [file]                   # 显示暂存区和上一个commit的差异
git diff HEAD                              # 显示工作区与当前分支最新commit之间的差异
git diff [first-branch]...[second-branch]  # 显示两次提交之间的差异
git diff --shortstat "@{0 day agp}"        # 显示今天你写了多少航代码
git show [commit]                          # 显示某次提交的元数据和内容变化
git show --name-only [commit]              # 显示某次提交发生变化的文件
git show [commit]:[filename]               # 显示某次提交时，某个文件的内容
git reflog                                 # 显示当前分支的最近几次提交
　　
#git中tag操作
git tag  # 列出所有本地标签
git tag <tagname>                     # 基于最新提交创建标签
git tag -d <tagname>                  # 删除标签
git push origin :refs/tags/[tagName]  # 删除远程tag
git show [tag]                        # 查看tag信息
git push [remote] [tag]               # 提交指定tag
git push [remote] --tags              # 提交所有tag
git checkout -b [branch] [tag]        # 新建一个分支，指向某个tag
　　

#git分支操作
git branch                                            # 显示所有本地分支
git branch -r                                         # 列出所有远程分支
git branch -a                                         # 列出所有本地分支和远程分支
git branch [branch-name]                              # 新建一个分支，但head依然停留在当前分支
git branch --track [branch] [remote-branch]           # 新建一个分支，与指定的远程分支建立追踪关系
git branch -d [branch-name]                           # 删除指定分支
git checkout -b [branch-name]                         # 新建一个分支，并切换head到该分支
git checkout [branch-name]                            # 切换head到指定分支，并更新工作区
git checkout -                                        # 切换到上一个分支
git branch --set-upstream [branch] [remote-branch]    # 建立追踪关系，在现有分支与指定的远程分支之间
git merge [branch]                                    # 合并指定分支到当前分支
git rebase <branch>                                   # 衍合指定分支到当前分支
git cherry-pick [commit]                              # 选择一个commit，合并进当前分支
```