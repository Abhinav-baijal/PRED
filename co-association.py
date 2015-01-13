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

    nb_clusters = max([len(set(clustering.values())) for clustering in data.values()])

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
