%define api	1.8
%define major	0
%define	libccext2	%mklibname ccext2_ %{api} %{major}
%define	libccgnu2	%mklibname ccgnu2_ %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	A GNU package for creating portable C++ programs
Name:		commoncpp2
Version:	1.8.1
Release:	4
Group:		Development/C++
License:	GPLv2
Url:		http://www.gnutelephony.org
Source0:	http://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
Patch0:		applog_pipe.patch
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	glibc-static-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(zlib)

%description
Common C++2 is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++2 is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

%package -n %{libccext2}
Summary:	A GNU package for creating portable C++ program
Group:		System/Libraries
Obsoletes:	%{_lib}commoncpp2_1.8

%description -n %{libccext2}
This package contains the shared library part of CommonC++.

%package -n %{libccgnu2}
Summary:	A GNU package for creating portable C++ program
Group:		System/Libraries
Conflicts:	%{_lib}commoncpp2_1.8

%description -n %{libccgnu2}
This package contains the shared library part of CommonC++.

%package -n %{devname}
Summary:	A GNU package for creating portable C++ program
Group:		Development/C++
Requires:	%{libccext2} = %{version}-%{release}
Requires:	%{libccgnu2} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}commoncpp-devel

%description -n %{devname}
This package contains the development files and documentation needed to build
programs with CommonC++.

%prep
%setup -q
%apply_patches

%build
./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std 

%multiarch_binaries %{buildroot}%{_bindir}/ccgnu2-config

%files -n %{libccext2}
%{_libdir}/libccext2-%{api}.so.%{major}*

%files -n %{libccgnu2}
%{_libdir}/libccgnu2-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README TODO COPYING COPYING.addendum THANKS ChangeLog doc/html 
%{_bindir}/ccgnu2-config
%{multiarch_bindir}/ccgnu2-config
%{_includedir}/cc++
%{_datadir}/aclocal/*
%{_infodir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

