model_name = "embedding"
weight = "./results/fashionIQ/moco/checkpoint_final.pth.tar"
model_type = "clusterresnet"
device = 0
num_cluster = 3
batch_size = 1000
world_size = 1
workers = 4
rank = 0
dist_url = 'tcp://localhost:10001'
dist_backend = "nccl"
seed = None
gpu = None
multiprocessing_distributed = True

data_test = dict(
    type="fashionIQ",
    root_folder="./datasets/fashionIQ",
    all=True,
    split="train+test",
    shuffle=True,
    ims_per_batch=50,
    aspect_ratio_grouping=False,
    train=False,
    embedding=None,
    show=False,
    trans1=dict(
        aug_type="test",
        normalize=dict(mean=[0.485, 0.456, 0.406],
                       std=[0.229, 0.224, 0.225]),
    ),
    trans2=dict(
        aug_type="test",
        normalize=dict(mean=[0.485, 0.456, 0.406],
                       std=[0.229, 0.224, 0.225]),
    ),

)


model_sim = dict(
    type=model_type,
    num_classes=128, #To Change?
    in_channels=3,
    in_size=96,
    batchnorm_track=True,
    test=False,
    feature_only=True,
    pretrained=weight,
    model_type="moco_sim_feature",
)


results = dict(
    output_dir="./results/fashionIQ/{}".format(model_name),
)