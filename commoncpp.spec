%define major 2_1.8
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:        A GNU package for creating portable C++ programs
Name:           commoncpp
Version:        1.8.1
Release:        3
Group:          Development/C++
License:        GPL
URL:            http://www.gnutelephony.org
Source:         http://ftp.gnu.org/gnu/commoncpp/commoncpp2-%{version}.tar.gz
Patch0:         applog_pipe.patch
BuildRequires:  doxygen
BuildRequires:	glibc-static-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Provides:       CommonC++ = %{version}-%{release}
Provides:       CommonC++2 = %{version}-%{release}

%description
Common C++2 is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++2 is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

%package -n %{libname}
Provides:	libCommonC++ = %{version}-%{release}
Provides:	libCommonC++2 = %{version}-%{release}
Summary:	A GNU package for creating portable C++ program
Group:		System/Libraries

%description -n %{libname}
Common C++2 is a GNU package which offers portable "abstraction" of system
services such as threads, networks, and sockets. Common C++ also offers
individual frameworks generally useful to developing portable C++ applications
including a object persistance engine, math libraries, threading, sockets, etc.

Common C++2 is small, and highly portable. Common C++ will support most Unix
operating systems as well as Win32, in addition to GNU/Linux.

This package contains the shared library part of CommonC++.

%package -n %{libnamedev}
Summary:	A GNU package for creating portable C++ program
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release} 
Provides:	lib%{name}2-devel = %{version}-%{release}
Provides:	libcommoncpp-devel = %{version}-%{release}
Provides:	libCommonC++2-devel  = %{version}-%{release}
Provides:	libCommonC++-devel = %{version}-%{release}

%description -n %{libnamedev}
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
%configure2_5x --disable-static
make LIBTOOL=%{_bindir}/libtool

%install
%makeinstall_std LIBTOOL=%{_bindir}/libtool

%multiarch_binaries %{buildroot}%{_bindir}/ccgnu2-config

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/*-1.8.so.*

%files -n %{libnamedev}
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README TODO COPYING COPYING.addendum THANKS ChangeLog doc/html 
%{_bindir}/ccgnu2-config
%{multiarch_bindir}/ccgnu2-config
%{_datadir}/aclocal/*
%{_infodir}/*
%{_libdir}/*.so
%{_includedir}/cc++
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2mdv2011.0
+ Revision: 661634
- multiarch fixes

* Sat Nov 06 2010 Angelo Naselli <anaselli@mandriva.org> 1.8.1-1mdv2011.0
+ Revision: 594365
- New version 1.8.1

* Thu Jul 22 2010 Angelo Naselli <anaselli@mandriva.org> 1.8.0-5mdv2011.0
+ Revision: 556923
- upstream patch to fix applog thread safety

* Fri Mar 12 2010 Angelo Naselli <anaselli@mandriva.org> 1.8.0-4mdv2010.1
+ Revision: 518305
- Avoid crash for assert call using Engine and TCPStream

* Wed Feb 24 2010 Angelo Naselli <anaselli@mandriva.org> 1.8.0-2mdv2010.1
+ Revision: 510711
- removed wron Obsoletes directive

* Wed Feb 24 2010 Angelo Naselli <anaselli@mandriva.org> 1.8.0-1mdv2010.1
+ Revision: 510645
- new version

* Mon Aug 10 2009 Funda Wang <fwang@mandriva.org> 1.7.3-2mdv2010.0
+ Revision: 414175
- fix build with gcc 4.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Thu Mar 12 2009 Angelo Naselli <anaselli@mandriva.org> 1.7.3-1mdv2009.1
+ Revision: 354200
- New version 1.7.3

* Wed Mar 04 2009 Angelo Naselli <anaselli@mandriva.org> 1.7.2-1mdv2009.1
+ Revision: 348420
- new version 1.7.2

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 1.7.1-1mdv2009.1
+ Revision: 337802
- New version 1.7.1

* Wed Jan 21 2009 Angelo Naselli <anaselli@mandriva.org> 1.7.0-1mdv2009.1
+ Revision: 332196
- Official 1.7.0 version

* Fri Sep 12 2008 Angelo Naselli <anaselli@mandriva.org> 1.7.0-0.839.1mdv2009.0
+ Revision: 284221
- new pre-release version 1.7.0 (svn 839)

* Fri Jun 13 2008 Angelo Naselli <anaselli@mandriva.org> 1.6.2-2mdv2009.0
+ Revision: 218785
- rebuilt

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 22 2008 Angelo Naselli <anaselli@mandriva.org> 1.6.2-1mdv2009.0
+ Revision: 196538
- new version 1.6.2
- added a patch to fix String copy costructor (memory over allocation)

* Wed Feb 06 2008 Angelo Naselli <anaselli@mandriva.org> 1.6.1-1mdv2008.1
+ Revision: 163023
- new version 1.6.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Angelo Naselli <anaselli@mandriva.org> 1.6.0-2mdv2008.1
+ Revision: 115531
- URL updated

* Mon Dec 03 2007 Angelo Naselli <anaselli@mandriva.org> 1.6.0-1mdv2008.1
+ Revision: 114497
- New version 1.6.0 (ABI changed)

* Fri Oct 26 2007 Angelo Naselli <anaselli@mandriva.org> 1.5.9-2mdv2008.1
+ Revision: 102361
- New version 1.5.9

* Thu Jul 12 2007 Angelo Naselli <anaselli@mandriva.org> 1.5.7-1mdv2008.0
+ Revision: 51682
- new release 1.5.7
  followed new library policy

* Wed May 16 2007 Angelo Naselli <anaselli@mandriva.org> 1.5.6-1mdv2008.0
+ Revision: 27344
- New version 1.5.6


* Fri Feb 23 2007 Angelo Naselli <anaselli@mandriva.org> 1.5.5-1mdv2007.0
+ Revision: 125040

* Thu Jan 25 2007 Lenny Cartier <lenny@mandriva.com> 1.5.4-1mdv2007.1
+ Revision: 113287
- Update to 1.5.4

* Wed Nov 22 2006 Lenny Cartier <lenny@mandriva.com> 1.5.3-1mdv2007.1
+ Revision: 86125
- Update to 1.5.3
- Import CommonC++

