Summary:	Network Audio System
Summary(pl):	Sieciowy system d¼wiêku (NAS)
Name:		nas
Version:	1.2p5
Release:	5
Copyright:	free
Group:		Applications/Sound
Source:		ftp://ftp.x.org/contrib/audio/nas/%{name}-%{version}.tar.gz
Patch0:		nas.patch
Patch1:		nas-shared.patch
Patch2:		nas-glibc.patch
Patch3:		nas-auscope.patch
Buildroot:	/tmp/%{name}-%{version}-root

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

%description -l pl
W pakiecie znajduje siê sieciwy system dzwiêku -- klient/serwer wraz z 
bibliotek±. Najwa¿niejsze zalety sieciowego systemu d¼wiêku:

    o	Niezale¿ny od urz±dzenia d¼wiêk w sieci
    o	Du¿a ilo¶æ plików w ró¿nych formatach d¼wiêkowych
    o	Mo¿liwo¶æ przechowywania d¼wiêku na serwerze
    o	Zaawansowane miksowanie, oddzielanie i manipulacja formatem d¼wiêkowym
    o	Mo¿liwo¶æ jednoczesnego u¿ywania urz±dzenia audio przez wiele programów
    o	U¿ycie wzrastaj±cej ilo¶ci ISV
    o	Ma³y rozmiar programu
    o	Wolne oprogramowanie ! Nie ma ograniczeñ licencyjnych

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki naglówkowe dla NAS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description -l pl devel
Pliki naglówkowe dla NAS

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
NAS static library.

%description -l pl static
Biblioteka statyczna NAS.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%build
xmkmf
make WORLDOPTS="-k CDEBUGFLAGS='$RPM_OPT_FLAGS -D__USE_BSD_SIGNAL -w'" \
CXXDEBUGFLAGS="$RPM_OPT_FLAGS -w" World

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/{man1/*,man3/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/*.so.*
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/lib/X11/AuErrorDB
/usr/X11R6/lib/AUVoxConfig.eg
/usr/X11R6/man/man1/*

%files devel
%defattr(644,root,root,755)
/usr/X11R6/include/audio

%attr(755,root,root) /usr/X11R6/lib/*.so
/usr/X11R6/man/man3/*

%files static
%attr(644,root,root) /usr/X11R6/lib/*.a

%changelog
* Sun Dec 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.2p5-4d]
- build against Tornado,
- fixed compiler flags during compile,
- translation modified for pl,
- fixed en translation,
- fixed files %files,
- bziped man pages,
- other -- minor changes.

* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2p5-4]
- added -q %setup parameter,
- spec rewrited for using Buildroot,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- in %post{un} ldconfig is now runed -p parameter,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Sun Dec 21 1997 Kjetil Wiekhorst Jørgensen (jorgens@fastfire.pvv.org)
  [1.2p5-3]
- previous not commented release in rpm package.
