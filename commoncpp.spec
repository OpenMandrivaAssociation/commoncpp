%define api	1.8
%define major	0
%define	libccext2	%mklibname ccext2
%define	libccgnu2	%mklibname ccgnu2
%define devname		%mklibname %{name} -d

Summary:	A GNU package for creating portable C++ programs
Name:		commoncpp2
Version:	1.8.1
Release:	16
Group:		Development/C++
License:	GPLv2+ with exceptions
URL:		https://www.gnu.org/software/commoncpp/
Source0:	https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
Patch0:		applog_pipe.patch
Patch1:		1.8.1-fix-buffer-overflow.patch
Patch2:		1.8.1-fix-c++14.patch
Patch3:		1.8.1-libgcrypt.patch
Patch4:		1.8.1-parallel-build.patch
# (fedora)
Patch5:		commoncpp2-gcc9.patch
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

#----------------------------------------------------------------------------

%package -n %{libccext2}
Summary:	A GNU package for creating portable C++ program
Group:		System/Libraries
Obsoletes:	%{_lib}commoncpp2_1.8 < 1.8.1-4

%description -n %{libccext2}
This package contains the shared library part of CommonC++.

%files -n %{libccext2}
%{_libdir}/libccext2-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libccgnu2}
Summary:	A GNU package for creating portable C++ program
Group:		System/Libraries
Conflicts:	%{_lib}commoncpp2_1.8

%description -n %{libccgnu2}
This package contains the shared library part of CommonC++.

%files -n %{libccgnu2}
%{_libdir}/libccgnu2-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	A GNU package for creating portable C++ program
Group:		Development/C++
Requires:	%{libccext2} = %{EVRD}
Requires:	%{libccgnu2} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}commoncpp-devel < 1.8.1-4
# Keep it for a while
Provides:	libcommoncpp-devel = %{EVRD}

%description -n %{devname}
This package contains the development files and documentation needed to build
programs with CommonC++.

%files -n %{devname}
%doc AUTHORS NEWS README TODO COPYING COPYING.addendum THANKS ChangeLog doc/html 
%{_bindir}/ccgnu2-config
%{_includedir}/cc++
%{_datadir}/aclocal/*
%{_infodir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export LC_ALL=C.utf-8
export CXXFLAGS="%{optflags} -std=c++14"

autoreconf -ifv
%configure \
	--disable-static \
	--disable-dependency-tracking

# (fedora)
# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	-e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
	-i libtool

%make_build

%install
%make_install

