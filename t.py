import time
import datetime
import urllib.request, urllib.parse, urllib.error
import cv2
import numpy as np
import glob
import os

def function_take_pictures(elapse_minutes, sleep_seconds):

  t_end = time.time() + 60 * elapse_minutes
  counter = 100000
  while time.time() < t_end:

    img = urllib.request.urlopen('http://192.168.1.122/snap.jpeg').read()
    fhand = open('/home/kyle/test1/snap%s.jpg' % counter, 'wb')
    fhand.write(img)
    fhand.close()
    print(counter)
    time.sleep(sleep_seconds)
    counter = counter + 1


def function_make_video():
  frameSize = (1920, 1080)
  filename = f"output_video-{datetime.datetime.now():%Y-%m-%d-%H-%M-%S}.mp4"
  out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'mp4v'), 24, frameSize)
  vid_capture = cv2.VideoCapture('/home/kyle/test1/snap1%05d.jpg')

  while(vid_capture.isOpened()):
      # vid_capture.read() methods returns a tuple, first element is a bool
      # and the second is frame
      ret, frame = vid_capture.read()
      if ret == True:
           # Write the frame to the output files
           out.write(frame)
      else:
          print("Stream disconnected")
          break




def delete_snap_files():
  files = glob.glob('*jpg')
  for filename in files:
    os.remove(filename)

#function_take_pictures (180, 10)
function_make_video()
#delete_snap_files()

