import numpy as np
import sys

def readParams(filename):
    lines = dict()
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    lines = [i.strip() for i in lines]
    params = lines[0].split(' ')
    num_cameras, num_points, num_observations = int(params[0]), int(params[1]), int(params[2])

    points_2d = np.zeros((num_observations,2))
    camera_indices = np.zeros(num_observations, dtype=np.int32)
    point_indices = np.zeros(num_observations, dtype=np.int32)

    for i in range(1, num_observations+1):
        a = lines[i].split(' ')
        a = [x for x in a if x]
        camera_indices[i-1] = int(a[0])
        point_indices[i-1] = int(a[1])
        x,y = float(a[2]), float(a[3])
        points_2d[i-1] = np.array([x,y])

    camera_k = num_cameras*9+1
    range_max = num_observations+camera_k+1

    temp = lines[num_observations+1:range_max-1]
    a = np.array(list(map(float, temp)))
    camera_params = np.reshape(a, (num_cameras, 9))

    temp = lines[range_max-1:]
    a = np.array(list(map(float, temp)))
    points_3d = np.reshape(a, (num_points, 3))

    return points_2d, points_3d, camera_indices, point_indices, camera_params

if __name__ == "__main__":
    filename = '../data/problem-21-11315-pre.txt'
    filename = '../data/problem-39-18060-pre.txt'
    filename = '../data/problem-50-20431-pre.txt'
    readParams(filename)