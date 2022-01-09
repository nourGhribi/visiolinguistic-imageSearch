import os
import torch
import torchvision.datasets as datasets
import torch.utils.data as data
from PIL import Image
from torchvision import transforms as tf
from glob import glob
import numpy as np
from pathlib import Path
import json
from collections import OrderedDict

def read_json(fname):
    with Path(fname).open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)

# Data: Dataset ? ImageFolder? 
class FASHIONIQ(data.Dataset):
    def __init__(self, data_dir, all=True, train=True, transform1=None, transform2=None, embedding=None, show=False):

        self.data_dir = data_dir
        self.image_dir = os.path.join(self.data_dir, "resized_images")

        if embedding is not None:
            self.embedding = np.load(embedding)
        else:
            self.embedding = None

        self.transform1 =  transform1
        self.transform2 =  transform2
        
        self.train=train
        self.all = all
        self.train_data = read_json(Path(self.data_dir + "/split_train.json"))
        self.test_data = read_json(Path(self.data_dir+"/split_train.json"))
        self.show = show

        self.categories = {'dress':0,'shirt':1,'toptee':2}

        # Train or Test
        if self.all:
            self.data = self.train_data + self.test_data
        else:
            self.data = self.train_data
        self.data_length = len(self.data)
            
    def __len__(self):
        return self.data_length


    def __getitem__(self, index):
        image_id = self.data[index]['image_id']

        #Get image
        fname = image_id + '.jpg'
        img = Image.open(os.path.join(self.image_dir, fname)).convert('RGB')

        if self.transform1 is not None:
            img_trans1 = self.transform1(img)
        else:
            img_trans1 = img

        if self.transform2 is not None:
            img_trans2 = self.transform2(img)
        else:
            img_trans2 = img

        if self.embedding is not None:
            emb = self.embedding[index]
        else:
            emb = None

        if self.show:
            mean = np.array([0.485, 0.456, 0.406])
            std = np.array([0.229, 0.224, 0.225])

            img_trans1 = img_trans1.numpy().transpose([1, 2, 0]) * std + mean
            # img_trans1 = img_trans1.numpy().transpose([1, 2, 0])
            # img_trans1 = (img_trans1 - img_trans1.min()) / (img_trans1.max() - img_trans1.min())
            plt.figure()
            plt.imshow(img_trans1)

            img_trans2 = img_trans2.numpy().transpose([1, 2, 0]) * std + mean
            plt.figure()
            plt.imshow(img_trans2)
            plt.show()

        #Get Image meta info
        meta_info = {'image': img, 'image_id': image_id}
        
        #Get class
        target = self.data[index]['class']
        
        if emb is not None:
            return img_trans1, img_trans2, emb, target, index
        else:
            return img_trans1, img_trans2, target, index