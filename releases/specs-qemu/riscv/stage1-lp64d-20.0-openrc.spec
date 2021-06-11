subarch: rv64_lp64d
target: stage1
version_stamp: 20.0-openrc-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: 20.0
profile: default/linux/riscv/20.0/rv64gc/lp64d
snapshot: @TIMESTAMP@
source_subpath: 20.0/stage3-rv64_lp64d-20.0-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
