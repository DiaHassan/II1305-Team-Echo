import os
from git import Repo

def git_commit_and_push():
    repo_path = "path/to/git/repo"
    ssh_key_path = "C:/Users/username/.ssh/id_rsa"
    os.environ["GIT_SSH_COMMAND"] = f"ssh -i {ssh_key_path}"
    repo = Repo(repo_path)
    repo.git.checkout("main")  # Switch to the "main" branch
    repo.git.add('test.txt')
    repo.git.commit("-m", "This commit was added through a script")
    repo.git.push()

# Main
if __name__ == '__main__':
    git_commit_and_push()