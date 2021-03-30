# Contributing guidelines

## Before contributing

Welcome to [geekquad/Image-Processing-OpenCV](https://github.com/geekquad/AlgoBook). Before sending your pull requests, make sure that you **read the whole guidelines**.


* Make sure you do not copy codes from external sources because that work will not be considered. Plagiarism is strictly not allowed.
* You can only work on issues that have been assigned to you.
* If you want to contribute to an existing algorithm, we prefer that you create an issue before making a PR and link your PR to that issue.
* If you have modified/added code work, make sure the code compiles before submitting.

### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Follow PEP8 guidelines. Read more about it <a href="https://pep8.org/"> here. </a>
- Please write in Python 3.7+.  __print()__ is a function in Python 3 so __print "Hello"__ will _not_ work but __print("Hello")__ will.
- Please focus hard on naming of functions, classes, and variables.  Help your reader by using __descriptive names__ that can help you to remove redundant comments.
  - Please follow the [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions) so variable_names and function_names should be lower_case, CONSTANTS in UPPERCASE, ClassNames should be CamelCase, etc.
  - Expand acronyms because __gcf()__ is hard to understand but __greatest_common_factor()__ is not.

- Using only OpenCV modules are highly recommended.
- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms.
- If you need a third party module that is not in the file __requirements.txt__, please add it to that file as part of your submission.

#### Other points to remember while submitting your work:
- **We won't be accepting just the dataset in the form of PRs.** If you are using any of the dataset in the implementation, then only we'll accept it.
- Jupyter notebook files should be there with proper step-wise implementation.
- Each file should contain a dedicated README.md document so that it is easy for others to understand your approach and the logic behind your implementation.
- File extension for code should be `.py`. 
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure. If you want to create a new directory, please contact us on our <a href="https://join.slack.com/t/geekquad/shared_invite/zt-l3t67zvr-JMKbn57PpxjEi7uC2k0etg"> Slack </a> channel.
- If you have modified/added code work, make sure the code compiles before submitting.
- If you have modified/added documentation work, ensure that your language is concise and contains no grammatical errors.
- Do not update the README.md and CONTRIBUTING.md.

## How to Contribute ?

## GIT AND GITHUB

Before proceeding, we want to clarify the difference between Git and Github. Git is a version control system(VCS) which is a tool to manage the history of our Source Code. GitHub is a hosting service for Git projects.

We assume that you have already created an account on Github and have Git installed on your system.

Now tell Git your name and E-mail (used on Github) address.

     $ git config --global user.name "YOUR NAME"
     $ git config --global user.email "YOUR EMAIL ADDRESS"
     

This is an important step to mark your commits to your name and email.

### FORK A PROJECT -

You can use github explore - https://github.com/explore to find a project that interests you and match your skills. Once you find a cool project to work on, you can make a copy of project to your account. This process is called forking a project to your Github account. On Upper right side of project page on Github, you can see -

<p align="center">  <img  src="https://i.imgur.com/P0n6f97.png">  </p>

Click on fork to create a copy of project to your account. This creates a separate copy for you to work on.

### FINDING A FEATURE OR BUG TO WORKON - 

Open Source projects always have something to workon and improves with each new release. You can see the issues section to find something you can solve or report a bug. The project managers always welcome new contributors and can guide you to solve the problem. You can find issues in the right section of project page.

<p align="center">  <img  src="https://i.imgur.com/czVjpS7.png">  </p>

### CLONE THE FORKED PROJECT -

You have forked the project you want to contribute to your github account. To get this project on your development machine we use clone command of git.

```$ git clone https://github.com/<your-account-username>/<your-forked-project>.git```  
Now you have the project on your local machine.

### ADD A REMOTE (UPSTREAM) TO ORIGINAL PROJECT REPOSITORY 

Remote means the remote location of project on Github. By cloning, we have a remote called origin which points to your forked repository. Now we will add a remote to the original repository from where we had forked.

    $ cd <your-forked-project-folder>
    $ git remote add upstream https://github.com/<author-account-username>/<project>.git
    
You will see the benefits of adding remote later.

### SYNCHRONIZING YOUR FORK -

Open Source projects have a number of contributors who can push code anytime. So it is necessary to make your forked copy equal with the original repository. The remote added above called Upstream helps in this.


    $ git checkout master
    $ git fetch upstream
    $ git merge upstream/master
    $ git push origin master
  

The last command pushes the latest code to your forked repository on Github. The origin is the remote pointing to your forked repository on github.

### CREATE A NEW BRANCH FOR A FEATURE OR BUGFIX -

Normally, all repositories have a master branch which is considered to remain stable and all new features should be made in a separate branch and after completion merged into master branch. So we should create a new branch for our feature or bugfix and start working on the issue.

```$ git checkout -b <feature-branch>```
This will create a new branch out of master branch. Now start working on the problem and commit your changes.

    $ git add --all
    $ git commit -m "<commit message>"
    

The first command adds all the files or you can add specific files by removing -a and adding the file names. The second command gives a message to your changes so you can know in future what changes this commit makes. If you are solving an issue on original repository, you should add the issue number like #35 to your commit message. This will show the reference to commits in the issue.

### REBASE YOUR FEATURE BRANCH WITH UPSTREAM-

It can happen that your feature takes time to complete and other contributors are constantly pushing code. After completing the feature, your feature branch should be rebase on latest changes to upstream master branch.

    $ git checkout <feature-branch>
    $ git pull --rebase upstream master

Now you get the latest commits from other contributors and check that your commits are compatible with the new commits. If there are any conflicts, solve them.

### SQUASHING YOUR COMMITS-

You have completed the feature, but you have made a number of commits which make less sense. You should squash your commits to make good commits.

```$ git rebase -i HEAD~5```    
This will open an editor which will allow you to squash the commits.

### PUSH CODE AND CREATE A PULL REQUEST -

Till this point you have a new branch with the feature or bugfix you want in the project you had forked. Now push your new branch to your remote fork on github.

```$ git push origin <feature-branch>```
    
Now you are ready to help the project by opening a pull request, which means that you can now tell the project managers to add the feature or bugfix to the original repository. You can open a pull request by clicking on the green icon -

<p align="center">  <img  src="https://i.imgur.com/aGaqAD5.png">  </p>

Remember, your upstream base branch should be master and source should be your feature branch. Click on create pull request and add a name to your pull request. You can also describe your feature.

Awesome! You have made your first contribution. If you have any doubts please let me know in the comments.

#### BE OPEN!


**Join our <a href="https://join.slack.com/t/geekquad/shared_invite/zt-l3t67zvr-JMKbn57PpxjEi7uC2k0etg"> Slack </a> channel now.**
Happy Coding :)

