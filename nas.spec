Summary:	Network Audio System
Summary(pl):	Sieciowy system d�wi�ku (NAS)
Name:		nas
Version:	1.2p5
Release:	6
Copyright:	free
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
Source:		ftp://ftp.x.org/contrib/audio/nas/%{name}-%{version}.tar.gz
Patch0:		nas.patch
Patch1:		nas-shared.patch
Patch2:		nas-glibc.patch
Patch3:		nas-auscope.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

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
W pakiecie znajduje si� sieciwy system dzwi�ku -- klient/serwer wraz z 
bibliotek�. Najwa�niejsze zalety sieciowego systemu d�wi�ku:

    o	Niezale�ny od urz�dzenia d�wi�k w sieci
    o	Du�a ilo�� plik�w w r�nych formatach d�wi�kowych
    o	Mo�liwo�� przechowywania d�wi�ku na serwerze
    o	Zaawansowane miksowanie, oddzielanie i manipulacja formatem d�wi�kowym
    o	Mo�liwo�� jednoczesnego u�ywania urz�dzenia audio przez wiele program�w
    o	U�ycie wzrastaj�cej ilo�ci ISV
    o	Ma�y rozmiar programu
    o	Wolne oprogramowanie ! Nie ma ogranicze� licencyjnych

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki nagl�wkowe dla NAS
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description -l pl devel
Pliki nagl�wkowe dla NAS

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
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
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/AuErrorDB
%{_libdir}/AUVoxConfig.eg
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/audio

%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
