---
layout: default
---
# 시스템 관리자를 위한 커널 공격 표면 파악: 주요 CVE 사례와 검증 노하우

## 요약
리눅스 커널의 대표적인 공격 표면(Attack Surface)을 알아보고,
24 ~ 25년도에 있었던, 각 공격 표면에 해당하는 주요 CVE들을 소개

리눅스 재단이 CNA가 된 이후, 사소한 버그 수정에도 CVE 발급을 남발하여 더 이상 리눅스 커널 CVE에는 별다른 가치가 없게 되었습니다.
별다른 가치가 없는 버그 패치가 아닌, 실제로 공격에 사용될 수 있는 CVE를 식별하는 노하우에 대해서도 다룰 예정이며, 이는 시스템 관리자, 커널 개발자 및 메인테이너에게 유용한 정보가 될 것이라 생각합니다.

## 발표 자료
발표 자료 비공개 (행사 내에서만 공개)

## 발표자 소개
김현우

Work Experience
- Theori (2022.11 ~ 2025.07)

Awards
- Pwnie Awards 2025 Best Privilege Escalation category WIN (CVE-2024-50264)
- Pwn2Own Berlin 2025 Red Hat Linux in the LPE category WIN (Theori, $15,000)
- Google kernelCTF LTS-6.6.75/COS-105 1-day WIN (CVE-2025-21756, $71,337)
- Google kernelCTF LTS-6.6.56/COS-109 0-day WIN (CVE-2024-50264, $81,337)
- Google kernelCTF LTS-6.6.35 0-day WIN (CVE-2024-41010, $51,337)

Vulnerability Reports
- CVE-2025-38087 (Linux Kernel Traffic Control TAPRIO Use-After-Free)
- CVE-2024-50264 (Linux Kernel Virtual Socket Use-After-Free)
- CVE-2024-27394 (Linux Kernel TCP Use-After-Free)
- CVE-2024-27395 (Linux Kernel OpenvSwitch Use-After-Free)
- CVE-2024-27396 (Linux Kernel GTP Use-After-Free)
- CVE-2023-51779 (Linux Kernel Bluetooth Socket Use-After-Free)
- CVE-2023-51780 (Linux Kernel ATM Socket Use-After-Free)
- CVE-2023-51781 (Linux Kernel Appletalk Socket Use-After-Free)
- CVE-2023-51782 (Linux Kernel Rose Socket Use-After-Free)
- CVE-2023-32269 (Linux Kernel NET/ROM Socket Use-After-Free)
- CVE-2022-41218 (Linux Kernel DVB Core Use-After-Free)
- CVE-2022-45884 (Linux Kernel DVB Core Use-After-Free)
- CVE-2022-45885 (Linux Kernel DVB Core Use-After-Free)
- CVE-2022-45886 (Linux Kernel DVB Core Use-After-Free)
- CVE-2022-45919 (Linux Kernel DVB Core Use-After-Free)
- CVE-2022-40307 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-41848 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-41849 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-41850 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-44032 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-44033 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-44034 (Linux Kernel Device Driver Use-After-Free)
- CVE-2022-45888 (Linux Kernel Device Driver Use-After-Free)

Linux Kernel Contributions
- net/sched: fix use-after-free in taprio_dev_notifier
- vsock: prevent null-ptr-deref in vsock_*[has_data\|has_space]
- vsock/virtio: cancel close work in the destructor
- vsock/virtio: discard packets if the transport changes
- vsock/virtio: Initialization of the dangling pointer occurring in vsk->trans
- hv_sock: Initializing vsk->trans to NULL to prevent a dangling pointer
- tcp: Fix Use-After-Free in tcp_ao_connect_init
- net: openvswitch: Fix Use-After-Free in ovs_ct_exit
- net: gtp: Fix Use-After-Free in gtp_dellink
- Bluetooth: af_bluetooth: Fix Use-After-Free in bt_sock_recvmsg
- atm: Fix Use-After-Free in do_vcc_ioctl
- appletalk: Fix Use-After-Free in atalk_ioctl
- net/rose: Fix Use-After-Free in rose_ioctl
- media: dvb-core: Fix use-after-free due to race at dvb_register_device()
- af_key: Fix heap information leak
- netrom: Fix use-after-free caused by accept on already connected socket
- net/rose: Fix to not accept on connected socket
- net/x25: Fix to not accept on connected socket
- efi: capsule-loader: Fix use-after-free in efi_capsule_write
- HID: roccat: Fix Use-After-Free in roccat_read
- video: fbdev: smscufx: Fix use-after-free in ufx_ops_open()
- video: fbdev: smscufx: Fix several use-after-free bugs
- char: xillybus: Fix trivial bug with mutex
- bpf: Always use maximal size for copy_array()
- media: dvb-core: Fix UAF due to refcount races at releasing
