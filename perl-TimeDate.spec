%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Date
Summary:	TimeDate Perl module
Summary(cs):	Modul TimeDate pro Perl
Summary(da):	Perlmodul TimeDate
Summary(de):	TimeDate Perl Modul
Summary(es):	Módulo de Perl TimeDate
Summary(fr):	Module Perl TimeDate
Summary(it):	Modulo di Perl TimeDate
Summary(ja):	TimeDate Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	TimeDate ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul TimeDate
Summary(pl):	Modu³ Perla TimeDate
Summary(pt):	Módulo de Perl TimeDate
Summary(pt_BR):	Módulo Perl TimeDate
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl TimeDate
Summary(sv):	TimeDate Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl TimeDate
Summary(zh_CN):	TimeDate Perl Ä£¿é
Name:		perl-TimeDate
Version:	1.12
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeDate contains: Date::Format, Date::Parse, Date::Language,
Time::Zone.

%description -l cs
Modul TimeDate pro Perl.

%description -l da
Perlmodul TimeDate.

%description -l de
TimeDate Perl Modul.

%description -l es
Módulo de Perl TimeDate.

%description -l fr
Module Perl TimeDate.

%description -l it
Modulo di Perl TimeDate.

%description -l ja
TimeDate Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
TimeDate ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul TimeDate.

%description -l pl
TimeDate zawiera modu³y: Date::Format, Date::Parse, Date::Language,
Time::Zone.

%description -l pt
Módulo de Perl TimeDate.

%description -l pt_BR
Módulo Perl TimeDate.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl TimeDate.

%description -l sv
TimeDate Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl TimeDate.

%description -l zh_CN
TimeDate Perl Ä£¿é

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
