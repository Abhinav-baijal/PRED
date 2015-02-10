#this script calculate the distance matrix in between the different images. 
import sys
#convert the data and return the results. It changes a tree structure to an array structure. Helps in faster calculation of distance matrix. 
def convert_data(data):
    result={}
    for clustering,values in data.items():
        result[clustering]={}
        for k,v in values.items():
            for image in v:
                result [clustering][image]=k

    return result
#computation of the distance matrix, in which the intial value of the matrix is set to the total number of clustering.
#each time an image appears to be in the same cluster in different clustering algorithms. The value of that cell in the matrix is reduced by 1 in the co-association matrix.
#the smaller the distance in the matrix, the higher is the similarity.
 
def compute_distance_matrix(data):
    result = {}

    nb_clustering = len(data)

    for image in next(iter(data.values())):
        result[image] = {}
        for image2 in next(iter(data.values())):
            result[image][image2] = nb_clustering

    for a in result:
        for b in result[a]:
            for clustering in data.values():
                if clustering[a] == clustering[b]:
                    result[a][b] -= 1

    return result

#This function returns the computed distance matrix. 
def distance_matrix(data):
    return compute_distance_matrix(convert_data(data))

#For applying the "must-link" constrains in the distance matrix. 
def constrain_together(matrix,image1,image2):
    matrix[image1][image2] =-sys.maxsize
    matrix[image2][image1] =-sys.maxsize
   
#For applying the "cannot-link" constrains in the distance matrix.     
def constrain_apart(matrix, image1, image2):
    matrix[image1][image2] = sys.maxsize
    matrix[image2][image1] = sys.maxsize
