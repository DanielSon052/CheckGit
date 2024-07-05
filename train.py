import torch
import argparse
import shutil
import os, sys
from pathlib import Path

if os.getcwd() + '/utils/model/' not in sys.path:
    sys.path.insert(1, os.getcwd() + '/utils/model/')
from utils.learning.train_part import train

if os.getcwd() + '/utils/common/' not in sys.path:
    sys.path.insert(1, os.getcwd() + '/utils/common/')
from utils.common.utils import seed_fix

#argparse를 사용하여 명령어 인자들을 파싱.
#파라미터: GPU 번호, 배치 크기, 에포크 수, 학습률, 보고 간격, 네트워크 이름 등 이건 테스트다
#하이퍼파라미터 : 캐스케이드 수, U-Net의 채널 수, 감도 맵의 채널 수 등

# train.sh: 모델 훈련을 실행하기 위한 쉘 스크립트

# python train.py: train.py 스크립트를 실행.
# -b 1: 배치 사이즈를 1로 설정.
# -e 5: 에포크 수를 5로 설정.
# -l 0.001: 학습률을 0.001로 설정.
# -r 10: 주기적으로 모델을 저장하는 간격을 10으로 설정.
# -n 'test_Varnet': 네트워크 이름을 'test_Varnet'으로 설정.
# -t '/home/Data/train/': 학습 데이터의 경로를 '/home/Data/train/'으로 설정.
# -v '/home/Data/val/': 검증 데이터의 경로를 '/home/Data/val/'으로 설정.

def parse():
    parser = argparse.ArgumentParser(description='Train Varnet on FastMRI challenge Images',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g', '--GPU-NUM', type=int, default=0, help='GPU number to allocate')
    parser.add_argument('-b', '--batch-size', type=int, default=1, help='Batch size')
    parser.add_argument('-e', '--num-epochs', type=int, default=1, help='Number of epochs')
    parser.add_argument('-l', '--lr', type=float, default=1e-3, help='Learning rate')
    parser.add_argument('-r', '--report-interval', type=int, default=500, help='Report interval')
    parser.add_argument('-n', '--net-name', type=Path, default='test_varnet', help='Name of network')
    parser.add_argument('-t', '--data-path-train', type=Path, default='/Data/train/', help='Directory of train data')
    parser.add_argument('-v', '--data-path-val', type=Path, default='/Data/val/', help='Directory of validation data')
    
    parser.add_argument('--cascade', type=int, default=1, help='Number of cascades | Should be less than 12') ## important hyperparameter
    parser.add_argument('--chans', type=int, default=9, help='Number of channels for cascade U-Net | 18 in original varnet') ## important hyperparameter
    parser.add_argument('--sens_chans', type=int, default=4, help='Number of channels for sensitivity map U-Net | 8 in original varnet') ## important hyperparameter
    parser.add_argument('--input-key', type=str, default='kspace', help='Name of input key')
    parser.add_argument('--target-key', type=str, default='image_label', help='Name of target key')
    parser.add_argument('--max-key', type=str, default='max', help='Name of max key in attributes')
    parser.add_argument('--seed', type=int, default=430, help='Fix random seed')

    args = parser.parse_args()
    return args

# 메인함수
if __name__ == '__main__':
    args = parse()
    
    # fix seed(재현 가능 보장)
    if args.seed is not None:
        seed_fix(args.seed)

    # 결과 저장 경로 설정
    args.exp_dir = '../result' / args.net_name / 'checkpoints'
    args.val_dir = '../result' / args.net_name / 'reconstructions_val'
    args.main_dir = '../result' / args.net_name / __file__
    args.val_loss_dir = '../result' / args.net_name

    args.exp_dir.mkdir(parents=True, exist_ok=True)
    args.val_dir.mkdir(parents=True, exist_ok=True)

    train(args) # in train_part.py

