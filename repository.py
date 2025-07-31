import os
import git

def download_github_repo(repo_url, repo_dir):
    """
    Downloads or updates a GitHub repository to the specified local directory.

    Args:
        repo_url (str): URL of the GitHub repository.
        repo_dir (str): Local directory to clone the repository into.
    """
    try:
        if os.path.exists(repo_dir):
            print(f"[INFO] Repository '{repo_dir}' already exists. Pulling latest changes...")
            repo = git.Repo(repo_dir)
            repo.remotes.origin.pull()
        else:
            print(f"[INFO] Cloning repository from '{repo_url}' to '{repo_dir}'...")
            git.Repo.clone_from(repo_url, repo_dir)
        print("[SUCCESS] Repository is ready.")
    except Exception as e:
        print(f"[ERROR] Failed to process the repository: {e}")
