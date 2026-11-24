Summary:	Object-oriented paths
Summary(pl.UTF-8):	Ścieżki zorientowane obiektowo
Name:		python3-pathable
Version:	0.6.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathable/
Source0:	https://files.pythonhosted.org/packages/source/p/pathable/pathable-%{version}.tar.gz
# Source0-md5:	1515f586cea1c43aa94d2049ff111c1d
URL:		https://pypi.org/project/pathable/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented paths. Key features:
- Traverse resources like paths
- Access resources on demand with separate accessor layer

%description -l pl.UTF-8
Ścieżki zorientowane obiektowo. Główne możliwości:
- przechodzenie zasobów jak ścieżek
- dostęp do zasobów na żądanie z osobną warstwą dostępową

%prep
%setup -q -n pathable-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/pathable
%{py3_sitescriptdir}/pathable-%{version}.dist-info
