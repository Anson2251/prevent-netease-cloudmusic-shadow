#!/usr/bin/env python3

import time
import os

tools = ["xwininfo", "xdotool"]
dpiScale = 1.6 ## should be customized
maxMenuSize = [240, 350]
checkInterval = 5 # check interval in seconds


def isMenu(size): 
	# the shadow of the window of netease music consist four parts
	# each side has its own shadow window
	# the purpose of the condition is to filter out the windows that are too narrow (both horizontally and vertically).
	return not (int(size[0])/dpiScale < maxMenuSize[0]) ^ (int(size[1])/dpiScale < maxMenuSize[1])

def getShadowLikeWindowInfo():
	## all window satisfied (className contain "wechat"), (no window name), (has size)
	allWechatShadowLikeWindowInfo = os.popen('xwininfo -tree -root | grep "cloudmusic" | grep "(has no name)" | grep -v "1x1+0+0  +0+0"')
	allInfo = allWechatShadowLikeWindowInfo.readlines()
	shadowLikeWindowInfo = []; # id, size (width, height)
	for info in allInfo:
		info = info.strip() # remove the spaces in front of the info
		windowID = info.split(" ")[0] #id
		windowSize = info.split(" ")[-3].split("+")[0].split("x") # width, height
		if(not isMenu(windowSize)):
			shadowLikeWindowInfo.append([windowID, windowSize])
	return shadowLikeWindowInfo

# def printList(l):
# 	for i in l:
# 		print(i)

def printMessage(msg):
	print(f"[{time.strftime('%H:%M:%S')}] {msg}")

def isStarted():
	exist = os.popen('ps -ef | grep cloudmusic.exe | grep -v "grep" | grep -v "ps"') # ignore prcesses of ps and grep
	e = exist.readlines()
	# printList(e)
	return (len(e) > 0)

def checkEssentialToolsExist():
	for tool in tools:
		if(len(os.popen(f'whereis {tool}').read().strip().split(" ")) > 1):
			printMessage(f"'{tool}' exists")
		else:
			printMessage(f"'{tool}' does not exist")
			return False
	return True



printMessage("Checking essential tools...")
if(checkEssentialToolsExist()):
	printMessage("All essential tools exist")
else:
	printMessage("Some essential tools does not exist, please install them first")
	exit()


printMessage("Checking if netease cloud music is started...")
time.sleep(5) # wait for wechat to start


while True:
	if(not isStarted()):
		printMessage("netease cloud music has not been closed, stop preventing")
		exit()
	else:
		printMessage("netease cloud music has been started, preventing")

	shadowLikeWindowInfo = getShadowLikeWindowInfo()
	for info in shadowLikeWindowInfo:
		printMessage(f"Found shadow like window: {info[0]}, size: {info[1][0]}x{info[1][1]}")
		os.system(f"xdotool windowunmap {info[0]}")
	
	time.sleep(checkInterval)