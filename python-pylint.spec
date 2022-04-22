%define module	pylint
  
Summary:	Python source code analyzer
Name:		python-pylint
Version:	2.9.6
Release:	2
Group:		Development/Python
License:	Python
Url:		http://pylint.org/
# Also: https://pypi.python.org/pypi/pylint
Source0:	https://github.com/PyCQA/pylint/archive/pylint-%{version}.tar.gz
# Not a elegant way but should works until we import few new deps and upgrade rest to match pylint requires
Patch0:   pylint-2.6.0-allow-to-work-with-astroid-2.5.8.patch
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(wheel)
 
%description 
A Python source code analyzer which looks for programming errors, helps
enforcing a coding standard and sniffs for some code smells.

%prep
%setup -qn %{module}-%{version}
%autopatch -p1
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{_bindir}/*
%{py_sitedir}/pylint
%{py_sitedir}/pylint*.egg-info
