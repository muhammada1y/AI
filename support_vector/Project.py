
import numpy as np

def find_nearest_neighbors(dataSetOne,dataSetTwo,num):
    nearest_neighbors = []
    for points in dataSetOne:
        nearest_distance = np.sum(np.abs(points - dataSetTwo),axis=1)
        
        min_index = np.argmin(nearest_distance)
        nearest_neighbors.append((point1.tolist(), array2[min_index].tolist()))




array1 = [[1,2],[4,6]]
array2 = [[3.3],[5,5]]
num = 1

outPut = find_nearest_neighbors(array1,array2,num)

print(outPut)