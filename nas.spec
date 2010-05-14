Summary:	Network Audio System
Summary(pl.UTF-8):	Sieciowy system dźwięku (NAS)
Summary(ru.UTF-8):	NAS - клиент-серверная сетевая поддержка аудио
Summary(uk.UTF-8):	NAS - клієнт-серверна мережева підтримка аудіо
Name:		nas
Version:	1.9.2
Release:	1
License:	Free
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/nas/%{name}-%{version}.src.tar.gz
# Source0-md5:	ed7864f55b384452167959022cfb403b
URL:		http://radscan.com/nas.html
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xorg-cf-files >= 1.0.1-0.3
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nas

%description
This package contains a network-transparent, client/server audio
system, with a library. Key features of the Network Audio System
include:
 - Device-independent audio over the network
 - Lots of audio file and data formats
 - Can store sounds in server for rapid replay
 - Extensive mixing, separating, and manipulation of audio data
 - Simultaneous use of audio devices by multiple applications
 - Use by a growing number of ISVs
 - Small size
 - Free! No obnoxious licensing terms.

%description -l pl.UTF-8
Pakiet zawiera przezroczysty sieciowo dźwiękowy system klient/serwer
wraz z biblioteką. Najważniejsze cechy Network Audio System to:
 - Przesyłanie dźwięku przez sieć, niezależne od karty dźwiękowej,
 - Obsługa dużej ilości formatów dźwięku,
 - Przechowywanie dźwięku na serwerze w razie potrzeby wielokrotnego
   odtwarzania,
 - Zaawansowane miksowanie, oddzielanie i manipulacja dźwięku,
 - Możliwość jednoczesnego używania karty dźwiękowej przez wiele
   programów,
 - Obsługa przez coraz większą liczbę programów,
 - Mały rozmiar,
 - Wolne oprogramowanie! Brak wstrętnych ograniczeń licencyjnych.

%description -l ru.UTF-8
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

%description -l uk.UTF-8
Цей пакет містить прозору для мережі систему клієнт-серверної
підтримки звуку, з бібліотекою. Ключові можливості NAS включають:
    - Незалежне від пристроїв аудіо через мережу
    - Велика кількість підтримуваних форматів
    - Можливість зберігання звуків на сервері для швидкого повторного
      програвання
    - Широкі можливості мікшування, розділення та маніпуляції аудіоданими
    - Одночасне використання аудіопристроїв багатьма прикладними
      програмами
    - Застосовується всезростаючим числом ISV
    - Маленький розмір
    - Вільна від ліцензійних умов

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl.UTF-8):	Pliki naglówkowe dla NAS
Summary(ru.UTF-8):	Библиотеки и .h-файлы для программ с поддержкой NAS
Summary(uk.UTF-8):	Бібліотеки та .h-файли для програм з підтримкою NAS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package allows you to develop your own network audio programs.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla NAS.

%description devel -l ru.UTF-8
Этот пакет позволяет вам разрабатывать собственные программы с
поддержкой звука по сети.

%description devel -l uk.UTF-8
Цей пакет дозволяє вам розробляти власні програми з підтримкою звуку
через мережу.

%package static
Summary:	NAS static library
Summary(pl.UTF-8):	Biblioteka statyczna NAS
Summary(ru.UTF-8):	Статические библиотеки для программ с поддержкой NAS
Summary(uk.UTF-8):	Статичні бібліотеки для програм з підтримкою NAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
NAS static library.

%description static -l pl.UTF-8
Biblioteka statyczna NAS.

%description static -l ru.UTF-8
Статические библиотеки для программ с поддержкой звука по сети.

%description static -l uk.UTF-8
Статичні бібліотеки для програм з підтримкою звуку через мережу.

%prep
%setup -q

%build
xmkmf
%{__make} World \
	WORLDOPTS="-k CDEBUGFLAGS='%{rpmcflags} -D__USE_BSD_SIGNAL -w'" \
	CXXDEBUGFLAGS="%{rpmcflsgs} -w" \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	AUDIOLIBS="-L`pwd`/lib/audio -laudio" \
	REQUIREDLIBS="-lXt -X11 -lm" \
	EXTRAXAWCLIENTLIBS=

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ TODO HISTORY
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nasd.conf
%attr(755,root,root) %{_bindir}/au*
%attr(755,root,root) %{_bindir}/checkmail
%attr(755,root,root) %{_bindir}/issndfile
%attr(755,root,root) %{_bindir}/nasd
%attr(755,root,root) %{_bindir}/playbucket
%attr(755,root,root) %{_bindir}/soundtoh
%attr(755,root,root) %{_libdir}/libaudio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudio.so.2
%{_libdir}/X11/AuErrorDB
%{_mandir}/man1/au*.1x*
%{_mandir}/man1/checkmail.1x*
%{_mandir}/man1/issndfile.1x*
%{_mandir}/man1/nas.1x*
%{_mandir}/man1/nasd.1x*
%{_mandir}/man1/playbucket.1x*
%{_mandir}/man1/soundtoh.1x*
%{_mandir}/man5/nasd.conf.5x*

%files devel
%defattr(644,root,root,755)
%doc doc/{*.txt,*.ps}
%attr(755,root,root) %{_libdir}/libaudio.so
%{_includedir}/audio
%{_mandir}/man3/Au*.3x*
%{_mandir}/man3/Sound*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libaudio.a
