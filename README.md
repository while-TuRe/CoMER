<div align="center">    
 
# CoMER: Modeling Coverage for Transformer-based Handwritten Mathematical Expression Recognition  
 
[![arXiv](https://img.shields.io/badge/arXiv-2207.04410-b31b1b.svg)](https://arxiv.org/abs/2207.04410)

</div>

## Project structure
```bash
├── README.md
├── comer               # model definition folder
├── convert2symLG       # official tool to convert latex to symLG format
├── lgeval              # official tool to compare symLGs in two folder
├── config.yaml         # config for CoMER hyperparameter
├── data.zip
├── eval_all.sh         # script to evaluate model on all CROHME test sets
├── example
│   ├── UN19_1041_em_595.bmp
│   └── example.ipynb   # HMER demo
├── lightning_logs      # training logs
│   └── version_0
│       ├── checkpoints
│       │   └── epoch=151-step=57151-val_ExpRate=0.6365.ckpt
│       ├── config.yaml
│       └── hparams.yaml
├── requirements.txt
├── scripts             # evaluation scripts
├── setup.cfg
├── setup.py
└── train.py
```

## Install dependencies   
```bash
cd CoMER
# install project   
conda create -y -n CoMER python=3.7
conda activate CoMER
conda install pytorch=1.8.1 torchvision=0.2.2 cudatoolkit=11.1 pillow=8.4.0 -c pytorch -c nvidia
# training dependency
conda install pytorch-lightning=1.4.9 torchmetrics=0.6.0 -c conda-forge
# evaluating dependency
conda install pandoc=1.19.2.1 -c conda-forge
pip install -e .
 ```

## Training
Next, navigate to CoMER folder and run `train.py`. It may take **7~8** hours on **4** NVIDIA 2080Ti gpus using ddp.
```bash
# train CoMER(Fusion) model using 4 gpus and ddp
python train.py --config config.yaml  
```

You may change the `config.yaml` file to train different models
```yaml
# train BTTR(baseline) model
cross_coverage: false
self_coverage: false

# train CoMER(Self) model
cross_coverage: false
self_coverage: true

# train CoMER(Cross) model
cross_coverage: true
self_coverage: false

# train CoMER(Fusion) model
cross_coverage: true
self_coverage: true
```

For single gpu user, you may change the `config.yaml` file to
```yaml
gpus: 1
# gpus: 4
# accelerator: ddp
```

## Evaluation
config environment:
https://zhuanlan.zhihu.com/p/161728028
```
wget -O- http://cpanmin.us | perl - -l ~/perl5 App::cpanminus local::lib
eval `perl -I ~/perl5/lib/perl5 -Mlocal::lib`
echo 'eval `perl -I ~/perl5/lib/perl5 -Mlocal::lib`' >> ~/.bashrc
echo 'export MANPATH=$HOME/perl5/man:$MANPATH' >> ~/.bashrc
source ~/.bashrc

cpan XML::LibXML
```


Metrics used in validation during the training process is not accurate.

For accurate metrics reported in the paper, please use tools officially provided by CROHME 2019 oganizer:

A trained CoMER(Fusion) weight checkpoint has been saved in `lightning_logs/version_0`



```bash
perl --version  # make sure you have installed perl 5

unzip -q data.zip

# evaluation
# evaluate model in lightning_logs/version_0 on all CROHME test sets
# results will be printed in the screen and saved to lightning_logs/version_0 folder
bash eval_all.sh 0
```
nohup ./start.sh >output.filename 2>&1 &

## how to see data logged in model
https://blog.csdn.net/weixin_44933805/article/details/118998102
the data is in lightning_logs/version_1/events.out.tfevents.1680700550.user-virtual-machine.3007347.0
```
pip install tensorboard
tensorboard --logdir=<存放tensorboard文件的文件夹名字>
```
