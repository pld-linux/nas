Summary:	Network Audio System
Summary(pl):	Sieciowy system d╪wiЙku (NAS)
Summary(ru):	NAS - клиент-серверная сетевая поддержка аудио
Summary(uk):	NAS - кл╕╓нт-серверна мережева п╕дтримка ауд╕о
Name:		nas
Version:	1.5
Release:	4
License:	Free
Group:		Applications/Sound
Source0:	http://radscan.com/nas/%{name}-%{version}.src.tar.gz
URL:		http://radscan.com/nas.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
W pakiecie znajduje siЙ sieciowy system dzwiЙku -- klient/serwer wraz z
bibliotek╠. Najwa©niejsze zalety sieciowego systemu d╪wiЙku:
 - Niezale©ny od urz╠dzenia d╪wiЙk w sieci
 - Du©a ilo╤Ф plikСw w rС©nych formatach d╪wiЙkowych
 - Mo©liwo╤Ф przechowywania d╪wiЙku na serwerze
 - Zaawansowane miksowanie, oddzielanie i manipulacja formatem
   d╪wiЙkowym
 - Mo©liwo╤Ф jednoczesnego u©ywania urz╠dzenia audio przez wiele
   programСw
 - U©ycie wzrastaj╠cej ilo╤ci ISV
 - MaЁy rozmiar programu
 - Wolne oprogramowanie! Nie ma ograniczeЯ licencyjnych

%description -l ru
Этот пакет содержит прозрачную для сети систему клиент-серверной
поддержки звука, с библиотекой. Ключевые возможности NAS включают:
    - Независимое от устройств аудио по сети
    - Большое количество поддерживаемых форматов
    - Возможность сохранения звуков на сервере для быстрого повторного
      проигрывания
    - Широкие возможности микширования, разделения и манипуляции
      аудиоданными
    - Одновременное использование аудиоустройств многими приложениями
    - Применяется растущим числом ISV
    - Маленький размер
    - Свободна от лицензионных условий

%description -l uk
Цей пакет м╕стить прозору для мереж╕ систему кл╕╓нт-серверно╖
п╕дтримки звуку, з б╕бл╕отекою. Ключов╕ можливост╕ NAS включають:
    - Незалежне в╕д пристро╖в ауд╕о через мережу
    - Велика к╕льк╕сть п╕дтримуваних формат╕в
    - Можлив╕сть збер╕гання звук╕в на сервер╕ для швидкого повторного
      програвання
    - Широк╕ можливост╕ м╕кшування, розд╕лення та ман╕пуляц╕╖ ауд╕оданими
    - Одночасне використання ауд╕опристро╖в багатьма прикладними
      програмами
    - Застосову╓ться всезростаючим числом ISV
    - Маленький розм╕р
    - В╕льна в╕д л╕ценз╕йних умов

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki naglСwkowe dla NAS
Summary(ru):	Библиотеки и .h-файлы для программ с поддержкой NAS
Summary(uk):	Б╕бл╕отеки та .h-файли для програм з п╕дтримкою NAS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description devel -l pl
Pliki naglСwkowe dla NAS.

%description devel -l ru
Этот пакет позволяет вам разрабатывать собственные программы с
поддержкой звука по сети.

%description devel -l uk
Цей пакет дозволя╓ вам розробляти власн╕ програми з п╕дтримкою звуку
через мережу.

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Summary(ru):	Статические библиотеки для программ с поддержкой NAS
Summary(uk):	Статичн╕ б╕бл╕отеки для програм з п╕дтримкою NAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
NAS static library.

%description static -l pl
Biblioteka statyczna NAS.

%description static -l ru
Статические библиотеки для программ с поддержкой звука по сети.

%description static -l uk
Статичн╕ б╕бл╕отеки для програм з п╕дтримкою звуку через мережу.

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
	MANPATH=%{_mandir} \
	USRLIBDIR=%{_libdir} \
	BINDIR=%{_bindir} \
	INCROOT=%{_includedir} \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/nasd.conf.eg \
	$RPM_BUILD_ROOT%{_sysconfdir}/nasd.conf
mv $RPM_BUILD_ROOT%{_mandir}/man5/nasd.conf.5nas \
	$RPM_BUILD_ROOT%{_mandir}/man5/nasd.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ TODO BUGS
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/nasd.conf
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_bindir}/*
/usr/X11R6/lib/X11/AuErrorDB
%{_mandir}/man[15]/*

%files devel
%defattr(644,root,root,755)
%doc doc/{*.txt,*.ps}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/audio
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
