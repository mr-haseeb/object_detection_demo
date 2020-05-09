import os


mydir="F:\\object_Detection\\object_detection_demo\\data\\images\\train"
filelist = [ f for f in os.listdir(mydir) if f.endswith(".xml") ]
for f in filelist:
    os.remove(os.path.join(mydir, f))
