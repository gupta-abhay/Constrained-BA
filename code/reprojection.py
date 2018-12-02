import numpy as np
from util import readParams
from rotation_utils import AngleAxisRotatePoint


def reprojection_err(camera, point_2d, point_3d):
    p = AngleAxisRotatePoint(camera, point_3d)

    #camera[3,4,5] are the translation.
    p[0] += camera[3]
    p[1] += camera[4]
    p[2] += camera[5]

    # Compute the center of distortion. The sign change comes from
    # the camera model that Noah Snavely's Bundler assumes, whereby
    # the camera coordinate system has a negative z axis.
    xp = - p[0] / p[2]
    yp = - p[1] / p[2]

    # Apply second and fourth order radial distortion.
    l1 = camera[7]
    l2 = camera[8]
    r2 = xp*xp + yp*yp
    distortion = 1.0 + r2  * (l1 + l2  * r2)


    # Compute final projected point position.
    focal = camera[6]
    predicted_x = focal * distortion * xp
    predicted_y = focal * distortion * yp

    # The error is the difference between the predicted and observed position.
    error = (predicted_x - point_2d[0]) ** 2 + (predicted_y - point_2d[1]) ** 2
    return error


def compute_total_error(points_2d, points_3d, camera_indices, point_indices, camera_params):
    reproj_error = 0.0
    
    for i in range(init_point_indices.shape[0]):
        point_2d = init_points_2d[i, :]
        point_3d = init_points_3d[init_point_indices[i], :]
        camera = init_camera_params[init_camera_indices[i], :]
        err = reprojection_err(camera, point_2d, point_3d)
        reproj_error += err

    return reproj_error


if __name__ == "__main__":
    initial_values = "../data/problem-21-11315-pre.txt"
    final_values = "../results_ceres/final_21.txt"
    
    init_points_2d, init_points_3d, init_camera_indices, init_point_indices, init_camera_params = readParams(initial_values)
    # final_points_2d, final_points_3d, final_camera_indices, final_point_indices, final_camera_params = readParams(final_values)
    init_reproj_error = compute_total_error(init_points_2d,
                                            init_points_3d,
                                            init_camera_indices,
                                            init_point_indices,
                                            init_camera_params)
    
    print(init_reproj_error)
    # print(init_points_2d.shape)
    # print(init_points_3d.shape)
    # print(init_camera_indices.shape)
    # print(init_point_indices.shape)
    # print(init_camera_params.shape)