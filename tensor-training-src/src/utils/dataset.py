import torch
from torch.utils.data import Dataset
from PIL import Image
import json
import os


class CustomObjectDetectionDataset(Dataset):
    def __init__(self, image_dir, annotation_file, transform=None):
        self.image_dir = image_dir
        self.annotation_file = annotation_file
        self.transform = transform
        with open(annotation_file) as f:
            self.annotations = json.load(f)

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        img_info = self.annotations[idx]
        img = Image.open(os.path.join(self.image_dir, img_info['image_id'])).convert("RGB")
        boxes = torch.tensor(img_info['boxes'], dtype=torch.float32)
        labels = torch.tensor(img_info['labels'], dtype=torch.int64)

        target = {'boxes': boxes, 'labels': labels}

        if self.transform:
            img = self.transform(img)

        return img, target
