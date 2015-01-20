from PIL import Image
import data
import images
import math

def image_ids_to_paths(ids):
    return ['images/' + images.images[id][1] for id in ids]

def images_on_grid(paths):
    thumbnail_size = 200
    count_x = math.ceil(math.sqrt(len(paths)))
    count_y = math.floor(math.sqrt(len(paths)))

    result = Image.new('RGB', (count_x*thumbnail_size,count_y*thumbnail_size))

    for i in range(len(paths)):
        x = i % count_x
        y = i // count_x

        image = Image.open(paths[i])
        image.thumbnail((thumbnail_size, thumbnail_size))
        result.paste(image, (x * thumbnail_size, y * thumbnail_size))

    return result
