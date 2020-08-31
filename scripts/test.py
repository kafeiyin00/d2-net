import torch
import torch.nn as nn
import torch.nn.functional as F

import torchvision.models as models

model = models.vgg16()
vgg16_layers = [
    'conv1_1', 'relu1_1', 'conv1_2', 'relu1_2',
    'pool1',
    'conv2_1', 'relu2_1', 'conv2_2', 'relu2_2',
    'pool2',
    'conv3_1', 'relu3_1', 'conv3_2', 'relu3_2', 'conv3_3', 'relu3_3',
    'pool3',
    'conv4_1', 'relu4_1', 'conv4_2', 'relu4_2', 'conv4_3', 'relu4_3',
    'pool4',
    'conv5_1', 'relu5_1', 'conv5_2', 'relu5_2', 'conv5_3', 'relu5_3',
    'pool5'
]
conv4_3_idx = vgg16_layers.index('conv4_3')

model1 = nn.Sequential(
    *list(model.features.children())[: conv4_3_idx + 1]
)