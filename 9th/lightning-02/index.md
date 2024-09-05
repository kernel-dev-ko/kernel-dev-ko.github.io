---
layout: default
comments: true
---

# Realtime Application 성능 최적화를 위한 RT-Linux 환경 구성
제9회 한국 리눅스 커널 개발자 모임 발표: 라이트닝 토크

## 발표내용
알티스트에서 기술지원 사례를 통해 얻은 preempt-rt 커널을 활용해 realtime 성능을 튜닝하기 위한 아래와 같은 주의사항을 정리하여 소개한다.
- Kernel Parameters
- CPU Affinity
- IRQ Affinity
- Multi-threading
- VGA Console
- Latencies caused by Page-faults
- Global variables and arrays
- Priority Inheritance Mutex support
- Priority 99
- Userland spin locks
- Input/Output
- Sharing data between applications
- Power management
- Signalling
- Clock
- Memory Overcommit
- RT Throttling
- Others

## 발표자 소개

### 황재호
OS 및 시스템 S/W 전문 기업 알티스트 리눅스 팀장.
무기체계 및 산업용 장비를 주 대상으로 Linux 공급 및 기술지원을 담당한다.

## 발표 자료
[Realtime Application 성능 최적화를 위한 RT-Linux 환경 구성](https://raw.githubusercontent.com/kernel-dev-ko/kernel-dev-ko.github.io/master/9th/lightning-02/lightning-02.pdf)
