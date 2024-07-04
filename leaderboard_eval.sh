# leaderboard_eval.sh: 리더보드 평가를 실행하기 위한 쉘 스크립트

# python leaderboard_eval.py: leaderboard_eval.py 스크립트를 실행합니다.
# -lp '/home/Data/leaderboard': 리더보드 데이터 경로를 '/home/Data/leaderboard'로 설정합니다.
# -yp '/root/result/test_Varnet/reconstructions_leaderboard': 테스트 결과가 저장된 경로를 '/root/result/test_Varnet/reconstructions_leaderboard'로 설정합니다.

python leaderboard_eval.py \
  -lp '/home/Data/leaderboard' \
  -yp '/root/result/test_Varnet/reconstructions_leaderboard'
