import os
x = 1
#os.chdir("C:/Users/Hisham/Desktop/Pictures_original - Copy")
camera_roll = "C:/Users/Hisham/Desktop/Pictures_original - Copy"
os.chdir(camera_roll)


#all files named 
for filename in os.listdir('.'):
    

    #if filename.startswith('20190408'):
     #   os.rename(filename,'Italy_'+filename)
        
    if filename.startswith('20190701'):
        os.rename(filename,'2018-02-04'+str(x))
        x+=1
