# Git Setup and Workflow

## Setting Up a Git Repository on a New Mac
If you're using a new Mac and haven't set up your repository locally, follow these steps to configure Git and start working with your repository.

### Step 1: Install Git

Open Terminal (Applications > Utilities > Terminal).
Check if Git is installed by running:
```bash
git --version
```
If Git is installed, you will see the version number. If not, you can install it by running:

```bash
xcode-select --install
```
This installs Xcode Command Line Tools, which includes Git.
### Step 2: Configure Git
Once Git is installed, set up your username and email address, which Git uses for commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
### Step 3: Clone Your Repository from GitHub

Go to your GitHub repository page.
Click on the green Code button and copy the repository's HTTPS or SSH URL.
In Terminal, navigate to the directory where you want to store the repository, then run:
For HTTPS:

```bash
git clone https://github.com/your-username/your-repo-name.git
For SSH:

```bash
git clone git@github.com:your-username/your-repo-name.git
```
This command will download the repository to your local machine.

### Step 4: Navigate to the Repository

After cloning, change into your repository’s directory:

```bash
cd your-repo-name
```
Now, you’re ready to start working on your project.

Step 5: SSH Key Setup (Optional)

If you prefer using SSH to connect to GitHub, set up SSH keys:

Generate a new SSH key (if not already created):
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```
Add the SSH key to the ssh-agent:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```
Copy your SSH public key:
```bash
pbcopy < ~/.ssh/id_rsa.pub
```
Add the SSH key to GitHub:
Go to GitHub's SSH settings, click "New SSH key," and paste your key.
### Step 6: Start Working with Git

Pull the latest changes from the remote repository:
```bash
git pull origin main
```
Make changes, then add and commit them:
```bash
git add .
git commit -m "Your commit message"
```
Push your changes to the remote repository:
```bash
git push origin main
```

## Accessing a Git Repository from iCloud Drive
If you store your Git repository on iCloud Drive and need to access it or update it from your local machine, follow these steps.

### Step 1: Navigate to the iCloud Drive Directory

In Terminal, iCloud Drive is located at `~/Library/Mobile Documents/com~apple~CloudDocs/`. First, navigate to the directory:

```bash
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/
```
This is where your iCloud Drive files are stored locally. If your repository is stored there, proceed to the next step.

### Step 2: Clone the Repository to iCloud Drive (if not already there)

If your GitHub repository isn’t already in iCloud Drive, clone it directly into the iCloud folder:

```bash
git clone https://github.com/your-username/your-repo-name.git ~/Library/Mobile\ Documents/com~apple~CloudDocs/
```
This will download the repository into iCloud Drive, syncing it across devices via iCloud.

### Step 3: Pull the Latest Changes

Before making any local changes, always pull the latest changes from the remote repository:

```bash
git pull origin main
```
This ensures your local copy is up-to-date and prevents conflicts.

### Step 4: Stage, Commit, and Push Changes

After making your changes:

Stage the changes by running:
```bash
git add .
Commit the changes with a meaningful message:
git commit -m "Updated feature XYZ"
```
Push the changes back to GitHub:
```bash
git push origin main
```
Step 5: Resolve Merge Conflicts (if necessary)

If there are changes on GitHub that conflict with your local changes, Git will alert you. Open the conflicting files, resolve the conflicts manually, and then:

```bash
git add <file>
git commit -m "Resolved merge conflict in <file>"
git push origin main
```
Best Practices for Working with Git and iCloud Drive
Always git pull before starting work to make sure your local repository is in sync with the remote one.
Commit often with meaningful messages so you can track changes easily.
Resolve conflicts promptly if Git detects changes that conflict with the remote repository.
Be cautious with iCloud Drive syncing: iCloud syncs automatically but may sometimes have delays. Ensure your files are fully synced before pushing changes to avoid issues.

## Common Git Commands Recap:
Clone a repository:
```bash
git clone <repository-url>
```
Check the status of your working directory:
```bash
git status
```

Pull the latest changes:
```bash
git pull origin main
```

Add changes to the staging area:
```bash
git add .
```

Commit your changes:
```bash
git commit -m "Your message"
```

Push your changes to GitHub:
```bash
git push origin main
```
----
Here is the course from VAI 

## Git and Github

<center>
<img src="https://imgs.xkcd.com/comics/git.png">
</center>

## Learning objectives


## Pre-class assignment

### Reading

Jenny Bryan's "Excuse me, do you have a moment to talk about version control?".
The pdf was sent via email and may also be found at

 - https://scheuerell-lab.github.io/lab-book/resources/Bryan_2018_version_control.pdf

 - https://peerj.com/preprints/3159.pdf (preprint)

### Set up Github account

This repo is private and cannot be viewed without an invited account, but here
are instructions:

If you don't already have a Github account (or know another student who
doesn't), [create an account](https://github.com/signup) and email an instructor
with your username to have you added to the [class Github team](https://github.com/Bioinformatics-Training-VAI)
and [repository](https://github.com/Bioinformatics-Training-VAI/2024-data-sci-bioinfo).

### Set up git

Go to <https://github.com/git-guides/install-git> and choose one of the
installation methods.

#### MacOS

If you are on a mac, you can use `git` directly from the command line. It does
not always come pre-installed so you may need to install it.

To check if you have git already installed open Terminal and run

```bash
git version
```

If this returns a `git version 2.42.0` or other number, you have git. If you get
`command not found: git`, git is not installed on your system. I would recommend
using the
[OSX installer](https://github.com/git-guides/install-git#install-git-from-an-installer).
You may also use [homebrew](brew.sh) or get the
[GitHub Desktop](https://github.com/git-guides/install-git#install-git-using-github-desktop)
app if you prefer.

#### Windows

Windows does not have native support for command-line git. If you want to follow
the class from your local machine, install [Git for
Windows](https://github.com/git-guides/install-git#install-git-on-windows).
You may also get the [GitHub Desktop](https://github.com/git-guides/install-git#install-git-using-github-desktop)
app which will install git.

#### HPC

Alternatively, both MacOS and Windows users may run git from the HPC from either
the command line through ssh or using the [OnDemand web
server](https://ondemand.hpc.vai.org).

#### Configuration

Your local git installation does not know about your GitHub account. To add your
username and email (the one used to make your GitHub account and that will show
up in your commits), follow these instructions:

 - [set up username](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)

 - [set up email](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

### Authentication

With your username and email set, you'll need to be able to securely push and
pull changes to github. There are two ways to do this:

 - Using tokens: This is like a password that you can use when asked for a
   password during GitHub operations.
   * <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>

 - Using an SSH key: this methods connects to GitHub in the same way that you
   would connect to the HPC. It requires the creation and management of ssh
   keys.
    * <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh>

 - <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#authenticating-with-the-command-line>


[Email me](mailto:james.eapen@vai.org) if you have issues with authentication.

## Additional resources

- <https://learngitbranching.js.org/>: interactive git branching tutorial

- [Github git guides](https://github.com/git-guides/)

- [Happy Git and GitHub for the useR](https://happygitwithr.com/): R-user-focused guide

- [Publish GitHub report with RStudio](https://resources.github.com/github-and-rstudio/)

## Render slides

Slides will be emailed after class but, if you'd like to render them yourself,
install [Quarto](https://quarto.org) and download it for your system. Then, run
`quarto render git.qmd` from this directory to generate the slides.

## Session 2 homework

Your homework will be practicing the git commands we learned today and
making a fork of the class repo for future homework submissions.

### Part 1

1. Identify one thing about git and Github you understood from today that you
   could see yourself using and one that you did not understand that you would
   like clarified or explained again. You may add as many questions as you'd
   like, but think about at least one.

2. Draft an email with these two elements.

### Part 2

1. Open RStudio using the [HPC OnDemand server](https://ondemand.hpc.vai.org)
   (or your own laptop's RStudio if that's what you used in class).

2. Modify the hello_world function to plot the "cars" dataset after sending the
   "Hello World!" message. The hello_world function should look like this with
   the `plot(cars)` line added to the function:

```r
#' Prints "Hello World!"
#' @export
hello_world <- function() {
  message("Hello world!")
  plot(cars)
}
```

3. Commit this change with an informative message about what changed and push to
   Github. Then, using your Github page for hello_git that you just pushed the
   change to, find the diff of this last change and the link to this diff. Add
   this link to the email you started in Part 1.

You don't have to have run the function to complete the homework but if you'd
like to see how R packages are built and run, go to the "Build" tab next to the
"Git" tab you used to make the commit. Here click on "Install" which will
install the hello_world function. Then in the R console on the bottom, run
`hello_world()`.

![](build_run.png)

### Part 3

Finally, you'll make a copy of the class repo so that you can submit homework
for the next classes. You'll need to make a fork (or copy) of our class
repository:

1. Go to <https://github.com/Bioinformatics-Training-VAI/2024-data-sci-bioinfo>

2. In the mid-upper right side of the page, you'll see a "Fork" button. Forking
   makes a copy to your Github account, like what you did with the hello_git,
   repo so that you can work on your homework without affecting anyone else
   until you're ready to submit.

![](./fork.png)

1. Along with the link to the diff from part 2, email me the link to your newly
   forked 2024-data-sci-bioinfo repo to complete the homework for this week.
