Summary:	Network Audio System
Summary(pl):	Sieciowy system dºwiÍku (NAS)
Name:		nas
Version:	1.5
Release:	1
License:	free
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/DºwiÍk
Source0:	http://radscan.com/nas/%{name}-%{version}.src.tar.gz
URL:		http://radscan.com/nas.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/nas

%description
This package contains a network-transparent, client/server audio
system, with a library Key features of the Network Audio System
include:
 - Device-independent audio over the network
 - Lots of audio file and data formats
 - Can store sounds in server for rapid replay
 - Extensive mixing, separating, and manipulation of audio data
 - Simultaneous use of audio devices by multiple applications
 - Use by a growing number of ISVs
 - Small size
 - Free! No obnoxious licensing terms

%description -l pl
W pakiecie znajduje siÍ sieciwy system dzwiÍku -- klient/serwer wraz z
bibliotek±. Najwaøniejsze zalety sieciowego systemu dºwiÍku:
 - Niezaleøny od urz±dzenia dºwiÍk w sieci
 - Duøa ilo∂Ê plikÛw w rÛønych formatach dºwiÍkowych
 - Moøliwo∂Ê przechowywania dºwiÍku na serwerze
 - Zaawansowane miksowanie, oddzielanie i manipulacja formatem
   dºwiÍkowym
 - Moøliwo∂Ê jednoczesnego uøywania urz±dzenia audio przez wiele
   programÛw
 - Uøycie wzrastaj±cej ilo∂ci ISV
 - Ma≥y rozmiar programu
 - Wolne oprogramowanie ! Nie ma ograniczeÒ licencyjnych

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki naglÛwkowe dla NAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description -l pl devel
Pliki naglÛwkowe dla NAS.

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
NAS static library.

%description -l pl static
Biblioteka statyczna NAS.

%prep
%setup -q

%build
xmkmf
%{__make} World \
	WORLDOPTS="-k CDEBUGFLAGS='%{rpmcflags} -D__USE_BSD_SIGNAL -w'" \
	CXXDEBUGFLAGS="%{rpmcflsgs} -w" \
	REQUIREDLIBS="-L%{_libdir} -lXt" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/nasd.conf.eg \
	$RPM_BUILD_ROOT%{_sysconfdir}/nasd.conf
mv $RPM_BUILD_ROOT%{_mandir}/man5/nasd.conf.5nas \
	$RPM_BUILD_ROOT%{_mandir}/man5/nasd.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/nasd.conf
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/AuErrorDB
%{_mandir}/man[15]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/audio
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
