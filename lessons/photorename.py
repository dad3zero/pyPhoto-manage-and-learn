#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Program which should rename photo files according to their creation date.
"""

import os
import exifread
from datetime import datetime

image_ext = ['.jpg', '.jpeg', 'cr2', 'cr3' 'nef', 'dng']


def get_creation_date(image_file_path):
    with open(image_file_path, 'rb') as my_picture:
        tags = exifread.process_file(my_picture)
        try:
            return datetime.strptime(str(
                tags.get('EXIF DateTimeOriginal')),
                '%Y:%m:%d %H:%M:%S')
        except ValueError:
            print("No value for ", image_file)
            return


image_files = [ifile for ifile in os.listdir('.')
               if os.path.splitext(ifile)[1].lower() in image_ext]

for image_file in image_files:

    file_basename, file_ext = os.path.splitext(image_file)

    picture_date = get_creation_date(image_file)

    if picture_date:
        rename_name = "/".join((os.path.dirname(image_file),
                               picture_date.strftime('%y%m%d-%H%M%S') + file_ext))
        if not os.path.exists(rename_name):
            os.rename(image_file, rename_name)
