import os
import glob


def get_files(file_path):
    all_files = []
    for root, _, files in os.walk(file_path):
        files = glob.glob(os.path.join(root, '*.json'))
        for file in files:
            all_files.append(os.path.abspath(file))
    return all_files
