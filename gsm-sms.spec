Summary:	Gsm Serial Cable SMS Controler
Summary(pl):	Kontroler SMS w telefonach GSM pod³±czonych przez port szeregowy
Name:		gsm-sms
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ep09.pld-linux.org/~blaass/%{name}-%{version}.tar.gz
# Source0-md5:	8bf59cea9edc4b97495912ce1946cf27
Requires:	perl-Device-Gsm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gsm Serial Cable SMS Controler can in very easy way read and send SMS
messages through the port connection. It works perfectly with Nokia
phones and Siemens. It also gives you abbility to check IMEI number or
software version. PDA isn't supported in this beta.

%description -l pl
Pakiet umo¿liwia ³atwe czytanie i wysy³anie wiadomo¶ci SMS poprzez
port szeregowy. Pod³±czamy telefon do portu szeregowego komputera i
wysy³amy, odbieramy wiadomo¶ci z konsoli. Program dzia³a znakomicie z
telefonami Nokia i Siemens. Potrafi tak¿e sprawdziæ numer IMEI
telefonu i wersjê oprogramowania.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name}.pl $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
