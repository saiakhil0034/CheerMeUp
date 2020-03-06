#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch
import torchvision.transforms as transforms
import torch.utils.data as data
import os
import pickle
import numpy as np
import pandas as pd
from PIL import Image


# In[3]:


class FergDataset(data.Dataset):
    def __init__(self, csv_file, transform=None):
        self.data      = pd.read_csv(csv_file)
        self.transform = transform
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_name   = self.data.iloc[idx, 0]
        img   = Image.open(img_name)
        
        if self.transform:
            img = self.transform(img)
        return img
    
def get_loader(csv_file, transforms, batch_size, shuffle, num_workers):
    fergDataset = FergDataset(csv_file, transforms)
    
    data_loader = torch.utils.data.DataLoader(dataset=fergDataset, 
                                              batch_size=batch_size, 
                                              shuffle=shuffle, 
                                              num_workers=num_workers)
    return data_loader


# In[ ]:




