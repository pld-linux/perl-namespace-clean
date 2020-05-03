#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	namespace
%define		pnam	clean
Summary:	namespace::clean - Keep imports and functions out of your namespace
Summary(pl.UTF-8):	namespace::clean - trzymanie symboli importowanych i funkcji poza przestrzenią nazw
Name:		perl-namespace-clean
Version:	0.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/namespace/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cba97f39ef7e594bd8489b4fdcddb662
URL:		https://metacpan.org/release/namespace-clean
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-B-Hooks-EndOfScope >= 0.13
BuildRequires:	perl-Package-Stash >= 0.23
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Requires:	perl-B-Hooks-EndOfScope >= 0.13
Requires:	perl-Package-Stash >= 0.23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Tie::ExtraHash and Tie::StdHash are present in Tie/Hash.pm package
%define		_noautoreq_perl	Tie::ExtraHash Tie::StdHash

%description
The namespace::clean pragma will remove all previously declared or
imported symbols at the end of the current package's compile cycle.
Functions called in the package itself will still be bound by their
name, but they won't show up as methods on your class or instances.

%description -l pl.UTF-8
Reguła namespace::clean usuwa wszystkie uprzednio zadeklarowane lub
zaimportowane symbole na końcu cyklu kompilacji bieżącego pakietu.
Funkcje wywoływane w samym pakiecie pozostaną nadal dowiązane po ich
nazwach, ale nie będą dostępne jako metody w klasach ani instancjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	--skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/namespace
%{perl_vendorlib}/namespace/clean.pm
%{perl_vendorlib}/namespace/clean
%{_mandir}/man3/namespace::clean.3pm*
