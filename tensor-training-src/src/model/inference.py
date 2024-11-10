import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.models.detection as models

# Load the trained model
model = models.fasterrcnn_resnet50_fpn(pretrained=False)
model.load_state_dict(torch.load('model.pth'))
model.eval()  # Set the model to evaluation mode

# Load and preprocess the image
image = Image.open('data/images/test/sample_image.jpg').convert("RGB")
transform = transforms.Compose([transforms.ToTensor()])
image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

# Perform inference
with torch.no_grad():  # No need to compute gradients during inference
    prediction = model(image_tensor)

# Get bounding boxes, labels, and scores from prediction
boxes = prediction[0]['boxes']
labels = prediction[0]['labels']
scores = prediction[0]['scores']

# Print the predictions
print(f"Boxes: {boxes}")
print(f"Labels: {labels}")
print(f"Scores: {scores}")

# Visualize the results (draw bounding boxes on the image)
fig, ax = plt.subplots(1, figsize=(12,9))
ax.imshow(image)

# Draw bounding boxes
for box, label, score in zip(boxes, labels, scores):
    if score > 0.5:  # Consider only predictions with confidence > 50%
        xmin, ymin, xmax, ymax = box
        ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, color='red', linewidth=3))
        ax.text(xmin, ymin, f'{label.item()}: {score:.2f}', color='red', fontsize=12)

plt.show()
