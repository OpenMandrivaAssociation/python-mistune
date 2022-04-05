Summary:	Markdown parser in pure Python with renderer features
Name:		python-mistune
# Please don't update to >= 2.0.0 until python-m2r can work
# with newer versions.
Version:	0.8.4
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/mistune/
Source0:	https://files.pythonhosted.org/packages/source/m/mistune/mistune-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-wheel
BuildRequires:	python-pip
BuildArch:	noarch

%description
Markdown parser in pure Python with renderer features

%prep
%autosetup -p1 -n mistune-%{version}

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/mistune.py
%{py_sitedir}/__pycache__/*
%{py_sitedir}/*.dist-info
