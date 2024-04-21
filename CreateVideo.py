import os
import cv2

path = "Images/"

Images = []

for file in os.listdir(path):
    name, ext = os.splitext(file)

if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path + "/" + file

    print(file_name)
    file.append(Images)
     
    count = len(Images)

frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX', 0.8, size))

for i in range(0, count - 1):
    cv2.imread(Images[0])
    out.write(frame)

out.release()
print("Done")