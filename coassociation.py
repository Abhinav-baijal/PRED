def convert_data(data):
    result={}

    for clustering,values in data.items():
        result[clustering]={}
        for k,v in values.items():
            for image in v:
                result [clustering][image]=k

    return result

def compute_distance_matrix(data):
    result = {}

    nb_clusters = len(data)

    for image in next(iter(data.values())):
        result[image] = {}
        for image2 in next(iter(data.values())):
            result[image][image2] = nb_clusters

    for a in result:
        for b in result[a]:
            for clustering in data.values():
                if clustering[a] == clustering[b]:
                    result[a][b] -= 1

    return result

def distance_matrix(data):
    return compute_distance_matrix(convert_data(data))


def constrain_together(matrix,image1,image2):
    matrix[image1][image2] =0
    matrix[image2][image1] =0

def constrain_appart(matrix, image1, image2):
    matrix[image1][image2] = float("inf")
    matrix[image2][image1] = float("inf")
