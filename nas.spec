Summary:	Network Audio System
Summary(pl):	Sieciowy system d�wi�ku (NAS)
Summary(ru):	NAS - ������-��������� ������� ��������� �����
Summary(uk):	NAS - �̦���-�������� �������� Ц������� ��Ħ�
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
W pakiecie znajduje si� sieciowy system dzwi�ku -- klient/serwer wraz z
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
 - Wolne oprogramowanie! Nie ma ogranicze� licencyjnych

%description -l ru
���� ����� �������� ���������� ��� ���� ������� ������-���������
��������� �����, � �����������. �������� ����������� NAS ��������:
    - ����������� �� ��������� ����� �� ����
    - ������� ���������� �������������� ��������
    - ����������� ���������� ������ �� ������� ��� �������� ����������
      ������������
    - ������� ����������� ������������, ���������� � �����������
      ������������
    - ������������� ������������� �������������� ������� ������������
    - ����������� �������� ������ ISV
    - ��������� ������
    - �������� �� ������������ �������

%description -l uk
��� ����� ͦ����� ������� ��� ����֦ ������� �̦���-�������ϧ
Ц������� �����, � ¦�̦������. �����צ ��������Ԧ NAS ���������:
    - ��������� צ� ������ϧ� ��Ħ� ����� ������
    - ������ ˦��˦��� Ц����������� �����Ԧ�
    - �����צ��� ���Ҧ����� ���˦� �� �����Ҧ ��� �������� ����������
      �����������
    - ����˦ ��������Ԧ ͦ��������, ���Ħ����� �� ��Φ����æ� ��Ħ�������
    - ��������� ������������ ��Ħ�������ϧ� �������� �����������
      ����������
    - ��������դ���� ������������� ������ ISV
    - ��������� ���ͦ�
    - ������ צ� ̦���ڦ���� ����

%package devel
Summary:	Development headers for writing programs using NAS
Summary(pl):	Pliki nagl�wkowe dla NAS
Summary(ru):	���������� � .h-����� ��� �������� � ���������� NAS
Summary(uk):	��̦����� �� .h-����� ��� ������� � Ц�������� NAS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own network audio programs.

%description devel -l pl
Pliki nagl�wkowe dla NAS.

%description devel -l ru
���� ����� ��������� ��� ������������� ����������� ��������� �
���������� ����� �� ����.

%description devel -l uk
��� ����� ������Ѥ ��� ���������� ����Φ �������� � Ц�������� �����
����� ������.

%package static
Summary:	NAS static library
Summary(pl):	Biblioteka statyczna NAS
Summary(ru):	����������� ���������� ��� �������� � ���������� NAS
Summary(uk):	������Φ ¦�̦����� ��� ������� � Ц�������� NAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
NAS static library.

%description static -l pl
Biblioteka statyczna NAS.

%description static -l ru
����������� ���������� ��� �������� � ���������� ����� �� ����.

%description static -l uk
������Φ ¦�̦����� ��� ������� � Ц�������� ����� ����� ������.

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
