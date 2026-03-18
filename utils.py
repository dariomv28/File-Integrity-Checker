import os

def get_all_files(path):
    """
    Returns a list of files from path
    - If path is file → return [path]
    - If path is folder → return all files inside (recursive)
    - If path doesn't exist → return []
    """
    if not os.path.exists(path):
        return []
    if os.path.isfile(path):
        return [path]
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            f_path = os.path.join(path, f)
            file_list.append(f_path)
    return file_list