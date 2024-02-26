subarch: amd64
target: stage1
version_stamp: llvm-systemd-@TIMESTAMP@
rel_type: 23.0-llvm
profile: default/linux/amd64/23.0/llvm/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-llvm/stage3-amd64-llvm-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
