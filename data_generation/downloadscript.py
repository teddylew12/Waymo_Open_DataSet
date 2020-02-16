# -*- coding: utf-8 -*-
"""DownloadScript

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TwFRq2T7gpfW6BE4KS4bKMo5EffZvtP
"""

from google.colab import drive
drive.mount('/content/drive/')

!ls "/content/drive/Shared drives/Waymo Project"

from google.colab import auth
auth.authenticate_user()



import time
import tqdm #Allows for progress bar
i_start = 5 #inclusive beginning
j_end = 11 #exclusive end

def download():
  for i in tqdm.tqdm(range(i_start,j_end)):
    if i not in [10,11]:
      if i<10:
      
        src = f'gs://waymo_open_dataset_v_1_0_0/training/training_000{i}.tar'
        tmp = f'/content/drive/Shared\\ drives/Waymo\\ Project/tmp/0{i}.tar'
        name = f'/content/drive/Shared\\ drives/Waymo\\ Project/Data/Data_No_2D_Labels/0{i}'
      else:
        src = f'gs://waymo_open_dataset_v_1_0_0/training/training_00{i}.tar'
        tmp = f'/content/drive/Shared\\ drives/Waymo\\ Project/tmp/{i}.tar'
        name = f'/content/drive/Shared\\ drives/Waymo\\ Project/Data/Data_No_2D_Labels/{i}'
      print(src, name)
      !mkdir -p $name
      print("Downloading",src)
      !gsutil cp $src $tmp
      print("Untarring", tmp)
      !tar -xf $tmp -C $name
      !rm $tmp
download()

src = f'gs://waymo_open_dataset_v_1_0_0/training/training_00{i}.tar'
tmp = f'/content/drive/Shared\\ drives/Waymo\\ Project/tmp/{i}.tar'
name = f'/content/drive/Shared\\ drives/Waymo\\ Project/Data/Data_No_2D_Labels/{i}'
print(src, name)
!mkdir -p "$name"

a = "/content/drive/Shared\\ drives/Waymo\ Project/Data/Data_No_2D_Labels/19"
! mkdir -p $a

gcs_service.get('waymo_open_dataset_v_1_0_0')

import time
import tqdm #Allows for progress bar
i_start = 12 #inclusive beginning
j_end = 16 #exclusive end
def download(i_s,j_e):
  for i in tqdm.tqdm(range(i_s,j_e)):
    if i not in [10,11]:
      if i<10:
      
        src = f'gs://waymo_open_dataset_v_1_0_0/training/training_000{i}.tar'
        tmp = f'/content/drive/Shared\\ drives/Waymo\\ Project/tmp/0{i}.tar'
        name = f'/content/drive/Shared\\ drives/Waymo\\ Project/Data/Data_No_2D_Labels/0{i}'
      else:
        src = f'gs://waymo_open_dataset_v_1_0_0/training/training_00{i}.tar'
        tmp = f'/content/drive/Shared\\ drives/Waymo\\ Project/tmp/{i}.tar'
        name = f'/content/drive/Shared\\ drives/Waymo\\ Project/Data/Data_No_2D_Labels/{i}'
      print(src, name)
      !mkdir -p $name
      print("Downloading",src)
      !gsutil cp $src $tmp
      print("Untarring", tmp)
      !tar -xf $tmp -C $name
      !rm $tmp
download(12,16)

rm -rf /content/drive
