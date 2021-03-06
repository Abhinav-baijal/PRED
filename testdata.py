import numpy

data = {
    1: {
        1: [1,2],
        2: [3,4],
        3: [5,6,7]
    },
    2: {
        4: [1,2,3],
        5: [4,5],
        6: [6,7]
    },
    3: {
        7: [1,3],
        8: [2,4,7],
        9: [5,6]
    }
}

affinitymatrix = [
    [3,2,2,0,0,0,0],
    [2,3,1,1,0,0,1],
    [2,1,3,1,0,0,0],
    [0,1,1,3,1,0,1],
    [0,0,0,1,3,2,1],
    [0,0,0,0,2,3,2],
    [0,1,0,1,1,2,3]
]

distancematrix = numpy.subtract(3, affinitymatrix)
