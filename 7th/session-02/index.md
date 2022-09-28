---
layout: default
comments: true
---

# GKI - ARM도 하나의 커널로
제7회 한국 리눅스 커널 개발자 모임 발표: 정규 세션

## 발표내용
Upstream, SoC, OEM, ODM 등 파편화가 굉장히 심한 안드로이드의 세계에서
userspace쪽은 2017년부터 Project Treble로 표준화가 되었지만, 커널은
여전히 파편화가 심한 상태였습니다. 구글의 주도하에, 올해 출시되는 안드로이드
기기부터 GKI(Generic Kernel Image)를 통해 ARM/SoC 쪽 세계에서도 커널을
표준화하는 정책이 적용되기 시작하였습니다. 올해 출시되는 안드로이드 기기는
실제로 제조사 말고 구글에서 제공하는 커널 이미지로 교체를 하여도 사용이
가능한데요, 커널 모듈 간의 ABI가 어떻게 지켜지고 이에 따른 문제점들을
어떤 것인지 다룰 예정입니다.

## 발표자 소개

### 박주형
2012년부터 리눅스 커널 개발을 취미로 삼아오고, 인터넷에 "arter97"이란
아이디로 안드로이드 OS 최적화 등을 진행하여 꾸준히 개발하고 커뮤니티와
공유하고 있다. 현재 대구경북과학기술원(DGIST) 박사과정 재학 중이며
안드로이드 시스템을 연구하고 있다.

## 발표 자료
[session-02.pdf](https://github.com/kernel-dev-ko/kernel-dev-ko.github.io/raw/master/5th/session-02/session-02.pdf)
