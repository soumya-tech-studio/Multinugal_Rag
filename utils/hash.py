import hashlib
def generate_hash(file):
    sha256=hashlib.sha256()
    file.file.seek(0)
    while chunk:=file.file.read(8196):
        sha256.update(chunk)
    file.file.seek(0)
    return sha256.hexdigest()
    
    
    