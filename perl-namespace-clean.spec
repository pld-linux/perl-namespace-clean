#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	namespace
%define		pnam	clean
%include	/usr/lib/rpm/macros.perl
Summary:	namespace::clean - Keep imports and functions out of your namespace
Name:		perl-namespace-clean
Version:	0.21
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/namespace/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eabf88eec3f5952c4bb87461b69fd1d8
URL:		http://search.cpan.org/dist/namespace-clean/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl-Package-Stash >= 0.23
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Tie::ExtraHash is present in Tie/Hash.pm package
%define		_noautoreq	perl(Tie::ExtraHash)

%description
The namespace::clean pragma will remove all previously declared or
imported symbols at the end of the current package's compile cycle.
Functions called in the package itself will still be bound by their
name, but they won't show up as methods on your class or instances.

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
%{_mandir}/man3/namespace::clean.3pm*