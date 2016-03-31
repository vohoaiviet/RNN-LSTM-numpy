#coding: utf8
import tensorflow as tf
import numpy as np
import math
import cv2
import sys
import os
from scipy import ndimage
import random

training_index = './training_index.txt'
newlabel_index ='./newlabel_index.txt'


def read_traing_list():
	train_image_dir = []
	train_label_dir = []
	reader = open(training_index)
	while 1:
		line = reader.readline()
		tmp = line.split(" ")
		# print tmp
		if not line:
			break
		train_image_dir.append(tmp[0])
		train_label_dir.append(tmp[1][0:-1])
	print train_image_dir[1:10]
	print train_label_dir[1:10]
	reader.close()
	return train_image_dir, train_label_dir

def distort_image():
	train_image_dir, train_label_dir = read_traing_list()

	label_reader = open(newlabel_index,"w")

	for idx in range(len(train_image_dir)):
		image_path = str(train_image_dir[idx])
		image_tmp = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
		rotate_image = ndimage.rotate(image_tmp,random.randint(7,30))
		rotate_image = cv2.resize(rotate_image,(28,28))
		rotate_image_path = image_path[:-4]+"_1.png"
		print rotate_image_path
		cv2.imwrite(rotate_image_path,rotate_image)

		rotate_image2 = ndimage.rotate(image_tmp,random.randint(330,355))
		rotate_image2 = cv2.resize(rotate_image2,(28,28))
		rotate_image_path2 = image_path[:-4]+"_2.png"
		cv2.imwrite(rotate_image_path2,rotate_image2)
		label_reader.write(rotate_image_path+" "+str(train_label_dir[idx])+"\n")
		label_reader.write(rotate_image_path2+" "+str(train_label_dir[idx])+"\n")

	label_reader.close()
	print "done"

distort_image()



