---
layout: default
comments: true
---

# LUF(Lazy Unmap Flush) 메커니즘 소개
제9회 한국 리눅스 커널 개발자 모임 발표: 정규 세션

## 발표내용
프로세스 페이지 테이블 매핑이 변경되면 TLB shootdown를 통해서 모든 CPU가 변경 후 페이지를 접근할 수 있도록 해 주어야 한다. 그렇게 하지 않으면 변경 전 페이지를 그대로 접근하는 CPU에 의해 시스템 crash가 발생할 수 있다. 하지만, 읽기 전용 매핑이 메모리 회수 목적이나 마이그레이션 목적으로 끊어지는 경우(unmap)에는 최적화 여지가 있다. 매핑이 끊어졌더라도 페이지 데이터 변경이 없는 동안에는 변경 전 페이지를 접근해서 읽기를 수행해도 문제가 발생하지 않는다. 즉, TLB shootdown을 미룰 수 있는 구간이 존재한다. 프로파일링을 통해 시스템에 읽기 전용 매핑이 많음을 확인하고 이를 최대한 뒤로 미루는 개념을 구현하여 TLB shootdown 횟수를 크게 줄인 LUF(Lazy Unmap Flush) 메커니즘에 대해서 소개한다.

https://lore.kernel.org/lkml/20240531092001.30428-1-byungchul@sk.com/

## 발표자 소개

### 박병철
현재 SK hynix에서 메모리 관리 서브시스템에 컨트리뷰션을 하고 있다. LUF(Lazy Unmap Flush) 메커니즘 외에도 DEPT(DEPendency Tracker) 툴을 개발 중이며, 주요 관심사는 스케줄러, 동기화, 메모리 관리이다.

## 발표 자료
발표 하루전 업데이트 예정
