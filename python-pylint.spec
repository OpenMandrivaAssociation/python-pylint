%define module	pylint

Name:		python-pylint
Version:	4.0.5
Release:	1
Summary:	Python source code analyzer
Group:		Development/Python
License:	GPL-2.0-or-later
URL:		https://pylint.org/
# Also: https://pypi.org/project/pylint  https://github.com/pylint-dev/pylint
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
A Python source code analyzer which looks for programming errors, helps
enforcing a coding standard and sniffs for some code smells.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info
# Fix/relase upper version bounds, astroid is already released as 4.1.n, pylint
# didnt update their version pins in time for the release:
# https://github.com/pylint-dev/pylint/pull/10843
sed -i 's/astroid>=4.0.2,<=4.1.dev0/astroid>=4.1,<=4.2.dev0/g' pyproject.toml

%files
%doc README.rst
%license LICENSE
%{_bindir}/*
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
