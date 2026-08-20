---
layout: default
---
# BPF Memory Allocation

## 요약
일반적인 커널 코드와 달리, BPF 프로그램은 커널 내 다양한 지점에서 실행될 수 있어 실행 중 메모리를 할당할때 엄격한
제약이 있습니다. 이번 세션에서는 BPF가 실행되는 컨텍스트의 특수성과, 이러한 제약 속에서 메모리 할당 문제를 해결하기 위한
BPF의 노력과 최근 동향을 소개합니다.

## 발표 자료
공유 예정

## 발표자 소개
### 유형곤
유형곤 (Harry Yoo)
- Software Engineer @ $TO_BE_ANNOUNCED
- 리눅스 Slab 할당자 서브시스템 공동 메인테이너 (with Vlastimil Babka)
- 리눅스 Reverse Mapping 서브시스템 리뷰어
