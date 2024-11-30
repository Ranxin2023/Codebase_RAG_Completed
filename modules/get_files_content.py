import os
SUPPORTED_EXTENSIONS = {'.py', '.js', '.tsx', '.jsx', '.ipynb', '.java',
                         '.cpp', '.ts', '.go', '.rs', '.vue', '.swift', '.c', '.h'}

IGNORED_DIRS = {'node_modules', 'venv', 'env', 'dist', 'build', '.git',
                '__pycache__', '.next', '.vscode', 'vendor'}

def get_file_content(file_path, repo_path):
    """
    Get content of a single file.

    Args:
        file_path (str): Path to the file

    Returns:
        Optional[Dict[str, str]]: Dictionary with file name and content
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get relative path from repo root
        rel_path = os.path.relpath(file_path, repo_path)

        return {
            "name": rel_path,
            "content": content
        }
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return None


def get_main_files_content(repo_path: str):
    """
    Get content of supported code files from the local repository.

    Args:
        repo_path: Path to the local repository

    Returns:
        List of dictionaries containing file names and contents
    """
    files_content = []

    try:
        for root, _, files in os.walk(repo_path):
            # Skip if current directory is in ignored directories
            if any(ignored_dir in root for ignored_dir in IGNORED_DIRS):
                continue

            # Process each file in current directory
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.splitext(file)[1] in SUPPORTED_EXTENSIONS:
                    file_content = get_file_content(file_path, repo_path)
                    if file_content:
                        files_content.append(file_content)

    except Exception as e:
        print(f"Error reading repository: {str(e)}")

    return files_content