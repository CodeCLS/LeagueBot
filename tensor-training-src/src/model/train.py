import torch
from torchvision import models, transforms
from torch.utils.data import DataLoader
import os
import json
from src.utils.dataset import CustomObjectDetectionDataset  # Assuming you store your dataset class here


# Initialize model
def get_model():
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    num_classes = 11  # Adjust for the number of classes in your dataset (10 classes + background)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)
    return model


# Set up data transformations
transform = transforms.Compose([
    transforms.ToTensor()
])

# Set up dataset and dataloaders
train_dataset = CustomObjectDetectionDataset(
    image_dir='data/images/train',
    annotation_file='data/annotations/train_annotations.json',
    transform=transform
)

train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True)


# Set up the training loop
def train(model, dataloader, device, num_epochs=10):
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

    for epoch in range(num_epochs):
        running_loss = 0.0
        for images, targets in dataloader:
            images = [image.to(device) for image in images]
            targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

            optimizer.zero_grad()
            loss_dict = model(images, targets)

            losses = sum(loss for loss in loss_dict.values())
            losses.backward()
            optimizer.step()

            running_loss += losses.item()

        print(f'Epoch #{epoch + 1} - Loss: {running_loss / len(dataloader):.4f}')


# Initialize device and model
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = get_model().to(device)

# Train the model
train(model, train_dataloader, device, num_epochs=10)

# Save the trained model
torch.save(model.state_dict(), 'model.pth')
