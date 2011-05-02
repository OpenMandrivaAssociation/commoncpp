%define name commoncpp
%define version 1.8.1
%define release %mkrel 2

%define major 2_1.8
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d


Summary:        A GNU package for creating portable C++ programs
Name:           %{name}
Provides:       CommonC++
Obsoletes:      CommonC++
Provides:       CommonC++2
Obsoletes:      CommonC++2
Version:        %version
Release:        %release
Group:          Development/C++
URL:            http://www.gnutelephony.org
Source:         http://ftp.gnu.org/gnu/commoncpp/commoncpp2-%{version}.tar.gz
Patch0:         applog_pipe.patch
License:        GPL
BuildRoot:      %_tmppath/%name-buildroot
BuildRequires:  doxygen glibc-static-devel libstdc++-devel
BuildRequires:	libtool zlib-devel

%description
Common C++2 is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++2 is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

%package -n %libname
Provides:  libCommonC++
Obsoletes: libCommonC++
Provides:  libCommonC++2 = %{version}-%{release}
Obsoletes: libCommonC++2
# to get rid of the old versions (2006.0 2007.0 and last 2007.1)
Obsoletes: libCommonC++2_1.3
Obsoletes: libCommonC++2_1.4
Obsoletes: libCommonC++2_1.5

Summary:        A GNU package for creating portable C++ program
Group:          System/Libraries

%description -n %libname
Common C++2 is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++2 is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

This package contains the shared library part of CommonC++.

%package -n %libnamedev
Summary:        A GNU package for creating portable C++ program
Group:          Development/C++
Requires:       %libname = %{version}-%{release} 
Provides:       lib%{name}2-devel = %{version}-%{release}
Provides:       libcommoncpp-devel
Obsoletes:      %mklibname %{name} 2_1.6 -d
Provides:       libCommonC++2-devel  = %{version}-%{release}
Obsoletes:      libCommonC++2-devel
Provides:       libCommonC++-devel
Obsoletes:      libCommonC++-devel

Requires:       libxml2-devel

%description -n %libnamedev
Common C++ is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++ is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

This package contains the development files and documentation needed to build
programs with CommonC++.

%prep
%setup -q -n commoncpp2-%{version}
%patch0 -p0 -b .missing_include

%build
./autogen.sh
%configure2_5x
make LIBTOOL=%_bindir/libtool

%install
rm -rf %buildroot
%makeinstall_std LIBTOOL=%_bindir/libtool

%multiarch_binaries %buildroot/%_bindir/ccgnu2-config

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*-1.8.so.*

%files -n %libnamedev
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README TODO COPYING COPYING.addendum THANKS ChangeLog doc/html 
%_bindir/ccgnu2-config
%{multiarch_bindir}/ccgnu2-config
%_datadir/aclocal/*
%_infodir/*
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_includedir/cc++
%_libdir/pkgconfig/*.pc

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%post -n %libnamedev
%_install_info commoncpp2.info

%postun -n %libnamedev
%_remove_install_info commoncpp2.info
