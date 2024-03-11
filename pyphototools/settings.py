from pathlib import Path

ROOT_DIR = Path('.').resolve().parent.parent

#  Global parameters
verbose = False
is_test = False

#  Parameters for the renaming action
date_format = "%y%m%d-%H%M%S"  # Renaming format
processing_dir = None  # Path to the directory to process