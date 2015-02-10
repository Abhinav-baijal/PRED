#this script to change the format of the data which helps in faster calculation of the matrix. 
import images
#this function converts a dictionary we have as the inital data to a list. 
# this funtion translate the image's cluster number as a label for all the clustering,
# i.e. for a certain partition what is does is that it say that 
#example: 
#image 1 goes to the 10 cluster, image 2 goes to the 5 cluster and so on for all the 1002 images and sort them in accending order. So we have a lable list like 
# output for a single partition: 10 5 14 ....... and so on, which means that 1st image belong to 10 cluster, 2nd image to the 5th, 3rd image to 14 and so on..  
#it does this for all the partitions.
def dict_to_list(d):
    tmp_dict = {}
    for cluster,images in d.items():
        for image in images:
            tmp_dict[image] = cluster

    result = []
    for k in sorted(tmp_dict):
        result.append(tmp_dict[k])

    return result
#This funtion just does the inverse of the above function, converting the label into the number of cluster of the image.
def list_to_dict(l):
    result = {}
    for cluster in l:
        result[cluster] = []

    d = labels_as_dictionary(l)
    for image,cluster in d.items():
        result[cluster].append(image)

    return result
#Convert the data so that we do not have the ids, but the order is sorted. 
#It help to make a matrix with all the values in the dictionary. 
def dict_to_matrix(d):
    result = []
    for k in sorted(d):
        subresult = []
        for k2 in sorted(d[k]):
            subresult.append(d[k][k2])
        result.append(subresult)
    return result
#this functions add the labels to the images with the help of the image id. 
def labels_as_dictionary(labels):
    return dict(zip(images.imageids, labels))
