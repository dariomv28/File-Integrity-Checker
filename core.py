from hasher import hash_file
from database import load_db, save_db
from utils import get_all_files

def init(path):
    """
    Scan all files
    Hash each file
    Save to db
    """
    db = {}
    files = get_all_files(path)
    for file in files:
        hash = hash_file(file)
        if hash is not None:
            db[file] = hash
    save_db(db)
    print('Hashes stored successfully.')

def check(path):
    """
    - Load DB
    - Rehash the current file
    - Compare
    """
    db = load_db()
    files = get_all_files(path)
    for file in files:
        get_hash = hash_file(file)
        if file not in db:
            print(f"{file} → Modified (Hash mismatch)")
            continue
        if get_hash is None:
            print(f"{file} → [ERROR]")
            continue
        if db[file] == get_hash:
            print(f"{file} → Unmodified")
        else:
            print(f"{file} → Modified (Hash mismatch)")

def update(path):
    """
    - Rehash the file
    - Update db
    """
    db = load_db()
    files = get_all_files(path)
    for file in files:
        get_hash = hash_file(file)
        if get_hash is not None:
            db[file] = get_hash
    save_db(db)
    print("Hash updated successfully.")


# update('a.txt')
