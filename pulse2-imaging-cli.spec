%define name pulse2-imaging-cli
# http://mds.mandriva.org/svn/mmc-projects/pulse2/client/imaging/trunk/
%define snapshot 20091125
%define version 0
%define rel 1
%define release %mkrel 0.%{snapshot}.%{rel}
%define tname lrs-0.1

Name:           %{name}
Summary: 	Pulse2 Imaging command line interface
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Version:        %{version}
Release:        %{release}
License: 	GPL
URL:		http://mds.mandriva.com
Source:         %{name}-%{snapshot}.tar.bz2
Patch0:		lrs-0.1-parallel.patch
BuildRequires:	glibc-static-devel gcc3.3-cpp gcc3.3 rpm-build newt-devel
ExclusiveArch:	i586

%description
This package contains command line tools for Pulse2 Imaging.

%prep
rm -rf ${RPM_BUILD_ROOT}
%setup -q -n %{tname}
%patch0 -p1 -b .parallel

%build
# parallel build broken in internal libext2fs copy
%make -j1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
install -m755 autosave/autosave %{buildroot}%{_bindir}/autosave
install -m755 autorestore/autorestore %{buildroot}%{_bindir}/autorestore
install -m755 autorestore/revoboot %{buildroot}%{_bindir}/revoboot
install -m755 autorestore/revoinc %{buildroot}%{_bindir}/revoinc
install -m755 autorestore/revosendlog %{buildroot}%{_bindir}/revosendlog
install -m755 autorestore/revowait %{buildroot}%{_bindir}/revowait
install -m755 autorestore/revogetname %{buildroot}%{_bindir}/revogetname
install -m755 autorestore/revoinv  %{buildroot}%{_bindir}/revoinv
install -m755 autorestore/revosetdefault %{buildroot}%{_bindir}/revosetdefault

install -m755 bench/bench %{buildroot}%{_bindir}/bench
install -m755 bench/bench.ping %{buildroot}%{_bindir}/bench.ping
install -m755 revosave/image_e2fs %{buildroot}%{_bindir}/
install -m755 revosave/image_fat %{buildroot}%{_bindir}/
install -m755 revosave/image_jfs %{buildroot}%{_bindir}/
install -m755 revosave/image_lvm %{buildroot}%{_bindir}/
install -m755 revosave/image_ntfs %{buildroot}%{_bindir}/
install -m755 revosave/image_raw %{buildroot}%{_bindir}/
install -m755 revosave/image_swap %{buildroot}%{_bindir}/
install -m755 revosave/image_ufs %{buildroot}%{_bindir}/
install -m755 revosave/image_xfs %{buildroot}%{_bindir}/
install -m755 revosave/liblrs.so %{buildroot}%{_libdir}/liblrs.so
install -m755 revosave/liblrs.so.1 %{buildroot}%{_libdir}/liblrs.so.1
install -m755 ui_newt/ui_newt %{buildroot}%{_bindir}/ui_newt

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%{__mkdir_p} /revosave
%{__mkdir_p} /revolog
%{__mkdir_p} /revoinfo

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README scripts/* consts.mk INSTALL
%attr(755,root,root) %{_bindir}/*
%{_libdir}/liblrs*

%changelog
