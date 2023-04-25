'''performs machine learning from a prepared image data folder and csv file
'''

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, models, transforms
from PIL import Image

# Read csv file
df = pd.read_csv('image_data.csv')

# Create dataset class
class ImageDataset(Dataset):
    def __init__(self, df, transform=None):
        self.df = df
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        # Load image from file
        img_name = self.df.iloc[index, 0]
        image = Image.open(img_name)

        # Apply transformations if any
        if self.transform is not None:
            image = self.transform(image)

        # Get label
        label = self.df.iloc[index, 1]

        return image, label

# Define transformations
transform = transforms.Compose([transforms.ToTensor()])

# Create dataset and dataloader
dataset = ImageDataset(df, transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Create model
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

# Train the model
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Train the model
model.train()
for epoch in range(50):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(dataloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        #if i % 2000 == 1999:    # print every 2000 mini-batches
        print('[%d, %5d] loss: %.3f' %
                (epoch + 1, i + 1, running_loss / 1))
        running_loss = 0.0

print('Finished Training')

# Evaluate the model
correct = 0
total = 0
with torch.no_grad():
    for data in dataloader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the test images: %d %%' % (
    100 * correct / total))

# Save the model
torch.save(model.state_dict(), 'model.pth')