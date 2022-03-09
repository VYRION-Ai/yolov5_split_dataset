import cv2
import glob
from PIL import Image
import os
import os.path
from os import path
import math
import os
from copy import copy
from pathlib import Path
import glob
from pathlib import Path
from PIL import Image
import os.path
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import torch
from PIL import Image, ImageDraw, ImageFont
import shutil

Path("train").mkdir(parents=True, exist_ok=True)
Path("valid").mkdir(parents=True, exist_ok=True)
count = 0
for filename in glob.glob('images/*.jpg'):
     basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
     img = cv2.imread(filename)
     print(filename)
     count = count + 1
     if count == 4:
         shutil.copyfile('images/' + basename_without_ext + '.txt', 'valid/' + basename_without_ext + '.txt')
         cv2.imwrite('valid/' + basename_without_ext + '.jpg', img)
         count = 0
     else:
         shutil.copyfile('images/' + basename_without_ext + '.txt', 'train/' + basename_without_ext + '.txt')
         cv2.imwrite('train/' + basename_without_ext + '.jpg', img)
count=0
for filename in glob.glob('images/*.jpeg'):
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    img = cv2.imread(filename)
    print(filename)
    count = count + 1
    if count == 4:
        shutil.copyfile('images/' + basename_without_ext + '.txt', 'valid/' + basename_without_ext + '.txt')
        cv2.imwrite('valid/' + basename_without_ext + '.jpeg', img)
        count = 0
    else:
        shutil.copyfile('images/' + basename_without_ext + '.txt', 'train/' + basename_without_ext + '.txt')
        cv2.imwrite('train/' + basename_without_ext + '.jpeg', img)
count=0
for filename in glob.glob('images/*.png'):
    basename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    img = cv2.imread(filename)
    print(filename)
    count = count + 1
    if count == 4:
        shutil.copyfile('images/' + basename_without_ext + '.txt', 'valid/' + basename_without_ext + '.txt')
        cv2.imwrite('valid/' + basename_without_ext + '.png', img)
        count = 0
    else:
        shutil.copyfile('images/' + basename_without_ext + '.txt', 'train/' + basename_without_ext + '.txt')
        cv2.imwrite('train/' + basename_without_ext + '.png', img)