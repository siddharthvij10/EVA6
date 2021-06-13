# -*- coding: utf-8 -*-

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import warnings
from torchvision import datasets, transforms
warnings.filterwarnings("ignore")

drop_out_val = 0.05

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
        ) 

        self.LN1 = nn.LayerNorm(torch.Size([8, 28, 28]))  # (x.size()[1:])
        self.DO = nn.Dropout(p=drop_out_val)

        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
        ) 
        self.LN2 = nn.LayerNorm(torch.Size([8, 28, 28]))  # (x.size()[1:])

        self.pool1 = nn.MaxPool2d(2, 2) 

        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
        ) 
        self.LN3 = nn.LayerNorm(torch.Size([16, 14, 14]))  # (x.size()[1:])

        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
        ) 
        self.LN4 = nn.LayerNorm(torch.Size([16, 14, 14]))  # (x.size()[1:])

        self.pool2 = nn.MaxPool2d(2, 2) 
        self.convblock100 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=8, kernel_size=(1, 1), padding=0, bias=False),
        ) 

        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),
          )
        self.LN5 = nn.LayerNorm(torch.Size([16, 5, 5]))  # (x.size()[1:])

        self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),
        ) 
        self.LN6 = nn.LayerNorm(torch.Size([16, 3, 3]))  # (x.size()[1:])

        self.gap = nn.Sequential(nn.AvgPool2d(3)) 
        self.fc = nn.Linear(16, 10) 


    def forward(self, x):
        x = self.convblock1(x)
        x = self.LN1(x)
        x = self.DO(x)  
        x = self.convblock2(x)
        x = self.LN2(x)
        x = self.DO(x)  
        x = self.pool1(x)
        x = self.convblock3(x)
        x = self.LN3(x)
        x = self.DO(x)  
        x = self.convblock4(x)
        x = self.LN4(x)
        x = self.DO(x)  
        x = self.pool2(x)
        x = self.convblock100(x)
        x = self.convblock5(x)
        x = self.LN5(x)
        x = self.DO(x)  
        x = self.convblock6(x)
        x = self.LN6(x)
        x = self.DO(x)  
        x = self.gap(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return F.log_softmax(x)
