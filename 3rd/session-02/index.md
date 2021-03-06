---
comments: true
---

# RISC-V 아키텍쳐 소스 분석
제3회 한국 리눅스 커널 개발자 모임 발표: 정규 세션

## 발표내용

최근에 마이크로프로세서 시장에서 가장 뜨거운 이슈로 부상하고 있는
RISC-V 오픈 소스 아키텍쳐에 대해서 소개하고
리눅스 커널 최신 버전(4.15)에 추가된 `/arch/riscv` 소스를 분석한 내용을 발표하고자 합니다.
RISC-V 아키텍쳐 명령어 특징과 장점에 대해서 말씀드리고
`/arch/riscv/include/asm`에 구현되어 있는 소스를 분석하여 RISC-V 아키텍쳐를 이해할 수 있도록 설명합니다.
아울러 `/arch/riscv/kernel`에 구현되어 있는 `entry.S`, `cpu.c`, `setup.c`, `smp.c` 등의 소스에 구현되어
있는 RISC-V 커널 소스를 분석한 내용을 공유하고자 합니다.

## 발표자 소개

### 정재준
* 커널 연구회(www.kernel.bz) 운영 중
* 부천대학교 지능로봇과 겸임교수 재직 중

## 발표 자료
[RISCV-analysis.pdf](https://github.com/kernel-dev-ko/kernel-dev-ko.github.io/raw/master/3rd/session-02/RISCV-analysis.pdf)

