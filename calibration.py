import numpy as np
import cv2
import matplotlib.image as mpimg
import glob


images = glob.glob('camera_cal/calibration*.jpg')


objpoints = []
imgpoints = []


def calib():
    objp = np.zeros((6 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    for fname in images:

        img = mpimg.imread(fname)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

        if ret == True:
            imgpoints.append(corners)
            objpoints.append(objp)
        else:
            continue

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], None, None)

    return mtx, dist


def undistort(img, mtx, dist):
    return cv2.undistort(img, mtx, dist, None, mtx)
