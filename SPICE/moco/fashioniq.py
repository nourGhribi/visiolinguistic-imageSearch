from PIL import Image
import os
import os.path
import numpy as np
from typing import Any, Callable, Optional, Tuple

from pathlib import Path
import json
from collections import OrderedDict

from torchvision.datasets.vision import VisionDataset
from torchvision.datasets.utils import check_integrity, download_and_extract_archive, verify_str_arg

import torch.utils.data as data

def read_json(fname):
    with Path(fname).open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)

class FASHIONIQ(data.Dataset):
    def __init__(self, data_dir, all, transform):

        self.data_dir = data_dir
        self.transform=  transform
        self.image_dir = os.path.join(self.data_dir, "resized_images")
        self.all = all
        self.train_data = read_json(Path(self.data_dir + "/split_train.json"))
        self.test_data = read_json(Path(self.data_dir+"/split_train.json"))
        # Train or Test
        if self.all:
            self.data = self.train_data + self.test_data
        else:
            self.data = self.train_data
        self.data_length = len(self.data)
        self.categories = {'dress':0,'shirt':1,'toptee':2}
            
    def __len__(self):
        return self.data_length

    def __getitem__(self, index):
        image_id = self.data[index]['image_id']

        #Get image
        fname = image_id + '.jpg'
        image_orig = Image.open(os.path.join(self.image_dir, fname)).convert('RGB')
        image = self.transform(image_orig)

        #Get Image meta info
        meta_info = {'image': image, 'image_id': image_id}
        
        #Get class
        target = self.data[index]['class']
        
        return image, target