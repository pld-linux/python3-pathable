#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-pathable.spec)

Summary:	Object-oriented paths
Summary(pl.UTF-8):	Ścieżki zorientowane obiektowo
Name:		python-pathable
# keep 0.3.x here for python2 support
Version:	0.3.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathable/
Source0:	https://files.pythonhosted.org/packages/source/p/pathable/pathable-%{version}.tar.gz
# Source0-md5:	46ee786643c28b3d184327c13186879e
URL:		https://pypi.org/project/pathable/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-pathable
Summary:	Object-oriented paths
Summary(pl.UTF-8):	Ścieżki zorientowane obiektowo
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pathable
Object-oriented paths. Key features:
- Traverse resources like paths
- Access resources on demand with separate accessor layer

%description -n python3-pathable -l pl.UTF-8
Ścieżki zorientowane obiektowo. Główne możliwości:
- przechodzenie zasobów jak ścieżek
- dostęp do zasobów na żądanie z osobną warstwą dostępową

%prep
%setup -q -n pathable-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/pathable
%{py_sitescriptdir}/pathable-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pathable
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pathable
%{py3_sitescriptdir}/pathable-%{version}-py*.egg-info
%endif
