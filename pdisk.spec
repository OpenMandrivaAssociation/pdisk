%define version 0.8
%define diskdev_cmds diskdev_cmds-208.11

Summary:		A partitioning tool for Apple Macintosh-style partitioned disks
Name:			pdisk
Version:		%{version}
Release:		%mkrel 14
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



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8-13mdv2011.0
+ Revision: 667017
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-12mdv2011.0
+ Revision: 607085
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-11mdv2010.1
+ Revision: 523610
- rebuilt for 2010.1

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.8-10mdv2010.0
+ Revision: 453441
- fix str fmt
- fix build with gcc 4.4

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8-10mdv2009.0
+ Revision: 223490
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-9mdv2008.1
+ Revision: 179160
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.8-8mdv2008.0
+ Revision: 65019
- fix man pages


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 00:51:21 (55259)
- rebuild

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 00:43:40 (55257)
Import pdisk

* Fri Jun 02 2006 Stew Benedict <sbenedict@mandriva.com> 0.8-7mdv2007.0
- rebuild

* Mon May 16 2005 Stew Benedict <sbenedict@mandriva.com> 0.8-6mdk
- rebuild, patch for gcc-4.0 (P2)

* Fri Apr 02 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.8-5mdk
- add fsck_hfs, newfs_hfs from the Apple source
- add Roman Zippel's patches for hfsplus support
- (suggestions from J.A. Magallon)
- perms on executables (rpmlint)

* Fri Feb 06 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.8-4mdk
- rebuild
- add t command to change type of partition (Christiaan Welvaart)

