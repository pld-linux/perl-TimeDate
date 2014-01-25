#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Date
Summary:	Manipulating timezones and parsing/formatting dates in Perl
Summary(pl.UTF-8):	Manipulowanie strefami czasowymi i analizowanie/formatowanie dat w Perlu
Name:		perl-TimeDate
Version:	2.30
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/G/GB/GBARR/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	b1d91153ac971347aee84292ed886c1c
URL:		http://search.cpan.org/dist/TimeDate/
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

%description -l pl.UTF-8
TimeDate zawiera moduły: Date::Format, Date::Parse i Time::Zone.

Date::Format dostarcza funkcje, formatujące datę w ciągi ASCII.
Funkcje te odpowiadają strftime() i ctime() z biblioteki C.

Date::Parse udostępnia dwie funkcje do zamiany ciągów ASCII na
wartości time: str2time(DATE [, ZONE]) oraz strptime(DATE [, ZONE]).

Time::Zone zawiera różne funkcje, służące do manipulowania strefami
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
%{perl_vendorlib}/Date/Format.pm
%{perl_vendorlib}/Date/Language.pm
%{perl_vendorlib}/Date/Parse.pm
%dir %{perl_vendorlib}/Date/Language
%{perl_vendorlib}/Date/Language/*.pm
%{perl_vendorlib}/Time/Zone.pm
%{_mandir}/man3/Date::Format.3pm*
%{_mandir}/man3/Date::Language.3pm*
%{_mandir}/man3/Date::Language::Bulgarian.3pm*
%{_mandir}/man3/Date::Language::Hungarian.3pm*
%{_mandir}/man3/Date::Parse.3pm*
%{_mandir}/man3/Time::Zone.3pm*
