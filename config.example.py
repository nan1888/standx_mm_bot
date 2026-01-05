"""
StandX MM Bot 설정 파일
사용법: config.py로 복사 후 수정
"""

# 모드 설정
MODE = "TEST"           # "TEST" = 시뮬레이션, "LIVE" = 실제 주문
EXCHANGE = "standx"
COIN = "BTC"

# 주문 설정
SPREAD_BPS = 8.0        # 주문 스프레드 (bps)
DRIFT_THRESHOLD = 3.0   # 재주문 트리거 (bps)
MIN_WAIT_SEC = 3.0      # 주문 변경 최소 대기 시간 (초)
REFRESH_INTERVAL = 0.05 # 화면 갱신 간격 (초)

# 수량 설정
SIZE_UNIT = 0.0001      # 주문 수량 단위 (BTC)
LEVERAGE = 6            # 레버리지 배수 (양방향이므로 실제 각 3배)
MAX_SIZE_BTC = 0.0002   # 최대 주문 수량 (None = 무제한)

# 안정성 설정
MAX_HISTORY = 1000              # 주문 히스토리 최대 보관 개수
MAX_CONSECUTIVE_ERRORS = 10     # 연속 에러 허용 횟수
