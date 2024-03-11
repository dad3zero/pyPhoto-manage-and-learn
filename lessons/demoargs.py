import argparse
parser = argparse.ArgumentParser()


parser.add_argument("source_dir", help="Source directory of the files to process")

args = parser.parse_args()
print(args.source_dir)