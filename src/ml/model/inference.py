import torch
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

# Load the Faster R-CNN model with the same backbone as the one used in training
model = fasterrcnn_resnet50_fpn(pretrained=False)  # pretrained=False, as you're loading a custom model

# Number of classes (update to the number used during training, including background)
num_classes = 2  # e.g., 1 class + background

# Modify the box predictor to match the number of classes
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
model.roi_heads.score_thresh = 0.00000000006  # Set a lower threshold, like 0.05

# Load the trained weights
model.load_state_dict(torch.load('fasterrcnn_model.pth'))

# Move model to the correct device (e.g., GPU or CPU)
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

# Set the model to evaluation mode
model.eval()
print(model.roi_heads.box_predictor.cls_score.weight)

# Test the model on an image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image you want to test
image_path = '../data/images/test_01.jpeg'
image = Image.open(image_path).convert("RGB")

# Preprocess the image (same as in training)
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

image_tensor = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device

# Perform inference
with torch.no_grad():
    prediction = model(image_tensor)

# Debug output
print("Prediction:", prediction)
if prediction:
    pred_boxes = prediction[0].get('boxes', [])
    pred_scores = prediction[0].get('scores', [])

    print("Predicted boxes:", pred_boxes)
    print("Predicted scores:", pred_scores)
else:
    print("No predictions were made.")
# Visualize the results
plt.imshow(np.array(image))
ax = plt.gca()

# Draw bounding boxes
for box in pred_boxes:
    x_min, y_min, x_max, y_max = box
    ax.add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                               fill=False, color='red', linewidth=1))

plt.show()
