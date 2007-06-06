# $Id$
# Authority: dag
# Upstream: <namikus$users,sf,net>

Summary: Recover files based on their headers and footers
Name: foremost
Version: 1.5
Release: 1
License: freeware
Group: Applications/Archiving
URL: http://foremost.sourceforge.net/

Source: http://foremost.sourceforge.net/pkg/foremost-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Foremost is a Linux program to recover files based on their headers and
footers. Foremost can work on image files, such as those generated by dd,
Safeback, Encase, etc, or directly on a drive. The headers and footers
are specified by a configuration file, so you can pick and choose which
headers you want to look for.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 foremost %{buildroot}%{_sbindir}/foremost
%{__install} -Dp -m0644 foremost.conf %{buildroot}%{_sysconfdir}/foremost.conf
%{__install} -Dp -m0644 foremost.1 %{buildroot}%{_mandir}/man1/foremost.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man1/foremost.1*
%config %{_sysconfdir}/foremost.conf
%{_sbindir}/foremost

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.69-0
- Updated to release 0.69.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.64-0
- Initial package. (using DAR)
