import images

def dict_to_list(d):
    tmp_dict = {}
    for cluster,images in d.items():
        for image in images:
            tmp_dict[image] = cluster

    result = []
    for k in sorted(tmp_dict):
        result.append(tmp_dict[k])

    return result

def list_to_dict(l):
    result = {}
    for cluster in l:
        result[cluster] = []

    d = labels_as_dictionary(l)
    for image,cluster in d.items():
        result[cluster].append(image)

    return result

def dict_to_matrix(d):
    result = []
    for k in sorted(d):
        subresult = []
        for k2 in sorted(d[k]):
            subresult.append(d[k][k2])
        result.append(subresult)
    return result

def labels_as_dictionary(labels):
    return dict(zip(images.imageids, labels))
