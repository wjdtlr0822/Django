import os

i=2
path='C:/Users/wjdtl/Desktop/dasar_haartrain/dasar_haartrain/positive/rawdata/'
for filename in os.listdir(path):
    print(filename)
    os.rename(path+filename, path+'a'+str(i)+'.bmp')
    i+=1