---
comments: true
---

# Lockdep(Lock Dependency) Mechanism
제2회 한국 리눅스 커널 개발자 모임 발표: 메인 토픽

## 발표내용

Linux kernel 동기화 메커니즘 중에 lock이 가장 많이 사용되고 있는데, 주의 깊게  사용하지 않으면
시스템이 deadlock이라는 상태에 빠질 수 있기 때문에 lock의 특성과 종류를 정확하게 이해하고
사용하는 것이 중요하다. 특히, kernel code는 다양한 context에서 - 예로, sleep-able context,
process context, irq context, bottom-half context 등등 - 수행될 수 있기 때문에 context의 특성과
종류까지 정확하게 이해해야, deadlock을 회피하면서도 효과적으로 lock을 사용할 수 있다.
다행히, 이미 kernel 내에 lock dependency를 검사하는 lockdep 기능과 lock이 잘못 사용되었을 때에
이를 알려주는 prove locking이라는 기능이 있기 때문에, 이들을 활용하여 lock을 문제없이 사용하는
데에 도움을 받을 수 있다. 이번 발표에서는 기본적인 lockdep 기능뿐만 아니라 lockdep 기능 개선을
위해 LKML에서 활발하게 진행 중인 crossrelease 기능
([https://lwn.net/Articles/709849/](https://lwn.net/Articles/709849/))에 대해서도
소개한다. 

## 발표자 소개

### 박병철
LG전자 오픈소스팀에서 scheduler 분야에 컨트리뷰션을 하고 있다. 현재 주요 관심사는 scheduler(CFS, RT, deadline) 및 RCU 그리고 lockdep
([https://lwn.net/Articles/709849/](https://lwn.net/Articles/709849/))등이다. 

## 발표 자료
[lockdep.pdf](https://github.com/kernel-dev-ko/kernel-dev-ko.github.io/raw/master/2nd/session-01/lockdep.pdf)
