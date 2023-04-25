'''make prediction with using models
'''

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms
from torchvision.transforms import ToTensor
from PIL import Image

#Device Configuration
def get_device(use_gpu):
    if use_gpu and torch.cuda.is_available():
        torch.backends.cudnn.deterministic = True
        return torch.device("cuda")
    else:
        return torch.device("cpu")

device = get_device(use_gpu=True)

# Define transformations to preprocess data
transform = transforms.Compose([transforms.ToTensor()])

#Load image data
img = Image.open('frame17.jpg')
inputs = transform(img)
inputs = inputs.unsqueeze(0)

#Model Loading
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load("model-test.pth"))

#Prediction Execution
with torch.no_grad():
    output = model(inputs)
    _, predicted = torch.max(output.data,1)

#Result Output
if predicted.item() == 0:
    print('result: 0')
else:
    print('result: 1')
