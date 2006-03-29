# $Id$
# Authority: dag

Summary: Tool for debugging of embedded Linux applications
Name: coretrace
Version: 0.71
Release: 1
License: GPL
Group: Development/Debuggers
URL: http://www.arbetsmyra.dyndns.org/coretrace/

Source: http://www.arbetsmyra.dyndns.org/coretrace/download/coretrace_v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
Coretrace is a tool for debugging of embedded Linux applications. It works
by analysing core files from crashed applications and outputs a short
plain-text backtrace, suitable for putting into logfiles.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 coretrace %{buildroot}%{_bindir}/coretrace

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%{_bindir}/*

%changelog
* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 0.71-1
- Initial package. (using DAR)
