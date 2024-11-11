import torch
from torch.utils.data import Dataset
from PIL import Image
import json
import os
from torch.utils.data import Dataset
import os
from PIL import Image
import json


class CustomObjectDetectionDataset(Dataset):
    def __init__(self, image_dir, annotation_file, transform=None):
        self.image_dir = image_dir
        self.annotation_file = annotation_file
        self.transform = transform
        self.images = []  # List to store image file names or paths
        self.annotations = []  # List to store annotations

        # Load annotation data from the JSON file
        with open(annotation_file) as f:
            data = json.load(f)
            for img_info in data["images"]:
                self.images.append(img_info["file_name"])
                # Assuming annotations are available for each image
                image_annotations = [anno for anno in data["annotations"] if anno["image_id"] == img_info["id"]]
                self.annotations.append(image_annotations)

    def __len__(self):
        # The length of the dataset is the number of images
        return len(self.images)

    def __getitem__(self, idx):
        # Get the image path
        image_path = os.path.join(self.image_dir, self.images[idx])
        image = Image.open(image_path).convert("RGB")  # Open the image file

        # Get the annotations for this image
        target = self.annotations[idx]
        boxes = []
        labels = []

        for ann in target:
            # Each annotation should have a 'bbox' (bounding box) and 'category_id' (class label)
            boxes.append(ann['bbox'])
            labels.append(ann['category_id'])

        # Convert lists to tensors
        boxes = torch.tensor(boxes, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.int64)

        # Create target dictionary
        target = {"boxes": boxes, "labels": labels}

        if self.transform:
            image = self.transform(image)

        return image, target
