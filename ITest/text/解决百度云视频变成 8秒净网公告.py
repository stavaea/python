#coding:utf-8

import hashlib
import shutil
import os
from os import walk
from os import listdir

def get_filepaths(directory):
    file_paths = []

    for root, dircetories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            extension = os.path.splitext(filename)[1][1:]
            if extension in ('jpg', 'png', 'torrent'):
                os.remove(filepath)
            else:
                file_paths.append(filepath)

    return file_paths

dir = '' #自己的dir
new_file_name = []

files = get_filepaths(dir)

for file in files:
    filename, file_extension = os.path.splitext(file)
    new_file_name = filename + 'bak' + file_extension

    with open(file, 'a') as testFile:
        testFile.write('ah')

print ('done')