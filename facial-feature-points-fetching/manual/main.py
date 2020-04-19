import cv2
import numpy as np

img = cv2.imread('cheetah.jpg')
click_cnt = 0

def draw_rectangle(event, x, y, flags, param): #mouse callback function
    global click_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_cnt == 0:
            f=open('cheetah_points.txt', "w")
            f.write(str(x) + ' ' + str(y) + '\n')
            f.close()
        else:
            f=open('cheetah_points.txt', "a")
            f.write(str(x) + ' ' + str(y) + '\n')
            f.close()
        print(click_cnt)
        click_cnt = click_cnt + 1
        cv2.rectangle(img, (x-1,y-1), (x+1,y+1), (0,0,255), 2)
        cv2.imshow('frame', img)

if __name__ == "__main__":
    
    cv2.namedWindow(winname='frame')
    cv2.setMouseCallback('frame', draw_rectangle)
    cv2.imshow('frame', img)
    cv2.waitKey(0)

'''
1 1
254 1
254 188
1 188
127 1
254 94
127 188
1 94
'''

