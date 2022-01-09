import json, codecs
from glob import glob
from joblib import Parallel, delayed
import multiprocessing


DRESS_IIDS_PATH="../dataset/fashioniq/image_splits/*.dress.*.json"
TOPTEE_IIDS_PATH="../dataset/fashioniq/image_splits/*.toptee.*.json"
SHIRT_IIDS_PATH="../dataset/fashioniq/image_splits/*.shirt.*.json"
BROKEN_LINKS_PATHS="../dataset/fashioniq/broken_links.json"

PATHS=[DRESS_IIDS_PATH, TOPTEE_IIDS_PATH, SHIRT_IIDS_PATH]

def get_broken_data():
    broken_iids = None
    with open(BROKEN_LINKS_PATHS) as json_file:
        broken_iids = json.load(json_file)
    return broken_iids

def clean_iids_operator(path, broken_iids_set):
    """Clean the traint, val and test data"""
    paths = glob(path)
    for file in paths:
        #For each file (train,val,test)
        #Initialize an empty list of iids
        #l_iids=[]
        # Read the iids present in each file
        with open(file) as json_file:
            iids=json.load(json_file)
            #l_iids.append(iids)
        #Set of iids present in file
        iidsset=set(iids)
        print("# of iids: {}".format(len(iidsset)))
        #The correct iids list
        correctiids = list(iidsset-broken_iids_set)
        #Write to file the correct iids
        with open(file,'wb') as f:
            json.dump(correctiids, codecs.getwriter('utf-8')(f), ensure_ascii=False)
        count=len(correctiids)-len(iidsset)
        print("Cleaned iids of %s"%file)
        print("Removed {} broken iids".format(count))


def clean_parallel(num_cores, broken_iids):
    Parallel(n_jobs=num_cores)(
        delayed(clean_iids_operator)(
        path,
        broken_iids) for path in PATHS)

def clean(broken_iids):
    for path in PATHS:
        clean_iids_operator(path,broken_iids)



def run_main(num_executors):
    print("working on {} CPUs".format(num_executors))
    broken_iids= set(get_broken_data())
    #For each category fix the file by deletinf broken iids
    clean_parallel(num_executors, broken_iids)
    #clean(broken_iids)


if __name__ == '__main__':
    NUM_CORES= 6
    run_main(NUM_CORES)