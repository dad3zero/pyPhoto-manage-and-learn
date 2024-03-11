from pathlib import Path

def remove_jpg_from_raw(dir_path:Path|str, missing_ok:bool=True):
    photodir = Path(dir_path).resolve()

    for file in photodir.glob('*.CR2'):
        jpg_name = file.with_suffix(".JPG")

        jpg_name.unlink(missing_ok=missing_ok)

def remove_raw_without_sidecar(dir_path:Path|str):
    pass