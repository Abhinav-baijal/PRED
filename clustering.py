import data
import coassociation
import data_format
from sklearn import cluster
import image_utils
import quality

print("Computing distance matrix")

#calcuate the distance matrix.
#from distance_matrix import distance_matrix   # Uncomment to use cached values
distance_matrix = data_format.dict_to_matrix(coassociation.distance_matrix(data.data))   # Comment to use cached values

#to apply the agglomerative clustering.
def agglomerative_clustering(clusters, linkage_type='average'):
    agglomerative = cluster.AgglomerativeClustering(n_clusters = clusters,
                                                    affinity = 'precomputed',
                                                    linkage = linkage_type,
                                                    memory = '/tmp/sklearn-cache/')

    agglomerative.fit(distance_matrix)

    return data_format.list_to_dict(agglomerative.labels_.copy())

#to create the results, calls  the agglomerative clusterings funtions.
print("Building consensus clusterings")
results = {i:agglomerative_clustering(i) for i in range(1,len(distance_matrix)+1,10)}

#curve of quality, with respect to number of clusters in a clustering.
def cluster_number_quality_curve():
    qualities = {k:result_quality(v) for k,v in results.items()}
    import plot
    plot.bar_chart(list(qualities.keys()), list(qualities.values()))

#to display a specific cluster.
def display_cluster(result, cluster_id):
    image_utils.images_on_grid(image_utils.image_ids_to_paths(result[cluster_id])).show()

#to display the quality of the results.
def result_quality(result):
    return quality.consensus_quality(result, data.data)

#def original_clusterings_quality():                                                # Comment to use cached values
#    return [quality.consensus_quality(x, data.data) for x in data.data.values()]   # Comment to use cached values
def original_clusterings_quality():             # Uncomment to use cached values
    from quality_values import quality_values   # Uncomment to use cached values
    return quality_values                       # Uncomment to use cached values

#plots the graph of quality.
def graph_quality(result):
    import plot
    plot.consensus_quality_bar_chart(result_quality(result), original_clusterings_quality())
