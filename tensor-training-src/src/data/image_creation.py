from PIL import Image
import random
import json


class Minion:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.group = group

    def __str__(self):
        return f"Minion at ({self.x}, {self.y}) with color {self.group}"


def create_image(index):
    # Load the full map image and the overlay image
    map_image = Image.open("../image-generation/league_assets/background/map_full.jpg")

    # Define zoom level for the map and enlargement factor for the overlay
    zoom_factor = 6  # Zoom level for the map
    enlarge_factor = 2  # Scale factor to enlarge overlay_image

    # Calculate dimensions of the zoomed-in area
    zoom_width = map_image.width // zoom_factor
    zoom_height = map_image.height // zoom_factor

    # Randomly select a top-left corner for the zoomed area within bounds
    x = random.randint(0, map_image.width - zoom_width)
    y = random.randint(0, map_image.height - zoom_height)

    # Crop the zoomed area from the full map image
    zoomed_area = map_image.crop((x, y, x + zoom_width, y + zoom_height))

    # Resize the zoomed area to the original size (zoom effect)
    zoomed_area = zoomed_area.resize(map_image.size, Image.LANCZOS)
    minions = []
    # Enlarge the overlay image
    for i in range(0, 20):
        num_index = str(random.randint(1, 4))
        overlay_image = Image.open("../image-generation/league_assets/minion-blue/" + num_index + ".png")
        new_overlay_size = (int(overlay_image.width * enlarge_factor), int(overlay_image.height * enlarge_factor))
        enlarged_overlay = overlay_image.resize(new_overlay_size, Image.LANCZOS)

        # Randomly place the enlarged overlay image within the zoomed area
        overlay_x = random.randint(0, zoomed_area.width - enlarged_overlay.width)
        overlay_y = random.randint(0, zoomed_area.height - enlarged_overlay.height)

        # Create a new Minion object and add it to the list
        minions.append(Minion(overlay_x, overlay_y, 1))  # Assuming group '1' for all minions

        # Paste the enlarged overlay image onto the zoomed area
        zoomed_area.paste(enlarged_overlay, (overlay_x, overlay_y), enlarged_overlay)

    # Save the final image with overlay
    zoomed_area.save("images/train_" + str(index) + ".jpg")
    print(f"Zoomed snapshot saved as 'train_{index}.jpg'")
    save_json(index, minions)


def save_json(index, minions):
    # Load the existing JSON file (if it exists)
    file_path = "annotations/train.json"

    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Load existing data
    except FileNotFoundError:
        data = {"images": [], "annotations": []}  # Initialize structure if the file doesn't exist

    # Add the image data
    image_id = len(data["images"]) + 1
    data["images"].append({
        "id": image_id,
        "file_name": f"train_{index}.jpg"
    })

    # Add annotations for the minions
    for pos, item in enumerate(minions):
        data["annotations"].append({
            "image_id": image_id,
            "bbox": [item.x, item.y, item.x + 150, item.y + 150],  # Assuming fixed size for minions
            "category_id": 0,  # You can change this if you have multiple classes
            "area": 64 * 64,  # Area of the bounding box (assuming square minion size)
            "iscrowd": 0  # Set to 0 if not part of a crowd
        })

    # Save the updated JSON data
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Annotations for 'train_{index}.jpg' added to the JSON file.")


if __name__ == "__main__":
    for i in range(0, 30):
        create_image(i)
