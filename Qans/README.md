# Questions ⁉️ 
" In this field i talked about problems that i encounterd during development "
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

4. i need someone to review my commits and PR , i need a agent or bot ?
ans : Coderabbit ai.

5. I raised a PR and coderabbit.ai has found Some gramatical mistakes thus
how can i now change the code present in the pr,
should i do from codebase, command line or code editor from where changes are made.
ans : go to code review option , searched for edit file , changes and commit file, raise 
<<<<<<< Updated upstream
PR raised, merged , existing PR get updated then Merged successfully.
=======
PR raised, merged , existing PR get updated then Merged sucessfully.

6. I do not want to pull whole repo , as main repo has huge size 
and my local machine can not handle this size but i want to work.
i want to pull logs and commits, but don't want actuall code in my local machine
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
