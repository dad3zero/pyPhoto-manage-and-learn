import argparse
from pathlib import Path

def remove_jpg_from_raw(dir_path:Path|str, missing_ok:bool=True):
    photodir = Path(dir_path).resolve()

    for file in photodir.glob('*.CR2'):
        jpg_name = file.with_suffix(".JPG")

        jpg_name.unlink(missing_ok=missing_ok)

parser = argparse.ArgumentParser()
parser.add_argument("source_dir", help="Source dir containing RAW+jpg files")
args = parser.parse_args()

source_dir = Path(args.source_dir).resolve()

if source_dir.is_dir():
    remove_jpg_from_raw(source_dir)
else:
    print(f"Le répertoire {source_dir} n'existe pas")
