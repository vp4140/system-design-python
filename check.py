import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from torch.utils.data import DataLoader, Dataset
from torchfl import server, client  # Federated Learning server and client


class LungCancerDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label


# Federated model definition
class LungCancerModel(nn.Module):
    def __init__(self):
        super(LungCancerModel, self).__init__()
        self.base_model = models.resnet50(pretrained=True)
        self.base_model.fc = nn.Linear(self.base_model.fc.in_features, 2)  # 2 classes: benign, malignant

    def forward(self, x):
        return self.base_model(x)


# Define training function
def train(model, data, optimizer, criterion):
    model.train()
    for images, labels in DataLoader(data, batch_size=16):
        optimizer.zero_grad()
        predictions = model(images)
        loss = criterion(predictions, labels)
        loss.backward()
        optimizer.step()
    return model


# Step 1: Initialize federated clients and server
def federated_training():
    # Initializing two federated clients
    client_1 = client.FederatedClient(id="client_1")
    client_2 = client.FederatedClient(id="client_2")

    # Send data to clients
    client_1.send_data(LungCancerDataset(image_paths_1, labels_1, transform))
    client_2.send_data(LungCancerDataset(image_paths_2, labels_2, transform))

    # Server receiving model updates
    federated_server = server.FederatedServer()
    federated_server.add_client(client_1)
    federated_server.add_client(client_2)

    # Step 2: Training loop
    model = LungCancerModel()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(5):
        print(f"Epoch {epoch + 1}")

        # Train on client 1 and client 2
        model = train(model, client_1.get_data(), optimizer, criterion)
        model = train(model, client_2.get_data(), optimizer, criterion)

        # Federated averaging
        federated_server.aggregate()

    # Save model after training
    torch.save(model.state_dict(), "lung_cancer_federated_model.pth")
