import os
import os.path
from pathlib import Path
import json
from collections import OrderedDict

def read_json(fname):
    with fname.open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)


def write_json(content, fname):
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)

categories = {"dress":0,"shirt":1,"toptee":2}
data_types = ["train","val","test"]


train_data = []
test_data = []

for cat in categories.keys():
    # create new json file for this category
    for type in data_types:
        print("data_type",type)
        print(f"Reading file split.{cat}.{type}.json")
        file = read_json(Path(f"datasets/fashionIQ/image_splits/split.{cat}.{type}.json"))
        print("class:",categories[cat])
        data = [{"image_id": im_id, "class":categories[cat]} for im_id in file]
        if type == "test":
            test_data += data
        else:
            train_data += data

write_json(train_data, Path("datasets/fashionIQ/split_train.json"))

write_json(test_data, Path("datasets/fashionIQ/split_test.json"))
