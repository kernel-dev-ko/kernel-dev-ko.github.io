---
layout: default
---
# Device Memory TCP 를 통한 효율적인 데이터 전송
제10회 한국 리눅스 커널 개발자 모임 발표 : Half Session

## 요약
Device Memory TCP 는 Linux Kernel 6.12 에 추가된 기술로, 전통적인 TCP/IP 와는 다르게 packet 의 payload 를 Device Memory 로 직접 전송하여 host memory buffer 복사를 줄이는 기술이다.
- [관련 커널 패치 threads](https://lore.kernel.org/all/20240628003253.1694510-1-almasrymina@google.com/)
- [Netdev Conferenece 영상](https://www.youtube.com/watch?v=1xCk_aTtQ6U&t=1541s)
- [관련 리눅스커널 Changlog](https://kernelnewbies.org/LinuxChanges#Linux_6.16.Networking)

## 발표 자료
(준비중)

## 발표자 소개
문연수:
* 리눅스 커널 네트워크 서브 시스템에서 컨트리뷰터로 활동
* 최근에는 Device Memory TCP 를 활용한 AMD GPU RCCL 플러그인의 연구 개발
