---
layout: default
comments: true
---

# 구글 클라우드 서버의 커널을 해킹해 상금을 받아보자 (Google kernelCTF)
제9회 한국 리눅스 커널 개발자 모임 발표: 라이트닝 토크

## 발표내용
구글의 리눅스 커널 해킹 대회인 Google VRP kernelCTF에서 우승하여 $51,337를 받게 된 스토리


## 발표자 소개

### 김현우
정보보안 스타트업 Theori에서 Vulnerability Researcher로 재직중에 있으며, 여러 오픈소스에서 발생하는 취약점들을 연구하고 있습니다.

### 개인 이력

#### Vulnerability report

* CVE-2024-27394 (Linux kernel TCP Use-After-Free)
* CVE-2024-27395 (Linux kernel openvswitch Use-After-Free)
* CVE-2024-27396 (Linux kernel GTP Use-After-Free)
* CVE-2023-51779 (Linux kernel bluetooth socket Use-After-Free)
* CVE-2023-51780 (Linux kernel atm socket Use-After-Free)
* CVE-2023-51781 (Linux kernel appletalk socket Use-After-Free)
* CVE-2023-51782 (Linux kernel rose socket Use-After-Free)
* CVE-2023-32269 (Linux kernel NET/ROM socket Use-After-Free)
* CVE-2022-41218 (Linux kernel DVB core Use-After-Free)
* CVE-2022-45884 (Linux kernel DVB core Use-After-Free)
* CVE-2022-45885 (Linux kernel DVB core Use-After-Free)
* CVE-2022-45886 (Linux kernel DVB core Use-After-Free)
* CVE-2022-45919 (Linux kernel DVB core Use-After-Free)
* CVE-2022-40307 (Linux kernel Device driver Use-After-Free)
* CVE-2022-41848 (Linux kernel Device driver Use-After-Free)
* CVE-2022-41849 (Linux kernel Device driver Use-After-Free)
* CVE-2022-41850 (Linux kernel Device driver Use-After-Free)
* CVE-2022-44032 (Linux kernel Device driver Use-After-Free)
* CVE-2022-44033 (Linux kernel Device driver Use-After-Free)
* CVE-2022-44034 (Linux kernel Device driver Use-After-Free)
* CVE-2022-45888 (Linux kernel Device driver Use-After-Free)

#### Linux kernel contribution

* tcp: Fix Use-After-Free in tcp_ao_connect_init
* net: openvswitch: Fix Use-After-Free in ovs_ct_exit
* net: gtp: Fix Use-After-Free in gtp_dellink
* Bluetooth: af_bluetooth: Fix Use-After-Free in bt_sock_recvmsg
* atm: Fix Use-After-Free in do_vcc_ioctl
* appletalk: Fix Use-After-Free in atalk_ioctl
* net/rose: Fix Use-After-Free in rose_ioctl
* media: dvb-core: Fix use-after-free due to race at dvb_register_device()
* af_key: Fix heap information leak
* netrom: Fix use-after-free caused by accept on already connected socket
* net/rose: Fix to not accept on connected socket
* net/x25: Fix to not accept on connected socket
* efi: capsule-loader: Fix use-after-free in efi_capsule_write
* HID: roccat: Fix Use-After-Free in roccat_read
* video: fbdev: smscufx: Fix use-after-free in ufx_ops_open()
* video: fbdev: smscufx: Fix several use-after-free bugs
* char: xillybus: Fix trivial bug with mutex
* bpf: Always use maximal size for copy_array()
* media: dvb-core: Fix UAF due to refcount races at releasing

## 발표 자료
발표 자료 비공개 (행사 내에서만 공개)
