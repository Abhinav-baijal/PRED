import images

def image_ids_to_paths(ids):
    return ['images/' + images.images[id][1] for id in ids]
