%include	/usr/lib/rpm/macros.perl
Summary:	TimeDate perl module
Summary(pl):	Modu� perla TimeDate
Name:		perl-TimeDate
Version:	1.08
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/TimeDate-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-12
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
TimeDate contains: Date::Format, Date::Parse, Date::Language, Time::Zone. 

%description -l pl
TimeDate zawiera modu�y: Date::Format, Date::Parse, Date::Language, Time::Zone.

%prep
%setup -q -n TimeDate-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/TimeDate
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Date/*.pm
%{perl_sitelib}/Time/*.pm
%{perl_sitearch}/auto/TimeDate

%{_mandir}/man3/*
