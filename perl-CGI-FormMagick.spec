#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	FormMagick
Summary:	CGI::FormMagick - easily create CGI form-based applications
Summary(pl.UTF-8):   CGI::FormMagick - łatwe tworzenie aplikacji CGI opartych na formularzach
Name:		perl-CGI-FormMagick
Version:	0.89
Release:	2
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

%description -l pl.UTF-8
FormMagick to zestaw narzędzi do łatwego tworzenia w miarę złożonych
aplikacji WWW opartych na formularzach. Pozwala programiście określić
strukturę wielostronnicowego formularza w stylu "czarodzieja" przy
użyciu XML-a, a następnie wyświetlić go przy użyciu zaledwie kilku
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

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/CGI/FormMagick/FAQ.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/FormMagick.pm
%{perl_vendorlib}/CGI/FormMagick
%{_mandir}/man3/*
