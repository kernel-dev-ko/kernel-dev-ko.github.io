---
comments: true
---

# SMB Network Filesystem : Introduce new In-Kernel SMB Server
제2회 한국 리눅스 커널 개발자 모임 발표: 메인 토픽

## 발표내용

IOT 및 기기들간의 네트워크 연결를 통한 서비스등으로 network filesystem 에 대한 필요성이 증가되고 있다.
MS, 애플, 안드로이드, 리눅스 등 모든 플랫폼에서 지원하는 SMB protocol이 connectivity 측면에서 가장
최적의 선택이나 대표적인 오픈소스 솔루션인 samba는 GPLv3 license로 인해 사용이 제한되고
상용업체들의 솔루션들은 비용 상승 문제로 채택이 어려웠다. In-Kernel engine을 통한 performance 최적화,
usersapce에서 구현하기 어려웠던 RDMA feature등도 samba를 대체하기 위한 새로운 솔루션의 needs 이다.
이 세미나에서는 이러한 새로운 needs들을 반영하기 위한 새로운 cifssrv
([https://github.com/namjaejeon/cifssrv](https://github.com/namjaejeon/cifssrv))라는
이름의 오픈소스 프로젝트에 대해서 얘기하고자 한다.

## 발표자 소개

### 전남재
삼성전자에서 리눅스 커널 개발관련 업무를 하고 있고 취미로 리눅스 커널에 기여해왔다.
주로 Linux Filesystem 분야에서 활동을 하고 있으며, 대표적으로 collapse range,
insert range 시스템 콜을 기여해왔다.
([https://lwn.net/Articles/589260/](https://lwn.net/Articles/589260/),
 [https://lwn.net/Articles/629965/](https://lwn.net/Articles/629965/)).
현재는 오늘 주제로 다룰 cifssrv() 개발에 주로 많은 시간을 투자하고 있다. 

## 발표 자료
[SMB-network-filesystem.pdf](https://github.com/kernel-dev-ko/kernel-dev-ko.github.io/raw/master/2nd/session-02/SMB-network-filesystem.pdf)
