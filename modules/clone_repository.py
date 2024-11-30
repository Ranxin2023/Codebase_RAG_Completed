import os
from github import Github, Repository
from git import Repo
"""# Clone a GitHub Repo locally"""
def clone_repository(repo_url):
    """Clones a GitHub repository to a temporary directory.

    Args:
        repo_url: The URL of the GitHub repository.

    Returns:
        The path to the cloned repository.
    """
    repo_name = repo_url.split("/")[-1]  # Extract repository name from URL
    repo_path = f"/content/{repo_name}"
    if os.path.exists(repo_path):
        print(f"Directory {repo_path} already exists. Pulling latest changes...")
        repo = Repo(repo_path)
        repo.git.pull()
    else:
        print(f"Cloning repository {repo_url} into {repo_path}...")
        Repo.clone_from(repo_url, str(repo_path))
    return str(repo_path)
