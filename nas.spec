Summary:     Network Audio System
Name:        nas
Version:     1.2p5
Release:     4
Copyright:   free
Group:       Applications/Sound
Source:      ftp://ftp.x.org/contrib/audio/nas/%{name}-%{version}.tar.gz
Patch0:      nas-1.2p5-1.patch
Patch1:      nas-1.2p5-shared.patch
Patch2:      nas-1.2p5-glibc.patch
Patch3:      nas-1.2p5-auscope.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
This package contains a network-transparent, client/server audio system,
with a library
Key features of the Network Audio System include:
    o   Device-independent audio over the network
    o   Lots of audio file and data formats
    o   Can store sounds in server for rapid replay
    o   Extensive mixing, separating, and manipulation of audio data
    o   Simultaneous use of audio devices by multiple applications
    o   Use by a growing number of ISVs
    o   Small size
    o   Free!  No obnoxious licensing terms

%package devel
Summary:     Development libraries and headers for writing programs using network audio
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%package static
Summary:     NAS static libraries
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
NAS static libraries.

%prep
%setup -q -n nas-1.2p5
%patch0 -p1 -b .usleep
%patch1 -p1 -b .shared
%patch2 -p1 -b .glibc
%patch3 -p1 -b .auscope

%build
xmkmf
make WORLDOPTS="-k CDEBUGFLAGS='$RPM_OPT_FLAGS -D__USE_BSD_SIGNAL'" World

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root, root) /usr/X11R6/lib/X11/AuErrorDB
%attr(644, root, root) /usr/X11R6/lib/AUVoxConfig.eg
%attr(644, root,  man) /usr/X11R6/man/man1/*

%files devel
%defattr(644, root,  root, 755)
/usr/X11R6/include/audio
/usr/X11R6/lib/lib*.so
%attr(644, root,  man) /usr/X11R6/man/man3/*

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2p5-4]
- added -q %setup parameter,
- spec rewrited for using Buildroot,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- in %post{un} ldconfig is now runed -p parameter,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Sun Dec 21 1997 Kjetil Wiekhorst Jørgensen (jorgens@fastfire.pvv.org)
  [1.2p5-3]
- previous not commented release in rpm package.
