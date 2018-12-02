import numpy as np

def AngleAxisRotatePoint(angle_axis, point):
    theta2 = np.dot(angle_axis, angle_axis)
    result = np.zeros((3))
    if theta2 > 1e-15:
        theta = np.sqrt(theta2)
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        theta_inverse = 1.0/theta

        w = np.multiply(angle_axis, theta_inverse)

        w_cross_pt = np.array([w[1]*point[2] - w[2]*point[1],
                               w[2]*point[0] - w[0]*point[2],
                               w[0]*point[1] - w[1]*point[0]])

        tmp = (w[0] * point[0] + w[1] * point[1] + w[2] * point[2]) * (1.0 - costheta)
        
        result[0] = point[0] * costheta + w_cross_pt[0] * sintheta + w[0] * tmp
        result[1] = point[1] * costheta + w_cross_pt[1] * sintheta + w[1] * tmp
        result[2] = point[2] * costheta + w_cross_pt[2] * sintheta + w[2] * tmp
    else:
        w_cross_pt = np.array([angle_axis[1] * point[2] - angle_axis[2] * point[1],
                              angle_axis[2] * point[0] - angle_axis[0] * point[2],
                              angle_axis[0] * point[1] - angle_axis[1] * point[0]])

        result[0] = point[0] + w_cross_pt[0]
        result[1] = point[1] + w_cross_pt[1]
        result[2] = point[2] + w_cross_pt[2]
    
    return result