def compute_distance_matrix(data):
    result = {}

    nb_clusters = max([set(clustering.values()) for clustering in data])

    for image in data.itervalues().next():
        result[image] = {}
        for image2 in data.itervalues().next():
            result[image2] = nb_clusters

    for a in result:
        for b in result[a]:
            for clustering in data.values():
                if clustering[a] == clustering[b]:
                    result[a][b] -= 1

    return result
