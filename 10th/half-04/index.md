---
layout: default
---
# Zombie Memory Cgroup 이슈와 논의 중인 해결 방안

## 요약
Memory cgroup은 상위 cgroup이 계층 구조에서 제거된 이후에도, 소유한 메모리가 모두 해제되기 전까지는 좀비 상태로 남습니다. 시나리오에 따라 일부 메모리는 회수할 수 없는 경우도 있기 때문에, memory cgroup이 장기간 좀비 상태로 유지될 수 있습니다. 만약 cgroup을 자주 생성하고 삭제하는 경우 이러한 zombie memory cgroup이 누적되어 커널 메모리가 낭비될 수 있으며, 이를 어떻게 해결할 수 있을지에 대해 논의합니다.

## 발표 자료
(준비중)

## 발표자 소개
유형곤 (Harry Yoo)
* Oracle에서 업스트림 및 다운스트림 리눅스 커널의 메모리 관리 서브시스템 개발
* Slab Allocator와 Reverse Mapping 서브시스템의 공식 리뷰어로 활동 중
* Memory Cgroup에도 관심
