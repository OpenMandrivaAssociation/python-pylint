%define module	pylint
  
Summary:	Python source code analyzer
Name:		python-pylint
Version:	3.0.2
Release:	1
Group:		Development/Python
License:	Python
Url:		http://pylint.org/
# Also: https://pypi.python.org/pypi/pylint
Source0:	https://files.pythonhosted.org/packages/source/p/pylint/pylint-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(pytest-runner)
BuildRequires:  python%{pyver}dist(wheel)
 
%description 
A Python source code analyzer which looks for programming errors, helps
enforcing a coding standard and sniffs for some code smells.

%prep
%autosetup -p1 -n %{module}-%{version}
  
%build
%py_build

%install 
%py_install

%files
%{_bindir}/*
%{py_sitedir}/pylint
%{py_sitedir}/pylint*.dist-info
