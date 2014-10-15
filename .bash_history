git config --global user.name Johan Brådvik
git config --global user.email johan@bradvik.se
git config --global color.ui.auto
git config --global user.name "Johan Brådvik"
git config -l
nano git-core-editor.sh
git config --global core.editor /usr/local/bin/git-core-editor.sh
git mergetool
git config --global alias co.checkout
git config --global alias.co checkout
git config --global alias.bra "branch -a"
$ git config --global alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit"
git config --global alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit"
git config --global alias.lola "log --graph --decorate --pretty=oneline --abbrev-commit --all"
 git init
git remote add origin https://github.com/SirPurple/Test.git
git push -u origin master
touch README.md
git add README.md
git commit -m "This is my first commit"
git remote add origin https://github.com/SirPurple/Test.git
git push -u origin master
git log -p
git log --oneline --graph
git branch -a
ls -al ~/.ssh
ssh-keygen -t rsa -C "johan@bradvik.se"
ssh-agent -s
ssh-add ~/.ssh/id_rsa
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
clip < ~/.ssh/id_rsa.pub
ssh -T git@github.com
history