---
layout: default
---
# GlusterFS in the Kernel - 서버 수정 없이 FUSE를 커널로

## 요약
GlusterFS의 FUSE 클라이언트를 커널 모듈로 옮긴 과정을 다룹니다. 서버는 그대로 두고, 커널에서 기존 GlusterFS 프로토콜을 그대로 구현해 DHT/AFR/EC, POSIX locks, RDMA까지 구현하는 과정입니다.

## 발표 자료
공유 예정

## 발표자 소개
### 김지현
스토리지와 파일 시스템을 즐기는 엔지니어입니다. 주로 분산 파일 시스템(GlusterFS, Lustre, DAOS 등), NVMe, CXL에 많은 관심을 기울이고 있습니다. 현재는 (주)글루시스에서 기업용 스토리지 관리 솔루션을 만들고 있습니다.
