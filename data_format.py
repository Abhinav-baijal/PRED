def dict_to_matrix(d):
    result = []
    for k in sorted(d):
        subresult = []
        for k2 in sorted(d[k]):
            subresult.append(d[k][k2])
        result.append(subresult)
    return result
