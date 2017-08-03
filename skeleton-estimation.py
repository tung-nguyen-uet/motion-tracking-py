# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 07:32:15 2017

@author: tungnb
"""
import numpy as np
import time
import sys
import cv2 

def readVid(namevid):
    #objective:get frames from video
    #input:path of video
    #output:frames of video,frames per second,width of video,height of video
    vid = cv2.VideoCapture(namevid)
    num_f = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) #Number of frames
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    obj = []
    t = time.time() ###
    print ""  ###
    sys.stdout.write("reading video ... 0%") ###
    for i in range(num_f):
        ret, frame = vid.read()
        if ret == False:
            break
        obj.append(frame)
        if time.time()-t>1: ###
            a=np.ceil(i*100*1.0/(num_f-1)) ###
            b = ("reading video ... " + "%d"%a+"%") ###
            sys.stdout.write('\r'+b) ###
            t=time.time() ###
    sys.stdout.write('\r'+"reading video ... 100%") ### 
    print "" ###
    time.sleep(1) ###
    vid.release()
    return obj, fps, width, height

#Gen 14 different colors for 14 edges
def gen_colors():
	delta = 256/4;
	colors = []
	for i in range(0,4):
		for j in range(0,4):
			for k in range(0,4):
				colors.append((delta*i, delta*j, delta *k))
	return colors

#Read skeleton file
def readSkeleton(filename):
	ske = []
	f = open(filename, 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		one_ske = []
		for l in line.split(';'):
			x, y = [int(i) for i in l.split()]
			one_ske.append((x,y))
		#Maps Deepcut skeleton to hetpin's skeleton
		tmp = []
		tmp.append(one_ske[13])
		tmp.append(one_ske[12])
		tmp.append(one_ske[8])
		tmp.append(one_ske[9])
		tmp.append(one_ske[2])
		tmp.append(one_ske[3])
		tmp.append(one_ske[7])
		tmp.append(one_ske[6])
		tmp.append(one_ske[10])
		tmp.append(one_ske[11])
		tmp.append(one_ske[1])
		tmp.append(one_ske[0])
		tmp.append(one_ske[4])
		tmp.append(one_ske[5])
		ske.append(tmp)
	return ske

#Read lookup table
def readLookupTable(filename):
	table = []
	f = open(filename, 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		x, y = [int(i) for i in line.split(':')]
		#minus one, since python count from one for array index
		x = x -1
		y = y -1
		table.append((x,y))
	return table
        
#Draw skeleton
def draw_skeleton(inputframe, one_ske, table):
	draw_frame = inputframe.copy()
	i = 0	
	# compute the middle of the hip
	centerHipY = (one_ske[4][0]+one_ske[5][0])/2
	centerHipX = (one_ske[4][1]+one_ske[5][1])/2
	centerHip = (centerHipY, centerHipX)
	cv2.line(draw_frame, one_ske[1], centerHip, blue, thickness)

	for xy in table:
		cv2.line(draw_frame, one_ske[xy[0]], one_ske[xy[1]], colors[i], thickness)        
		#draw joints
		cv2.circle(draw_frame, one_ske[xy[0]], joint_r, green, 2)
		cv2.circle(draw_frame, one_ske[xy[1]], joint_r, green, 2)
		i = i + 1
	cv2.imshow('frame',draw_frame)	
	return draw_frame

def checkNearby(m, one_ske):# m, r, p stands for mouse, radius, point (joint)
	#print "Checking ", m
	r = 20
	k = 0 #for index of joint
	for p in one_ske:
		#print p , m
		if (abs(p[1]-m[1])<r) and (abs(p[0]-m[0])<r):
			print "Ok " , k
			return k
		k = k + 1
	return -1
#Drag function
moving = False
def click_and_drag(event, x, y, flags, param):
	global moving
	if event == cv2.EVENT_LBUTTONDOWN:
		#Check click nearby joint with radius of r pixcels
		if checkNearby((x,y), ske[i]) >= 0:
			moving = True
		else:
			moving = False
	if event == cv2.EVENT_MOUSEMOVE:
		if moving:
			#update moving joint
			k = checkNearby((x,y), ske[i])
			if k >= 0:
				ske[i][k] = (x,y)
			else:
				moving = False
			#draw
			draw_skeleton(obj[i-1], ske[i-1], table)
	if event == cv2.EVENT_LBUTTONUP:
		moving = False

#==================MAIN=========================
#MAIN LOOP
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',click_and_drag)
#------------------Skeleton-style---------------
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
thickness = 10
joint_r = 5
colors = gen_colors()
#------------------EndOfSkeletonStyle-----------
ske = readSkeleton("test2d.skeleton") # Read the stored skeleton
#Define skeleton lookup table
table = readLookupTable("lookup.skeleton")
obj, fps, width, height = readVid('D:/tungnb/Aniage/motion-tracking-py/dance.mp4')
numOfFrame = len(obj)
i = 1;
isPlay = False

try:
    while(i < numOfFrame):        
        draw_skeleton(obj[i], ske[i], table)
        isPlay = True
        i = i + 1
        k = cv2.waitKey(1000/fps) & 0xFF
        controller = cv2.waitKey(1) & 0xFF
        
        if controller == ord('q'):
            break
        if controller == ord('p'):
            print 'pause'
            isPlay = False
            cv2.waitKey(0)
except Exception,e: 
    print e
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
#==================END===========================