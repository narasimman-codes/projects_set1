import os
import hashlib

def file_hash(file_path):
    """Generate hash for a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # 64KB chunks
            if not data:
                break
            hasher.update(data)
    return hasher.digest()

def find_duplicates(directory):
    """Find duplicate files within a directory."""
    duplicates = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_stat = os.stat(file_path)
            file_key = (file_hash(file_path), os.path.getsize(file_path), file_stat.st_mtime)
            if file_key in duplicates:
                duplicates[file_key].append(file_path)
            else:
                duplicates[file_key] = [file_path]
    
    return {key: value for key, value in duplicates.items() if len(value) > 1}

def delete_duplicates(duplicates):
    """Delete duplicate files except for the latest modified."""
    for file_key, file_paths in duplicates.items():
        latest_file_path = max(file_paths, key=os.path.getmtime)
        for file_path in file_paths:
            if file_path != latest_file_path:
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    duplicates = find_duplicates(directory)
    if duplicates:
        print("Duplicates found:")
        for file_key, file_paths in duplicates.items():
            print(f"{len(file_paths)} duplicates of {file_paths[0]} - {file_key[1]} bytes")
            for file_path in file_paths:
                print(f"  {file_path}")
        delete_duplicates(duplicates)
    else:
        print("No duplicates found.")
