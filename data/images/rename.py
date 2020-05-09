import os
folder="F:\\object_Detection\\object_detection_demo\\data\\images\\test"

for root, dirs, files in os.walk(folder):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        newname = os.path.join(root, str(i) + ".jpg")
        os.rename(absname, newname)