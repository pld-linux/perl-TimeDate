%include	/usr/lib/rpm/macros.perl
Summary:	TimeDate perl module
Summary(pl):	Modu³ perla TimeDate
Name:		perl-TimeDate
Version:	1.10
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/TimeDate-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeDate contains: Date::Format, Date::Parse, Date::Language,
Time::Zone.

%description -l pl
TimeDate zawiera modu³y: Date::Format, Date::Parse, Date::Language,
Time::Zone.

%prep
%setup -q -n TimeDate-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Date/*.pm
%{perl_sitelib}/Time/*.pm
%{_mandir}/man3/*
