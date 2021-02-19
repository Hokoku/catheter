import os
import cv2
import zipfile
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from matplotlib import pyplot as plt

train = pd.read_csv(
    '../input/ranzcr-clip-catheter-line-classification/train.csv')

TRAIN_PATH = '../input/ranzcr-clip-catheter-line-classification/train/'

with zipfile.ZipFile(f'train.zip', 'w') as img_out:
    for uid in tqdm(train['StudyInstanceUID'].values):
        image = cv2.imread(TRAIN_PATH + f'{uid}.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (640, 640))
        image = cv2.imencode('.png', image)[1]
        img_out.writestr(f"{uid}.png", image)
