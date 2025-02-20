import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np
from PIL import Image
import syft as sy  # Ensure PySyft 0.7+

# Start Duet (this will act as the server)
duet = sy.duet("server")  # Change to "client" if you're on the client side

# Define the custom dataset for lung cancer images
class LungCancerDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image = Image.open(self.image_paths[idx]).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, self.labels[idx]

# Define the CNN model
class ConvNet(nn.Module):
    def __init__(self, num_classes=2):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.fc1 = nn.Linear(32 * 56 * 56, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        return x

# Transform for image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Example dataset (update with actual paths and labels)
image_paths = ["/mnt/data/image1.png", "/mnt/data/image2.png"]
labels = [0, 1]  # Replace with actual labels

dataset = LungCancerDataset(image_paths, labels, transform=transform)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Initialize and send the model to the remote worker
num_classes = 2
model = ConvNet(num_classes=num_classes)
sy_model = sy.Module(model, torch.optim.Adam(model.parameters(), lr=0.001))
sy_model_ptr = sy_model.send(duet)

# Training loop
def train_federated_model():
    num_epochs = 5
    for epoch in range(num_epochs):
        for images, labels in dataloader:
            # Send images and labels to Duet
            images_ptr = images.send(duet)
            labels_ptr = labels.send(duet)

            # Forward pass
            outputs_ptr = sy_model_ptr(images_ptr)
            loss_ptr = torch.nn.functional.cross_entropy(outputs_ptr, labels_ptr)

            # Backward pass
            sy_model_ptr.zero_grad()
            loss_ptr.backward()
            sy_model_ptr.step()

            # Retrieve loss
            loss = loss_ptr.get()
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

# Train the model
train_federated_model()

# Save the trained model locally
torch.save(model.state_dict(), "lung_cancer_cnn.pth")
