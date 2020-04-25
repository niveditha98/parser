import os
import extract
import pandas as pd
f=[]
for file in os.listdir("/"):
    if file.endswith(".pdf"):
        origpath=os.path.join("/", file)
        os.system('python pdf2imgpages.py '+file)
        for f in os.listdir('/'):
            l=[]
            if f.startswith(file):
                if f.endswith(".jpg"):
                    l.append(f)
        os.system('python detection.py '{}''.format(l))
        #give predicted results in csv format as input
        extract.cropimg(file+'.csv')
for file in os.listdir("/"):
    if file.startswith('cropped'):
        os.system('python toexcel.py '+file)
a=pd.read_csv('final.csv')
a.to_html('Final.htm')
