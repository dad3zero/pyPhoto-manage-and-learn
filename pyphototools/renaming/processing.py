"""
Program which should rename photo files according to their creation date.
"""

from pathlib import Path
from datetime import datetime
import exifread

image_ext = ['.jpg', '.jpeg', '.cr2', '.cr3' '.nef', '.dng']


def get_creation_date(image_file_path):
    with open(image_file_path, 'rb') as my_picture:
        tags = exifread.process_file(my_picture)
        try:
            return datetime.strptime(str(
                tags.get('EXIF DateTimeOriginal')),
                '%Y:%m:%d %H:%M:%S')
        except ValueError:
            print("No value for ", image_file_path)
            return


def process_dir(dir_path: Path | str):
    dir_path = Path(dir_path).resolve()

    image_paths = [ifile for ifile in dir_path.iterdir()
                   if ifile.suffix.lower() in image_ext]

    for image_path in image_paths:

        picture_date = get_creation_date(image_path)

        print(f'found {picture_date}')

        if picture_date:
            renamed_file_name = picture_date.strftime('%y%m%d-%H%M%S') + image_path.suffix
            rename_path = image_path.with_name(renamed_file_name)

            if not rename_path.exists():
                image_path.rename(rename_path)
            else:
                print(f"Fichier {rename_path} existe pour le fichier {image_path}")
