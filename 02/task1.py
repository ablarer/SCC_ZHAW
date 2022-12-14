import math

import numpy as np
import matplotlib.pyplot as plt
import unittest

from numpy.linalg import inv


# Task 1
def rotate_around_point(p, a, b, phi):
    # translate to center
    translate_to_center = np.array([[1, 0, -a], [0, 1, -b], [0, 0, 1]])
    # print('Center\n', center)

    # translate back to point in space
    to_point = inv(translate_to_center)
    # print('To point\n', to_point)

    # rotate around center
    rotation = np.array([[math.cos(phi), -math.sin(phi), 0], [math.sin(phi), math.cos(phi), 0], [0, 0, 1]])
    # print('Rotation\n', rotation)

    # translate around center -> rotate around center -> translate back to original point in space
    p_new = ((to_point @ rotation) @ translate_to_center) @ p
    # print('P new\n', p_new)

    return p_new


def rotate_tuple(p1, a, b, phi):

    p_new = [rotate_around_point(p1[0], a, b, phi),
             rotate_around_point(p1[1], a, b, phi),
             rotate_around_point(p1[2], a, b, phi),
             rotate_around_point(p1[3], a, b, phi),
             rotate_around_point(p1[4], a, b, phi)]
    return p_new


class TestRotateAroundPoint(unittest.TestCase):
    # Test cases for task 1.1
    def test_rotate_around_point(self):
        # Test case 1
        act1 = rotate_around_point(np.array([2., 5., 1.]), 6., 9., np.pi / 2.)
        exp1 = np.array([10., 5., 1.])
        test1 = act1 == exp1
        # Test case 2
        act2 = rotate_around_point(np.array([-2., 8., 1.]), 5., 7., np.pi)
        exp2 = np.array([12., 6., 1.])
        test2 = act2 == exp2
        # Test evaluation
        self.assertEqual(True, test1.all(), print(f'Test 1: act: {act1}, exp: {exp1}'))
        self.assertEqual(True, test2.all(), print(f'Test 2: act: {act2}, exp: {exp2}'))


if __name__ == '__main__':
    unittest.main()