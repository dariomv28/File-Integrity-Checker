import hashlib

def hash_file(path, chunk_size=4096):
    sha256 = hashlib.sha256()
    try:
        with open(path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[ERROR] {e}")
        return None