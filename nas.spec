Summary:	Network Audio System
Summary(pl):	Sieciowy system d¼wiêku (NAS)
Name:		nas
Version:	1.5
Release:	1
License:	free
Group:		Applications/Sound
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
W pakiecie znajduje siê sieciwy system dzwiêku -- klient/serwer wraz z
bibliotek±. Najwa¿niejsze zalety sieciowego systemu d¼wiêku:
 - Niezale¿ny od urz±dzenia d¼wiêk w sieci
 - Du¿a ilo¶æ plików w ró¿nych formatach d¼wiêkowych
 - Mo¿liwo¶æ przechowywania d¼wiêku na serwerze
 - Zaawansowane miksowanie, oddzielanie i manipulacja formatem
   d¼wiêkowym
 - Mo¿liwo¶æ jednoczesnego u¿ywania urz±dzenia audio przez wiele
   programów
 - U¿ycie wzrastaj±cej ilo¶ci ISV
 - Ma³y rozmiar programu
 - Wolne oprogramowanie ! Nie ma ograniczeñ licencyjnych

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki naglówkowe dla NAS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description devel -l pl
Pliki naglówkowe dla NAS.

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
NAS static library.

%description static -l pl
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
