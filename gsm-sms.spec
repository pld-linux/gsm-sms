Summary:	Gsm Serial Cable SMS Controler
Summary(pl):	Kontroler SMS w telefonach GSM, przez port serial
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
messages through the port connection. It works perfectly with nokia
phones and siemens. It also gives you abbility to check IMEI number or
software version. PDA isn't supported in this beta.

%description -l pl
Wysy�anie SMS przez kabel serial. Pod��czamy telefon do komputera na
porcie serial i wysy�amy, odbieramy wiadomo�ci z konsoli. Program
potrafi tak�e sprawdzi� numer IMEI telefonu i wersje oprogramowania.

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
