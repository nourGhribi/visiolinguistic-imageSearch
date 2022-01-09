import subprocess
import json
from tqdm import tqdm

txt_paths = ['../dataset/fashioniq/asin2url.dress.txt',
             '../dataset/fashioniq/asin2url.shirt.txt',
             '../dataset/fashioniq/asin2url.toptee.txt']

broken_links = []
BROKEN_LINKS_PATHS='../dataset/fashioniq/broken_links.json'

for t_p in txt_paths:
    with open(t_p) as f:
        lines = f.readlines()
    for line in lines:
        iid, url = line.strip().split('\t')
        iid, url = iid.strip(), url.strip()
        name = '../dataset/fashioniq/images/%s.jpg'%iid
        ret_code = subprocess.call(["wget", "-O", name, url], stdout=subprocess.PIPE)
        if(ret_code!=0):
            broken_links.append(iid)

with open(BROKEN_LINKS_PATHS, 'w') as outfile:
    json.dump(broken_links, outfile)
