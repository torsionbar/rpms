# $Id$
# Authority: dag

%define real_name encfs

Summary: Encrypted pass-thru filesystem in userspace
Name: fuse-encfs
Version: 1.4.0
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.arg0.net/encfs

Source: http://www.arg0.net/encfs-1.4.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, fuse-devel >= 2.2, rlog-devel >= 1.3
Requires: fuse >= 2.2

Obsoletes: encfs <= %{name}-%{version}
Provides: encfs = %{name}-%{version}

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace. EncFS encrypts all data and filenames in the filesystem and
passes access through to the underlying filesystem. Similar to CFS except that
it does not use NFS. 

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}
### Make sure we install translations on EL5/x86_64 (bug in 1.4.0)
%{__make} %{?_smp_mflags} -C po

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
### Make sure we install translations on EL5/x86_64 (bug in 1.4.0)
%{__make} install DESTDIR="%{buildroot}" -C po
%find_lang %{real_name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/encfs.1*
%doc %{_mandir}/man1/encfsctl.1*
%{_bindir}/encfs
%{_bindir}/encfsctl
%{_bindir}/encfssh
%{_libdir}/libencfs.so*
%exclude %{_libdir}/libencfs.la

%changelog
* Tue Jan 08 2008 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
