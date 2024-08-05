---
layout: default
comments: true
---

# LUF(Lazy Unmap Flush) 메커니즘 소개
제9회 한국 리눅스 커널 개발자 모임 발표: 정규 세션

## 발표내용
프로세스의 페이지 테이블 매핑을 변경하면 TLB shoodown를 통해서 관련 CPU들이 새로운 페이지를 볼 수 있게 해 주어야 한다.
그렇게 하지 않으면 사용하지 않기로 한 오래된 페이지를 가지고 잘못된 연산을 수행할 수 있기 때문에 위험하다.
하지만, 읽기 전용 매핑이 메모리 회수 목적이나 마이그레이션 목적으로 끊어지는 경우(unmap)에는 끊어진 페이지가 변경되지 않는 한 TLB shootdown을 수행하지 않아도 문제가 발생하지 않는다.
프로파일링을 통해 시스템에 읽기 전용 매핑이 많음을 확인하고 이를 최대한 뒤로 미루는 개념을 구현하여 TLB shootdown 횟수를 크게 줄인 LUF(Lazy Unmap Flush) 메커니즘에 대해서 소개한다.
(https://lore.kernel.org/lkml/20240531092001.30428-1-byungchul@sk.com/)

## 발표자 소개

### 박병철
현재 SK hynix에서 메모리 관리 서브시스템에 컨트리뷰션을 하고 있다.
LUF(Lazy Unmap Flush) 메커니즘 외에도 DEPT(DEPendency Tracker) 툴을 개발 중이며, 주요 관심사는 스케줄러, 동기화, 메모리 관리이다.

## 발표 자료
발표 하루전 업데이트 예정
