---
layout: default
comments: true
---

# Linux Kernel Hacking (From user to root privileges)
제8회 한국 리눅스 커널 개발자 모임 발표: 정규 세션

## 발표내용
리눅스 커널에서 취약점을 찾아, 이를 공격하여 root 권한으로 상승시키는 일련의 과정들을 소개하겠습니다.

## 발표자 소개

### 김현우
정보보안 스타트업 Theori에서 Vulnerability Researcher로 재직중에 있으며, 여러 오픈소스에서 발생하는 취약점들을 연구하고 있습니다.

개인 이력

Vulnerability report
• CVE-2023-32269 (Linux kernel NET/ROM socket Use-After-Free)
• CVE-2022-41218 (Linux kernel DVB core Use-After-Free)
• CVE-2022-45884 (Linux kernel DVB core Use-After-Free)
• CVE-2022-45885 (Linux kernel DVB core Use-After-Free)
• CVE-2022-45886 (Linux kernel DVB core Use-After-Free)
• CVE-2022-45919 (Linux kernel DVB core Use-After-Free)
• CVE-2022-40307 (Linux kernel Device driver Use-After-Free)
• CVE-2022-41848 (Linux kernel Device driver Use-After-Free)
• CVE-2022-41849 (Linux kernel Device driver Use-After-Free)
• CVE-2022-41850 (Linux kernel Device driver Use-After-Free)
• CVE-2022-44032 (Linux kernel Device driver Use-After-Free)
• CVE-2022-44033 (Linux kernel Device driver Use-After-Free)
• CVE-2022-44034 (Linux kernel Device driver Use-After-Free)
• CVE-2022-45888 (Linux kernel Device driver Use-After-Free)

Linux kernel contribution
• af_key: Fix heap information leak
• netrom: Fix use-after-free caused by accept on already connected socket
• net/rose: Fix to not accept on connected socket
• net/x25: Fix to not accept on connected socket
• efi: capsule-loader: Fix use-after-free in efi_capsule_write
• HID: roccat: Fix Use-After-Free in roccat_read
• video: fbdev: smscufx: Fix use-after-free in ufx_ops_open()
• video: fbdev: smscufx: Fix several use-after-free bugs
• char: xillybus: Fix trivial bug with mutex
• bpf: Always use maximal size for copy_array()
• media: dvb-core: Fix UAF due to refcount races at releasing


## 발표 자료
[session-02](https://raw.githubusercontent.com/kernel-dev-ko/kernel-dev-ko.github.io/master/8th/session-02/session-02.pdf)
