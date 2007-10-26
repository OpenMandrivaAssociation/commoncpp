%define name commoncpp
%define version 1.5.9
%define release %mkrel 2

%define major 2_1.5
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d


Summary:	A GNU package for creating portable C++ programs
Name:		%{name}
Provides:	CommonC++
Obsoletes:	CommonC++
Provides:	CommonC++2
Obsoletes:	CommonC++2
Version:	%version
Release:	%release
Group:		Development/C++
URL:		http://cplusplus.sourceforge.net/
Source:		http://ftp.gnu.org/gnu/commoncpp/commoncpp2-%{version}.tar.bz2
Patch0:         Doxyfile.patch

License:	GPL
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:  doxygen libxml2-devel glibc-static-devel libstdc++-devel

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
Requires:	%libname = %{version}-%{release} 
Provides:	lib%{name}2-devel = %{version}-%{release}
Provides:	libcommoncpp-devel
Obsoletes:	%mklibname %{name} 2_1.5 -d
Provides:	libCommonC++2-devel  = %{version}-%{release}
Obsoletes:	libCommonC++2-devel
Provides:	libCommonC++-devel
Obsoletes:	libCommonC++-devel

Requires: 	libxml2-devel

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
rm -rf $RPM_BUILD_ROOT
%setup -q -n commoncpp2-%{version}
{
cd doc
%patch0 -b .Doxyfile
cd ..
}

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/libxml2/libxml/"
CXXFLAGS="$RPM_OPT_FLAGS -I/usr/include/libxml2/libxml/"
./configure --prefix=%_prefix --datadir=%_datadir --libdir=%_libdir
# it tries to run make install, so we exit with 0
make ||:

%install
rm -rf %buildroot
%makeinstall 
%multiarch_binaries %buildroot/%_bindir/ccgnu2-config

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*.so.*

%files -n %libnamedev
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README TODO COPYING COPYING.addendum THANKS ChangeLog doc/html doc/latex
%_bindir/*/ccgnu2-config
%_bindir/ccgnu2-config
%_datadir/aclocal/*
%_infodir/*
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_includedir/cc++
%_libdir/pkgconfig/*.pc

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%post -n %libnamedev
%_install_info commoncpp2.info

%postun -n %libnamedev
%_remove_install_info commoncpp2.info


