import numpy as np

def calculate_distances(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)
    for array1set in array1:
        distances = np.sum(np.abs(array2 - array1set), axis=1)
        print(distances)
        print(f"Distances from {array1set} to points in array2: {distances}")
        
        minDistance = np.argmin(distances)
        print(f"Nearest neighbor to {array1set} is {array2[minDistance]} with a distance of {distances[minDistance]}\n")

array1 = [[1, 2], [4, 6]]
array2 = [[3, 3], [5, 5]]

calculate_distances(array1, array2)


