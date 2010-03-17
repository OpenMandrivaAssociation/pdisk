%define version 0.8
%define diskdev_cmds diskdev_cmds-208.11

Summary:		A partitioning tool for Apple Macintosh-style partitioned disks
Name:			pdisk
Version:		%{version}
Release:		%mkrel 11
License:		Apple Public Source License
Group:			System/Base

Source:			ftp://cfcl.com/pub/ev/pdisk.20000516.src.tar.bz2
Source1:		http://www.opensource.apple.com/darwinsource/tarballs/apsl/diskdev_cmds-208.11.tar.bz2
Patch0:			pdisk-changetype.patch
Patch1:			http://www.ardistech.com/hfsplus/diskdev_cmds.diff
Patch2:			pdisk-gcc-4.0.patch
Patch3:			pdisk-gcc44.patch
Patch4:			pdisk-fix-str-fmt.patch
URL:			http://cantaforda.com/cfcl/eryk/linux/pdisk/index.html
BuildRoot:		%{_tmppath}/%{name}-buildroot

%description
pdisk enables you to view and modify Apple Macintosh-style partition maps.
Normally, it is used to create Mandriva Linux partitions on your disk,
however, it can create partitions of any type, including HFS (except
it would be up to MacOS or some other tool to actually create the HFS
filesystem in that HFS partition).  pdisk won't put MacOS disk drivers
onto your disk.

%prep
%setup -q -a 1 -n pdisk
%patch0 -p1
pushd %{diskdev_cmds}
%patch1 -p1 -b .hfsplus
popd
%patch2 -p1 -b .gcc40
%patch3 -p0 -b .gcc44
%patch4 -p0 -b .str

%build
%make CFLAGS="%{optflags}"
cd %{diskdev_cmds}
%make -f Makefile.lnx

%install
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m755 pdisk $RPM_BUILD_ROOT/sbin/pdisk
install -m444 pdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m755 %{diskdev_cmds}/fsck_hfs.tproj/fsck_hfs $RPM_BUILD_ROOT/sbin
install -m755 %{diskdev_cmds}/newfs_hfs.tproj/newfs_hfs $RPM_BUILD_ROOT/sbin
install -m444 %{diskdev_cmds}/newfs_hfs.tproj/newfs_hfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
chmod 0444 README pdisk.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README pdisk.html
/sbin/pdisk
/sbin/newfs_hfs
/sbin/fsck_hfs

%{_mandir}/man8/pdisk.*
%{_mandir}/man8/newfs_hfs.*

