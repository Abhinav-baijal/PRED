import data as testdata
import images
import coassociation
from PIL import Image
from sklearn import cluster

agglomerative = cluster.AgglomerativeClustering(n_clusters = 100,
                                                affinity = 'precomputed',
                                                linkage = 'average')

distancematrix = coassociation.dict_to_matrix(coassociation.distance_matrix(testdata.data))
agglomerative.fit(distancematrix)

result = dict(zip(images.imageids, agglomerative.labels_))

filenames = ['images/' + images.images[image][1] for image,cluster in result.items() if cluster == 1]
for f in filenames:
    Image.open(f).show()
