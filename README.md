# Erstsemester-DT-Projekt

Download GitHub Collaboration Guide


1. Cloning the Main Repository
First, team members should clone the main repository that you have created on GitHub to their own systems.

1.1. Provide the GitHub repository URL to your team members. This URL can be found on the repository page on GitHub, and it typically looks like this:
   ```
   https://github.com/username/repo-name.git
   ```

1.2. Each member should run this command in their terminal (or Git Bash) to clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git
   ```

1.3. After cloning, a folder with the repository name will be created on each member’s system, and the main project files and structure will be accessible within that folder.

2. Creating a New Branch
After each member has cloned the main repository, they can create a separate branch for themselves. Branching allows each person to work on their own section of code without interfering with others' code.

2.1. First, navigate to the project directory (if not already inside it):
   ```bash
   cd repo-name
   ```

2.2. To create a new branch, run the following command. Choose a branch name related to your name or the feature you’re working on, like `feature/ali` or `bugfix/ali`.
   ```bash
   git checkout -b feature/ali-feature
   ```
   - This command creates a new branch named `feature/ali-feature` and switches you to that branch.

2.3. Now any changes you make will only affect this branch and won’t interfere with the main branch.

3. Making Changes and Committing
After each member has created their own branch, they can start making changes to their code within that branch.

3.1. After making the necessary changes in the code, first, add the changes to Git:
   ```bash
   git add .
   ```
   - This command stages all the modified files for commit.

3.2. Now commit the changes to save them in Git with a descriptive message:
   ```bash
   git commit -m "Short description of the changes"
   ```
   - The message should be short and clear, for example: `"Added login form"`.

4. Pushing the Branch to the Main Repository
Once the changes are committed to the individual branch, they need to be pushed to the main GitHub repository.

4.1. To push the branch to the main repository on GitHub, run the following command:
   ```bash
   git push origin feature/ali-feature
   ```
   - This command pushes the `feature/ali-feature` branch to the main repository on GitHub.
   - Now, your branch will be visible in the GitHub repository, and others can see it.
