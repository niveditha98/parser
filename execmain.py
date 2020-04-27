import os
import extract
import pandas as pd
f=[]
for file in os.listdir("C:/Users/Admin/AppData/Local/Programs/Python/Python36/Lib/site-packages/example/"):
    if file.endswith(".pdf"):
        origpath=os.path.join("C:/Users/Admin/AppData/Local/Programs/Python/Python36/Lib/site-packages/example/", file)
        os.system('python pdf2imgpages.py '+origpath)
        os.system('python detection.py '+file)
        #give predicted results in csv format as input
        extract.cropimg(origpath+'.csv')
for file in os.listdir("C:/Users/Admin/AppData/Local/Programs/Python/Python36/Lib/site-packages/example/"):
    if file.endswith('cropped.jpg'):
        os.system('python toexcel.py '+file)
a=pd.read_csv('final.csv')
a.to_html('Final.htm')
