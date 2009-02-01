#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	namespace
%define	pnam	clean
Summary:	namespace::clean - Keep imports and functions out of your namespace
#Summary(pl.UTF-8):	
Name:		perl-namespace-clean
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/namespace/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8edfbf0ccd9cb0557e7d0c5366d9f1f1
URL:		http://search.cpan.org/dist/namespace-clean/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(B::Hooks::EndOfScope)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The namespace::clean pragma will remove all previously declared or
imported symbols at the end of the current package's compile cycle.
Functions called in the package itself will still be bound by their
name, but they won't show up as methods on your class or instances.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/namespace/
%{_mandir}/man3/*
