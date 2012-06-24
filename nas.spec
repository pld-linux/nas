Summary:	Network Audio System
Summary(pl):	Sieciowy system d�wi�ku (NAS)
Name:		nas
Version:	1.2p5
Release:	8
License:	free
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	ftp://ftp.x.org/contrib/audio/nas/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-auscope.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
W pakiecie znajduje si� sieciwy system dzwi�ku -- klient/serwer wraz z
bibliotek�. Najwa�niejsze zalety sieciowego systemu d�wi�ku:
 - Niezale�ny od urz�dzenia d�wi�k w sieci
 - Du�a ilo�� plik�w w r�nych formatach d�wi�kowych
 - Mo�liwo�� przechowywania d�wi�ku na serwerze
 - Zaawansowane miksowanie, oddzielanie i manipulacja formatem
   d�wi�kowym
 - Mo�liwo�� jednoczesnego u�ywania urz�dzenia audio przez wiele
   program�w
 - U�ycie wzrastaj�cej ilo�ci ISV
 - Ma�y rozmiar programu
 - Wolne oprogramowanie ! Nie ma ogranicze� licencyjnych

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki nagl�wkowe dla NAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description -l pl devel
Pliki nagl�wkowe dla NAS.

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
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
%{__make} WORLDOPTS="-k CDEBUGFLAGS='%{rpmcflags} -D__USE_BSD_SIGNAL -w'" \
CXXDEBUGFLAGS="%{rpmcflsgs} -w" REQUIREDLIBS="-L%{_libdir} -lXt" World

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

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
%defattr(644,root,root,755)
%{_libdir}/lib*.a
