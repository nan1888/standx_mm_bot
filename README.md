# StandX Market Making Bot

StandX 무기한 선물 거래소에서 자동으로 마켓메이킹을 수행하는 봇입니다.

---

## 면책조항 (Disclaimer)

> **경고: 이 소프트웨어는 있는 그대로(AS-IS) 제공되며, 어떠한 보증도 하지 않습니다.**
>
> - 이 봇을 사용하여 발생하는 **모든 손실에 대한 책임은 전적으로 사용자에게 있습니다.**
> - 이 소프트웨어는 **투자 조언이 아닙니다.** 재정적 결정은 본인의 판단 하에 내려야 합니다.
> - 암호화폐 거래는 **원금 손실 위험**이 있으며, 레버리지 거래는 손실을 증폭시킬 수 있습니다.
> - 개발자는 버그, 거래소 장애, 네트워크 문제 등으로 인한 **예기치 않은 동작에 대해 책임지지 않습니다.**
> - 반드시 **잃어도 되는 금액**으로만 거래하세요.
>
> 이 소프트웨어를 사용함으로써 위 조건에 동의한 것으로 간주됩니다.

---

## 빠른 시작 (처음 사용자용)

### 1단계: 파이썬 설치 확인

터미널(명령 프롬프트)을 열고 아래 명령어를 입력하세요:

```bash
python --version
```

`Python 3.10.x` 같은 결과가 나와야 합니다. 안 나오면 Python 3.10을 먼저 설치하세요.

### 2단계: 의존성 설치

프로젝트 폴더로 이동한 후:

```bash
pip install -r requirements.in
```

### 3단계: 지갑 설정 파일 만들기

`.env.example` 파일을 복사해서 `.env` 파일을 만듭니다.

**Windows:**
```bash
copy .env.example .env
```

**Mac/Linux:**
```bash
cp .env.example .env
```

그 다음 `.env` 파일을 메모장이나 편집기로 열어서 수정합니다:

```
WALLET_ADDRESS=0x여기에_지갑_주소_입력
PRIVATE_KEY=여기에_개인키_입력
```

**예시:**
```
WALLET_ADDRESS=0x1234567890abcdef1234567890abcdef12345678
PRIVATE_KEY=abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

> **참고**: `PRIVATE_KEY`는 생략 가능합니다. 생략하면 실행 시 브라우저 로그인 창이 열립니다.

### 4단계: 봇 설정 파일 만들기

`config.example.py` 파일을 복사해서 `config.py` 파일을 만듭니다.

**Windows:**
```bash
copy config.example.py config.py
```

**Mac/Linux:**
```bash
cp config.example.py config.py
```

그 다음 `config.py` 파일을 편집기로 열어서 원하는 대로 수정합니다. (아래 "설정 파라미터" 섹션 참고)

### 5단계: 실행

```bash
python main.py
```

처음에는 `MODE = "TEST"`로 시뮬레이션 모드에서 테스트해보세요!

---

## 설정 파라미터 (config.py)

`config.py` 파일을 열면 아래 설정들이 있습니다:

### 기본 설정

| 설정 | 예시 | 설명 |
|------|------|------|
| `MODE` | `"TEST"` | **중요!** `"TEST"` = 시뮬레이션(돈 안 씀), `"LIVE"` = 실제 주문 |
| `EXCHANGE` | `"standx"` | 거래소 이름 (바꾸지 마세요) |
| `COIN` | `"BTC"` | 거래할 코인 |

### 주문 설정

| 설정 | 기본값 | 설명 |
|------|--------|------|
| `SPREAD_BPS` | `8.0` | 주문 스프레드. 8 = 현재가에서 ±0.08% 위치에 주문 |
| `DRIFT_THRESHOLD` | `3.0` | 가격이 3bps(0.03%) 이상 움직이면 주문 재배치 |
| `MIN_WAIT_SEC` | `3.0` | 주문 재배치 최소 대기 시간 (초) |
| `REFRESH_INTERVAL` | `0.05` | 화면 갱신 주기 (초). 0.05 = 초당 20회 |

### 수량 설정

| 설정 | 기본값 | 설명 |
|------|--------|------|
| `SIZE_UNIT` | `0.0001` | 주문 수량 단위. BTC 기준 0.0001 = 약 $10 |
| `LEVERAGE` | `6` | 레버리지 배수. 6배 = 양방향 각 3배씩 |
| `MAX_SIZE_BTC` | `0.0002` | 최대 주문 수량. `None`으로 설정하면 제한 없음, 에드작 생각하면 1BTC가 최대 |

### 안정성 설정

| 설정 | 기본값 | 설명 |
|------|--------|------|
| `MAX_HISTORY` | `1000` | 히스토리 최대 보관 개수 (메모리 관리용) |
| `MAX_CONSECUTIVE_ERRORS` | `10` | 연속 에러 10회 시 봇 종료 |

### 포지션 자동 청산

| 설정 | 기본값 | 설명 |
|------|--------|------|
| `AUTO_CLOSE_POSITION` | `True` | 포지션 생기면 자동 청산 후 MM 재개 |

> **동작 방식**: MM 호가가 체결되어 포지션이 생기면 → 모든 주문 취소 → 포지션 청산(시장가) → MM 재개
>
> `False`로 설정하면 포지션을 유지한 채 MM을 계속합니다.

### 포지션 로그 기록

포지션이 감지되고 청산될 때마다 `position_log.txt` 파일에 자동으로 기록됩니다.

**로그 예시:**
```
2026-01-06 14:30:15 | POSITION DETECTED | LONG 0.000100 BTC @ 97500.00 | uPnL: $+1.25
2026-01-06 14:30:16 | POSITION CLOSED  | LONG 0.000100 BTC | PnL: $+1.25 | Total: 1 closes, 0.000100 BTC, $+1.25
```

**대시보드 통계:**
```
Placed: 125  Cancelled: 120  Rebalanced: 45  Closes: 3 (0.0003 BTC, $+5.50)
```

> **주의**: 기록되는 PnL은 청산 직전의 미실현 손익(unrealized PnL)입니다. 시장가로 청산하기 때문에 슬리피지가 발생할 수 있어 **실제 실현 손익과 약간 차이**가 날 수 있습니다.

---

## 설정 예시

### 안전하게 테스트하고 싶을 때

```python
MODE = "TEST"           # 시뮬레이션 모드
MAX_SIZE_BTC = 0.0001   # 최소 수량
```

### 실제로 돌리고 싶을 때

```python
MODE = "LIVE"           # 실제 주문
MAX_SIZE_BTC = 0.0002   # 약 $20 정도
```

---

## 실행 화면

```
┌─ StandX Market Making [LIVE] ─────────────────────┐
│ ▌ ACCOUNT                                         │
│   Available: $100.00                              │
│   Order Size: 0.0002 BTC ($20.00) x6              │
│                                                   │
│ ▌ MARKET DATA                                     │
│   Mark Price: 100,000.00                          │
│   Best Bid: 99,990.00  │  Best Ask: 100,010.00    │
│   OB Spread:  2.00 bps │  Drift:  1.50 bps        │
│                                                   │
│ ▌ ORDERS                                          │
│   SELL: ● OPEN  @ 100,008.00  x0.0002             │
│   BUY:  ● OPEN  @  99,992.00  x0.0002             │
│                                                   │
│ ▌ STATUS                                          │
│   ● MONITORING - Orders active                    │
└───────────────────────────────────────────────────┘
```

---

## 종료 방법

`Ctrl+C`를 누르면 종료됩니다.

LIVE 모드에서는 자동으로 모든 주문을 취소한 후 종료합니다.

---

## 원격 서버에서 실행 (AWS, GCP 등)

SSH 접속이 끊겨도 봇이 계속 돌아가게 하려면 **tmux**를 사용하세요.

### tmux 설치

```bash
# Ubuntu/Debian
sudo apt install tmux

