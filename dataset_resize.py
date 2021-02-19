from PIL import Image
from glob import glob
import os
from tqdm import tqdm

dataset_dir = "../input/ranzcr-clip-catheter-line-classification/train/"
dest_dir = "../input/ranzcr-256x256-dataset/"
size = (256, 256)

for path in tqdm(glob(dataset_dir+"*")):
    file_name = os.path.splitext(os.path.basename(path))[0]

    img = Image.open(path)
    img_resized = img.resize(size, Image.LANCZOS)
    img_resized.save(dest_dir+file_name+".png")
