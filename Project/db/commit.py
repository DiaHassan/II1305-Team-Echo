import os
from git import Repo

# Automatically commits and pushes to the GitHub repository

def git_commit_and_push():
    repo_path = os.environ.get("REPO_PATH")
    ssh_key_path = os.environ.get("SSH_KEY_PATH")

    os.environ["GIT_SSH_COMMAND"] = f"ssh -i {ssh_key_path}"
    repo = Repo(repo_path)
    repo.git.checkout("to-be-published-2")  # Switch to the "to-be-published-2" branch
    repo.git.add('Project/db/echo.db')
    repo.git.commit("-m", "Automatic monthly database update")
    repo.git.push()

# Main
if __name__ == '__main__':
    git_commit_and_push()
