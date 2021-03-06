"""
	Dices Detection
	python version 2.7.13 or 3.6.x
	cv2(OpenCV) version 3.4.1
"""
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

#Function to load image
def loadImage(imgPath):
	img = cv2.imread(imgPath)
	return img

#GrayScale transform 
def trasform(img):
	grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return grayScale

def trasform2(img):
	BGR = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	return BGR;

#Kernel creator
def doKernel(bit, lenght):
	if(bit==0):
		kernel = np.zeros((lenght,lenght),np.uint8)
	else:
		kernel = np.ones((lenght,lenght),np.uint8)

#Show multiples images
def multipleView(images, titles):
	for i in range(len(titles)):
		plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
		plt.title(titles[i])
		plt.xticks([]),plt.yticks([])

	plt.show()

#Borders detection filters
	# gaussianBlur filter
def gaussianBlur(img):
	gaussianBlurM = cv2.GaussianBlur(img,(15,15),0)
	return gaussianBlurM

	# medianBlur filter
def medianBlur(img):
	medianBlurM = cv2.medianBlur(img,5)
	return medianBlurM

	# blur filter
def blur(img):
	blurM = cv2.blur(img,(10,10))
	return blurM

	#bilateral filter
def bilateral(img):
	bilateralM = cv2.bilateralFilter(img,9,75,75)
	return bilateralM

	#personalized filter
def personalized(img, kernel):
	dst = cv2.filter2D(img,-1,kernel)
	return dst

#Objects detection filters
	#Canny
def canny(img):
	cannyM = cv2.Canny(img,50,500)
	return cannyM

	#Laplacian
def laplacian(img):
	laplacianM = np.uint8(np.absolute(cv2.Laplacian(img, cv2.CV_64F)))
	return laplacianM

#Thresholding algorithms with Otsu's Binarization
def threshBinary(img):
	ret,threshed = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return threshed

def threshBynaryInv(img):
	ret,threshed = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	return threshed

#Thresholding adaptative algorithms	
def adaptativeMeanThresholding(img):
	threshed = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
		cv2.THRESH_BINARY,11,2)
	return threshed

def adaptativeMeanThresholdingInv(img):
	threshed = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
		cv2.THRESH_BINARY_INV,11,2)
	return threshed

def adaptativeGaussianThresholdingInv(img):	
	threshed = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		cv2.THRESH_BINARY_INV,11,2)
	return threshed

def adaptativeGaussianThresholding(img):	
	threshed = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		cv2.THRESH_BINARY,11,2)
	return threshed

#Morphological
def morphologyOpen(img, kernel):
	opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	return opened

def detectCircles(img):
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,38,
                            param1=200,param2=60,minRadius=3,maxRadius=50)
	return circles

#Filter for borders menu
def filter_menu(argument):
	switcher = {
		1: gaussianBlur,
		2: medianBlur,
		3: blur,
		4: bilateral,
		5: personalized
	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "Invalid option")
	# Execute the function
	return func

# #Filter for objects menu
def filter_menu2(argument):
	switcher = {
		1: canny,
		2: laplacian
	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "Invalid option")
	# Execute the function
	return func

#Threshholding algorithms menu
def thresh_menu(argument):
	switcher = {
		1: threshBynary,
		2: threshBynaryInv,
		3: adaptativeMeanThresholding,
		4: adaptativeGaussianThresholding
	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "Invalid option")
	# Execute the function
	return func