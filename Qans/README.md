# Questions related



## Related to the git and github
1. a branch is created on the remote repository and i want to pull this brach to my local repository.
ans : We can see branches present on the remote repo using ``git branch -r `` to update this info in your local repo
use `` git fetch origin `` then pull the remote branches into the local machine using
command 1 : ``git checkout -b <branch_name>`` <br>
command 2 : `` git swithc -c <branch_name> `` <br>
you can see and verify the process using `` git branch ``

2. how to merge local branches into one another ? 
3. Need to remove commits and from the git history , commits are not pushed.
Ans : condition 1 : if files are added using ``git add . ``, but not did `` git commit -m " msg" ``if you want to unstagged changes from the the stage and you didn't commit the changes.
command to unstagge everything : `` git restore --staged . ``
if you want to unstage a single file than do : `` git restore --staged <file_name.ex> ``

you also have an old command to do the above thing : `` git reset HEAD <file_name.ex> ``
<br>
condition 2 : files are commited but not pushed.
case : we need to remove files from the last commit, keep file locally but remove from commit
command is : `` git reset --soft HEAD~1 `` by this files are removed from the commits and moved to the stage like `` git add . ``
<br> Now you can use conditon 1  commands

 

