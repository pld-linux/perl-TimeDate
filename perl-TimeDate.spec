%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Date
Summary:	Manipulating timezones and parsing/formatting dates in Perl
Summary(pl):	Manipulowanie strefami czasowymi i analizowanie/formatowanie dat w Perlu
Name:		perl-TimeDate
Version:	1.14
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeDate contains Date::Format, Date::Parse and Time::Zone.

Date::Format provides routines to format dates into ASCII strings.
They correspond to the C library routines strftime() and ctime().

Date::Parse provides two routines for parsing date strings into time
values: str2time(DATE [, ZONE]) and strptime(DATE [, ZONE]).

Time::Zone contains miscellaneous timezone manipulations routines.

%description -l pl
TimeDate zawiera modu³y: Date::Format, Date::Parse i Time::Zone.

Date::Format dostarcza funkcje, formatuj±ce datê w ci±gi ASCII.
Funkcje te odpowiadaj± strftime() i ctime() z biblioteki C.

Date::Parse udostêpnia dwie funkcje do przetwarzania dat w warto¶ci
time: str2time(DATE [, ZONE]) and strptime(DATE [, ZONE]).

Time::Zone zawiera ró¿ne funkcje, s³u¿±ce do manipulowania strefami
czasowymi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Date/*.pm
%dir %{perl_sitelib}/Date/Language
%{perl_sitelib}/Date/Language/*.pm
%{perl_sitelib}/Time/*.pm
%{_mandir}/man3/*
