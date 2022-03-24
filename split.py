import glob
from pathlib import Path
import os.path
import shutil

Path("train/images").mkdir(parents=True, exist_ok=True)
Path("valid/images").mkdir(parents=True, exist_ok=True)
Path("train/labels").mkdir(parents=True, exist_ok=True)
Path("valid/labels").mkdir(parents=True, exist_ok=True)
count = 0
for filename in glob.glob('*.jpg'):
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    print(filename)
    count = count + 1
    if count == 4:
        shutil.copyfile(basename_without_ext + '.jpg', 'valid/images/' + basename_without_ext + '.jpg')
        shutil.copyfile(basename_without_ext + '.txt', 'valid/labels/' + basename_without_ext + '.txt')

        count = 0
    else:
        shutil.copyfile(basename_without_ext + '.jpg', 'train/images/' + basename_without_ext + '.jpg')
        shutil.copyfile(basename_without_ext + '.txt', 'train/labels/' + basename_without_ext + '.txt')


