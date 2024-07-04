python train.py \
  -b 1 \
  -e 5 \
  -l 0.001 \
  -r 10 \
  -n 'test_Varnet' \
  -t '/home/Data/train/' \
  -v '/home/Data/val/'
  
# train.sh: 모델 훈련을 실행하기 위한 쉘 스크립트

# python train.py: train.py 스크립트를 실행.
# -b 1: 배치 사이즈를 1로 설정.
# -e 5: 에포크 수를 5로 설정.
# -l 0.001: 학습률을 0.001로 설정.
# -r 10: 주기적으로 모델을 저장하는 간격을 10으로 설정.
# -n 'test_Varnet': 네트워크 이름을 'test_Varnet'으로 설정.
# -t '/home/Data/train/': 학습 데이터의 경로를 '/home/Data/train/'으로 설정.
# -v '/home/Data/val/': 검증 데이터의 경로를 '/home/Data/val/'으로 설정.
