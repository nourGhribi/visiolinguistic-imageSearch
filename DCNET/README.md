# Interactive Image Retrieval: Dual Composition Network (DCNet)

This directory hosts the code of the paper Dual Compositional Learning in Interactive Image Retrieval.
In addition, the experiments directory holds all the experiments done base on this solution.

- [Jongseok Kim](https://ozmig77.github.io/), [Youngjae Yu](https://yj-yu.github.io/home), Hoeseong Kim and [Gunhee Kim](http://vision.snu.ac.kr/gunhee/).
Dual Compositional Learning in Interactive Image Retrieval. In *AAAI*, 2021.

```bibtex
@inproceedings{kim:2021:AAAI,
    title="{Dual Compositional Learning in Interactive Image Retrieval}",
    author={Kim, Jongseok and Yu, Youngjae and Kim, Hoeseong and Kim, Gunhee},
    booktitle={AAAI},
    year=2021
}
```

The project is an Winning Solution in [FashionIQ 2020](https://sites.google.com/view/cvcreative2020/fashion-iq).

## Getting Started

### Datasets
- Download Fashion-IQ dataset images from [here](https://github.com/hongwang600/fashion-iq-metadata). Save it under ./dataset/fashioniq/images/   
(May use `preprocess/download_fashioniq.py` for downloading images.)

- Download Fashion-IQ dataset annotations from [here](https://github.com/XiaoxiaoGuo/fashion-iq). Save it under ./dataset/fashioniq/
(Files under folder `captions` and `image_splits`)                                                                                                

### Preprocessing
Below code resize images and create glove embedded caption files.
```
cd preprocess
python -m nltk.downloader 'punkt'
python -m spacy download en_vectors_web_lg
python process_cap.py
python resize_img.py
```


## How to Run the code

### Evaluation on FashionIQ
For evaluation, first download checkpoint and config.json file from [Fashion IQ](https://drive.google.com/drive/folders/1wgygqF095Di67EaHaGOXbwh3wEzk9izB?usp=sharing) under `./logdir/fashioniq_dcnet`.
Then run below,
```
python test.py --resume logdir/fashioniq_dcnet/
```
### Training
For training run below,
```
python train.py --config configs/ce/fashioniq_dcnet.json --logdir fashioniq
```
You can change json file for other settings.

### Experiments
For qualitative result and attention plot for text expert, refer to
```
./experiments/result.ipynb
./experiments/textatt.ipynb
```
