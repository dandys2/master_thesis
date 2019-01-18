import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import cv2
import numpy as np
import keras.backend as Kb

ITOP_bone_list = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [1, 8], [8, 9], [8, 10], [9, 11], [10, 12],
                  [11, 13], [12, 14]]


def visualize_pose_2D(img_coords, pause=True):  # image coords (J, 2), number of joints in skeleton
    fig, ax = plt.subplots(1, figsize=(3, 8))
    plt.title('Visualized skeleton pose')
    # plt.xlim(100, 200)
    # plt.ylim(-250, 0)
    # skeleton = movement[i * num_joints:(i + 1) * num_joints]

    if img_coords.shape[1] == 3:
        img_coords = Kb.eval(img_coords)
        y = img_coords[:, 1]
    else:
        y = -img_coords[:, 1]

    x = img_coords[:, 0]

    sc = ax.scatter(x, y, s=40)

    # connecting lines:
    if img_coords.shape[0] == 15:  # ITOP dataset
        for bone in ITOP_bone_list:
            ax.plot([x[bone[0]], x[bone[1]]], [y[bone[0]], y[bone[1]]], 'r')

    plt.show()
    if pause:
        plt.pause(0.001)
        input("Press [enter] to show next pose.")


def visualize_pose_3D(coords, pause=True):  # coords with shape (3, J)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = Kb.eval(coords[0])
    y = Kb.eval(coords[1])
    z = Kb.eval(coords[2])

    ax.scatter(x, z, y, c='r', marker='o')
    ax.set_xlabel('x axis')
    ax.set_ylabel('z axis')
    ax.set_zlabel('y axis')

    plt.xlim(-1, 1)
    ax.set_zlim3d(-1.25, 0.75)
    plt.ylim(-1, 1)

    # connecting lines:
    if coords.shape[1] == 15:  # ITOP dataset
        for bone in ITOP_bone_list:
            ax.plot([x[bone[0]], x[bone[1]]], [z[bone[0]], z[bone[1]]], [y[bone[0]], y[bone[1]]], 'r')

    plt.show()
    if pause:
        plt.pause(0.001)
        input("Press [enter] to show next pose.")
