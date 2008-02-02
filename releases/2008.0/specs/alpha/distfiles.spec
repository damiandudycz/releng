subarch: alpha
version_stamp: 2008.0
target: grp
rel_type: default
profile: default-linux/alpha/2008.0
snapshot: 2008.0
source_subpath: default/stage3-alpha-2008.0
grp: src

grp/use:
	bindist

grp/src/type: srcset
grp/src/packages:
	udev
	devfsd
	=vanilla-sources-2.4*
	=vanilla-sources-2.6*
	rp-pppoe
	speedtouch
	pptpclient
	iputils
	vixie-cron
	dcron
	sysklogd
	metalog
	syslog-ng
	xfsprogs
	reiserfsprogs
	dosfstools
	aboot
	gentoolkit
	chkrootkit
	isdn4k-utils
	iproute2
#	wireless-tools
	genkernel
