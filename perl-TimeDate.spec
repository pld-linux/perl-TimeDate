#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Date
Summary:	Manipulating timezones and parsing/formatting dates in Perl
Summary(pl):	Manipulowanie strefami czasowymi i analizowanie/formatowanie dat w Perlu
Name:		perl-TimeDate
Version:	1.16
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	b3cc35a7cabd106ac8829d2f2ff4bd9d
BuildRequires:	rpm-perlprov >= 4.1-13
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

Date::Parse udostêpnia dwie funkcje do zamiany ci±gów ASCII na
warto¶ci time: str2time(DATE [, ZONE]) oraz strptime(DATE [, ZONE]).

Time::Zone zawiera ró¿ne funkcje, s³u¿±ce do manipulowania strefami
czasowymi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Date/*.pm
%dir %{perl_vendorlib}/Date/Language
%{perl_vendorlib}/Date/Language/*.pm
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*
