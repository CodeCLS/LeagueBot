import torch
import torchvision
from torch.utils.data import DataLoader
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import torchvision.transforms as T
from src.utils.dataset import CustomObjectDetectionDataset

model = fasterrcnn_resnet50_fpn(pretrained=True)
def start():
    # Set device to GPU if available
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    # Define transforms for training
    transform = T.Compose([
        T.ToTensor(),
        # Add more transforms if needed (e.g., data augmentation)
    ])

    image_dir = '../data/images'
    annotation_file = '../data/annotations/train.json'
    dataset = CustomObjectDetectionDataset(image_dir=image_dir, annotation_file=annotation_file, transform=transform)

    # Split into train and validation datasets if needed
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

    # Dataloader
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))
    val_loader = DataLoader(val_dataset, batch_size=4, shuffle=False, collate_fn=lambda x: tuple(zip(*x)))

    # Load the Faster R-CNN model
    num_classes = 2  # Update this to match your dataset (1 class + background)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)

    # Move model to device
    model.to(device)

    # Define optimizer and learning rate
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
    num_epochs = 40

    # Training loop
    for epoch in range(num_epochs):
        train_one_epoch(model, optimizer, train_loader, device, epoch)
        evaluate(model, val_loader, device)

# Save the trained model

# Training function
def train_one_epoch(model, optimizer, data_loader, device, epoch):
    model.train()
    total_loss = 0
    for images, targets in data_loader:
        # Move images and targets to device
        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        # Forward pass and calculate loss
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())

        # Backpropagation
        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

        total_loss += losses.item()


    print(f"Epoch {epoch + 1}, Loss: {total_loss / len(data_loader)}")

# Evaluation function (basic)
# Evaluation function (modified to calculate loss)
def evaluate(model, data_loader, device):
    model.train()  # Keep the model in train mode to calculate loss
    total_loss = 0
    for images, targets in data_loader:
        images = list(img.to(device) for img in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        # Calculate loss
        loss_dict = model(images, targets)  # Get a dictionary of losses
        losses = sum(loss for loss in loss_dict.values())
        total_loss += losses.item()
    model.eval()  # Keep the model in train mode to calculate loss

    print(f"Validation Loss: {total_loss / len(data_loader)}")




if __name__ == "__main__":
    start()
    torch.save(model.state_dict(), "fasterrcnn_model.pth")


