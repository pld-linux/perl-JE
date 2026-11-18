#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	JE
Summary:	JE - Pure-Perl ECMAScript (JavaScript) Engine
Name:		perl-JE
Version:	0.066
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JE/%{pdir}-%{version}.tar.gz
# Source0-md5:	63ed03bd82fbae5021a7f3f200c18799
Patch0:		%{name}-goto-into-construct.patch
URL:		http://search.cpan.org/dist/JE/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-TimeDate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JE, short for JavaScript::Engine (imaginative, isn't it?), is a
pure-Perl JavaScript engine.

%prep
%setup -q -n %{pdir}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorlib}/JE.pm
%{perl_vendorlib}/JE
%{perl_vendorlib}/JavaScript/Engine.pm
%{_mandir}/man3/JE.3pm*
%{_mandir}/man3/JE::*.3pm*
%{_mandir}/man3/JavaScript::Engine.3pm*
