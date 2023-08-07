import os
from git import Repo

# Automatically commits and pushes to the GitHub repository

def git_commit_and_push():
    repo_path = os.environ.get("REPO_PATH")
    ssh_key = os.environ.get("SSH_KEY")

    os.environ["GIT_SSH_COMMAND"] = f"ssh -i <(echo '{ssh_key}')"
    repo = Repo(repo_path)
    repo.git.checkout("main")  # Switch to the "main" branch
    repo.git.add('Project/db/echo.db')
    repo.git.commit("-m", "Automatic monthly database update")
    repo.git.push()

# Main
if __name__ == '__main__':
    git_commit_and_push()
