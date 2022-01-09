import subprocess
import json
from tqdm import tqdm

LINKS_PATH='../dataset/fashioniq/image_splits/links.txt'

broken=0
with open(LINKS_PATH) as f:
    lines = f.readlines()
    for line in lines:
        name, url = line.strip().split(' ')
        name, url = name.strip(), url.strip()
        dir_name = '../dataset/fashioniq/image_splits/%s'%name
        ret_code = subprocess.call(["wget", "-O", dir_name, url], stdout=subprocess.PIPE)
        if(ret_code!=0):
            broken=broken+1
        else:
            print("Succesfully downloaded from {}".format(url))