# StandX Market Making Bot

StandX 무기한 선물 거래소에서 자동으로 마켓메이킹을 수행하는 봇입니다.

## 개요

Mark Price 기준 ±8bps 위치에 양방향(BUY/SELL) 지정가 주문을 배치하고, 가격 변동(drift)에 따라 자동으로 리밸런싱합니다.

### 주요 기능

- **듀얼 모드**: TEST(시뮬레이션) / LIVE(실제 주문)
- **Maker 전용**: Taker 조건이 되면 즉시 주문 취소
- **자동 리밸런싱**: 가격이 기준점에서 3bps 이상 이동하면 주문 재배치
- **담보금 기반 수량 계산**: 6배 레버리지로 양방향 3배씩 분배
- **실시간 대시보드**: Rich TUI로 주문 상태, 포지션, 수익 모니터링

## 설치

```bash
pip install -r requirements.in
```

Python 3.10 필요

## 환경 설정

`.env.example`을 `.env`로 복사 후 설정:

```
WALLET_ADDRESS=0x...
PRIVATE_KEY=생략가능, 생략시 로그인창으로 연결
```

- `WALLET_ADDRESS`: BSC 지갑 주소
- `PRIVATE_KEY`: 개인키 (생략 시 브라우저 로그인)

## 실행

```bash
python main.py
```

LIVE 모드 실행 시 `YES` 입력으로 확인 필요

## 설정 파라미터

`main.py` 상단에서 조정 가능:

| 파라미터 | 기본값 | 설명 |
|---------|--------|------|
| `MODE` | `"LIVE"` | `"TEST"` 또는 `"LIVE"` |
| `COIN` | `"BTC"` | 거래 코인 |
| `SPREAD_BPS` | `8.0` | 주문 스프레드 (bps) |
| `DRIFT_THRESHOLD` | `3.0` | 리밸런스 트리거 (bps) |
| `MIN_WAIT_SEC` | `3.0` | 주문 변경 최소 대기 시간 |
| `LEVERAGE` | `6.0` | 레버리지 배수 |
| `SIZE_UNIT` | `0.0001` | 주문 수량 단위 (BTC) |
| `MAX_SIZE_BTC` | `0.0002` | 최대 주문 수량 |

## 동작 원리

1. **주문 배치**: Mark Price 기준 ±SPREAD_BPS 위치에 BUY/SELL 주문
2. **Maker 검증**: 주문이 Taker가 되면 즉시 취소
3. **Drift 모니터링**: 현재가와 주문 시점 가격 차이 추적
4. **리밸런싱**: Drift > DRIFT_THRESHOLD 시 주문 취소 후 재배치 (MIN_WAIT_SEC 대기)
5. **수량 계산**: `담보금 × 레버리지 / 2 / Mark Price`

## 대시보드

```
┌─ StandX Market Making [LIVE] ─┐
│ ▌ ACCOUNT                     │
│   Available: $100.00          │
│   Order Size: 0.0002 BTC      │
│                               │
│ ▌ MARKET DATA                 │
│   Mark Price: 100,000.00      │
│   Best Bid/Ask, Spread, Drift │
│                               │
│ ▌ SIMULATED ORDERS            │
│   SELL: ● OPEN @ 100,008.00   │
│   BUY:  ● OPEN @  99,992.00   │
│                               │
│ ▌ STATUS                      │
│   ● MONITORING                │
└───────────────────────────────┘
```

## 종료

`Ctrl+C`로 종료. LIVE 모드에서 미체결 주문이 있으면 취소 여부 확인
