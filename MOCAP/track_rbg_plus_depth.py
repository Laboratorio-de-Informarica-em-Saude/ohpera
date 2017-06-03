
import freenect
import cv2
import numpy as np


def get_video():
    """Get video in 8bit form kineck."""
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_8BIT)
    return array


def get_video_rgb():
    """Get video rgb from kineck."""
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


def add_depth(depth):
    """Add depth image to 8bit image."""
    balance = 2**10 - 1

    np.clip(depth, 0, balance, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth

if __name__ == "__main__":
    while 1:
        # get a 8bit frame from RGB camera
        frame = get_video()
        # display IR image
        frame = add_depth(frame)

        circles = cv2.HoughCircles(frame, cv2.cv.CV_HOUGH_GRADIENT, 1, 10)

        # get new frame from RGB camera
        # frame2 = get_video_rgb()

        if circles != None:
            print "Circle There !"

            for coordinates in circles:
                for coord in coordinates:
                    print coord
                    cv2.circle(frame, (coord[0], coord[1]), coord[2],
                        (0, 255, 0), 4)
                    # cv2.circle(frame2, (coord[0], coord[1]), coord[2],
                    #     (0, 255, 0), 4)

        cv2.imshow('RGB + Depth', frame)
        # cv2.imshow('RGB CIRCLES', frame2)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