# Amazon Linux
sudo yum install tmux
```

### 사용법

**1. 새 세션 시작**
```bash
tmux new -s mm
```
> `mm`은 세션 이름입니다. 원하는 이름으로 바꿔도 됩니다.

**2. 봇 실행**
```bash
python main.py
```

**3. 세션에서 분리 (봇은 계속 실행됨)**
```
Ctrl+B 누른 후 D
```
> SSH 끊겨도 봇은 계속 돌아갑니다!

**4. 나중에 세션 다시 연결**
```bash
tmux attach -t mm
```
> 대시보드 화면이 그대로 보입니다.

**5. 봇 종료하고 싶을 때**
```bash
tmux attach -t mm    # 세션 연결
Ctrl+C               # 봇 종료
exit                 # 세션 종료
```

### tmux 명령어 요약

| 명령어 | 설명 |
|--------|------|
| `tmux new -s 이름` | 새 세션 시작 |
| `tmux attach -t 이름` | 세션 다시 연결 |
| `tmux ls` | 실행 중인 세션 목록 |
| `tmux kill-session -t 이름` | 세션 강제 종료 |
| `Ctrl+B` → `D` | 세션에서 분리 (detach) |

---

## 문제 해결

### "ModuleNotFoundError" 에러가 나요

의존성이 설치 안 된 것입니다:
```bash
pip install -r requirements.in
```

### ".env 파일을 찾을 수 없어요"

`.env.example`을 `.env`로 복사했는지 확인하세요:
```bash
cp .env.example .env
```

### "config 모듈을 찾을 수 없어요"

`config.example.py`를 `config.py`로 복사했는지 확인하세요:
```bash
cp config.example.py config.py
```

### 봇이 바로 종료돼요

1. `.env`에 `WALLET_ADDRESS`가 제대로 입력됐는지 확인
2. StandX에 담보금(DUSD)이 있는지 확인

---

## 동작 원리

1. **주문 배치**: 현재가 기준 ±SPREAD_BPS 위치에 BUY/SELL 주문
2. **Maker 검증**: Taker가 되면 즉시 취소 (손실 방지)
3. **Drift 모니터링**: 가격 변동 추적
4. **리밸런싱**: 가격이 많이 움직이면 주문 취소 후 재배치
5. **반복**: 위 과정을 계속 반복

---

## 주의사항

- **처음에는 반드시 `MODE = "TEST"`로 테스트하세요!**
- LIVE 모드는 실제 돈이 사용됩니다
- 담보금이 부족하면 주문이 생성되지 않습니다
