#
# Conditional build:
%bcond_without	xft	# without xft support
#
Summary:	On Screen Display menu with lirc
Summary(pl):	Menu ekranowe obs³ugiwane pilotem
Name:		animenu
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.blackfiveservices.co.uk/projects/%{name}-%{version}.tar.gz
# Source0-md5:	0e8de8be1fc848e1623431c72667ff6e
Source1:	%{name}-examples.tar.gz
# Source1-md5:	1e8f16b3a9227072a92253db9c16bb7a
URL:		http://www.blackfiveservices.co.uk/animenu.shtml
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lirc-devel
%{?with_xft:BuildRequires:	xft-devel}
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
On Screen Display menu with lirc. Fully configurable, with directory
autoloading support and file types assotiations.

%description -l pl
Menu ekranowe obs³ugiwane pilotem. Jest w pe³ni konfigurowalne, z
mo¿liwo¶ci± konfiguracji wczytywanych podczas startu katalogów
i programów przypisanych do obs³ugi poszczególnych typów plików.

%prep
%setup  -q
cp %{SOURCE1} .
tar zxf %{SOURCE1}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	%{!?with_xft:--disable-xft}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples examplemenus
%attr(755,root,root) %{_bindir}/animenu
