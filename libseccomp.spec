%global debug_package %{nil}

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name: libseccomp
Epoch: 100
Version: 2.5.1
Release: 1%{?dist}
Summary: Seccomp (mode 2) helper library
License: LGPLv2
URL: https://github.com/seccomp/libseccomp
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gperf
BuildRequires: make
BuildRequires: pkgconfig

%description
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts away
the underlying BPF-based syscall filter language and presents a more
conventional function-call based filtering interface.

%if 0%{?suse_version} > 1500 || 0%{?is_opensuse}
%package -n libseccomp2
Summary: Enhanced Seccomp (mode 2) helper library

%description -n libseccomp2
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts away
the underlying BPF-based syscall filter language and presents a more
conventional function-call based filtering interface.
%endif

%package devel
Summary: Development files for libseccomp, an enhanced Seccomp (mode 2) helper library
%if 0%{?suse_version} > 1500 || 0%{?is_opensuse}
Requires: libseccomp2 = %{epoch}:%{version}-%{release}
%else
Requires: libseccomp = %{epoch}:%{version}-%{release}
%endif

%description devel
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts away
the underlying BPF-based syscall filter language and presents a more
conventional function-call based filtering interface. This package
contains the development files for libseccomp.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libseccomp.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if 0%{?suse_version} > 1500 || 0%{?is_opensuse}
%files -n libseccomp2
%else
%files
%endif
%license LICENSE
%{_libdir}/libseccomp.so.*

%files devel
%{_bindir}/scmp_sys_resolver
%{_includedir}/seccomp-syscalls.h
%{_includedir}/seccomp.h
%{_libdir}/libseccomp.a
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
