%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Date
Summary:	TimeDate Perl module
Summary(cs):	Modul TimeDate pro Perl
Summary(da):	Perlmodul TimeDate
Summary(de):	TimeDate Perl Modul
Summary(es):	M�dulo de Perl TimeDate
Summary(fr):	Module Perl TimeDate
Summary(it):	Modulo di Perl TimeDate
Summary(ja):	TimeDate Perl �⥸�塼��
Summary(ko):	TimeDate �� ����
Summary(no):	Perlmodul TimeDate
Summary(pl):	Modu� Perla TimeDate
Summary(pt):	M�dulo de Perl TimeDate
Summary(pt_BR):	M�dulo Perl TimeDate
Summary(ru):	������ ��� Perl TimeDate
Summary(sv):	TimeDate Perlmodul
Summary(uk):	������ ��� Perl TimeDate
Summary(zh_CN):	TimeDate Perl ģ��
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
M�dulo de Perl TimeDate.

%description -l fr
Module Perl TimeDate.

%description -l it
Modulo di Perl TimeDate.

%description -l ja
TimeDate Perl �⥸�塼��

%description -l ko
TimeDate �� ����.

%description -l no
Perlmodul TimeDate.

%description -l pl
TimeDate zawiera modu�y: Date::Format, Date::Parse, Date::Language,
Time::Zone.

%description -l pt
M�dulo de Perl TimeDate.

%description -l pt_BR
M�dulo Perl TimeDate.

%description -l ru
������ ��� Perl TimeDate.

%description -l sv
TimeDate Perlmodul.

%description -l uk
������ ��� Perl TimeDate.

%description -l zh_CN
TimeDate Perl ģ��

%prep
%setup -q -n TimeDate-%{version}

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
