import os
from git import Repo

def git_commit_and_push():
    repo_path = os.environ.get("REPO_PATH")
    ssh_key_path = os.environ.get("SSH_KEY_PATH")

    os.environ["GIT_SSH_COMMAND"] = f"ssh -i {ssh_key_path}"
    repo = Repo(repo_path)
    repo.git.checkout("to-be-published")  # Switch to the "main" branch
    repo.git.add('echo.db')
    repo.git.commit("-m", "This commit was added through Zeet")
    repo.git.push()

# Main
if __name__ == '__main__':
    git_commit_and_push()