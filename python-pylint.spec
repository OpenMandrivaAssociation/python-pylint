%define module	pylint
  
Summary:	Python source code analyzer
Name:		python-pylint
Version:	2.5.0
Release:	1
Group:		Development/Python
License:	Python
Url:		http://pylint.org/
# Also: https://pypi.python.org/pypi/pylint
Source0:	https://github.com/PyCQA/pylint/archive/pylint-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:  python3dist(pytest-runner)
 
%description 
A Python source code analyzer which looks for programming errors, helps
enforcing a coding standard and sniffs for some code smells.

%prep
%setup -qn %{module}-%{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{_bindir}/*
%{py_sitedir}/pylint
%{py_sitedir}/pylint*.egg-info
