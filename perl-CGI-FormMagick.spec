#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	FormMagick
Summary:	CGI::FormMagick - easily create CGI form-based applications
Summary(pl):	CGI::FormMagick - ³atwe tworzenie aplikacji CGI opartych na formularzach
Name:		perl-CGI-FormMagick
Version:	0.89
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f40a7de9af1e2484d76240896174774e
# no tests
#BuildRequires:	perl-Test-Inline >= 0.15
#BuildRequires:	perl-Test-Simple >= 0.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# R, not BR - versioned deps are not generated, and there are no tests for BR
Requires:	perl-CGI-Persistent >= 0.21
Requires:	perl-Class-ParamParser >= 1.041
Requires:	perl-I18N-LangTags >= 0.13
Requires:	perl-Mail-RFC822-Address
Requires:	perl-Persistence-Object-Simple >= 0.47
Requires:	perl-Text-Iconv >= 1.2
Requires:	perl-Text-Template >= 1.40
Requires:	perl-XML-Parser >= 2.30
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FormMagick is a toolkit for easily building fairly complex form-based
web applications. It allows the developer to specify the structure of a
multi-page "wizard" style form using XML, then display that form using
only a few lines of Perl.

%description -l pl
FormMagick to zestaw narzêdzi do ³atwego tworzenia w miarê z³o¿onych
aplikacji WWW opartych na formularzach. Pozwala programi¶cie okre¶liæ
strukturê wielostronnicowego formularza w stylu "czarodzieja" przy
u¿yciu XML-a, a nastêpnie wy¶wietliæ go przy u¿yciu zaledwie kilku
linii kodu w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/FormMagick.pm
%{perl_vendorlib}/CGI/FormMagick
%{_mandir}/man3/*
