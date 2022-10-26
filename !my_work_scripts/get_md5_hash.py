import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--File', nargs='?')
args = parser.parse_args()

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print (md5(args.File))