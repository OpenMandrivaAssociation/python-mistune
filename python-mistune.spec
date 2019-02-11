Summary:	Markdown parser in pure Python with renderer features
Name:		python-mistune
Version:	0.8.4
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/mistune/
Source0:	https://files.pythonhosted.org/packages/2d/a4/509f6e7783ddd35482feda27bc7f72e65b5e7dc910eca4ab2164daf9c577/mistune-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Markdown parser in pure Python with renderer features

%package -n python2-mistune
Summary:	Markdown parser in pure Python with renderer features
Group:		Development/Python

%description -n python2-mistune
Markdown parser in pure Python with renderer features

%prep
%setup -qn mistune-%{version}
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/mistune.py*
%{py_sitedir}/*.egg-info
%{py_sitedir}/__pycache__/*

%files -n python2-mistune
%{py2_puresitedir}/mistune.py*
%{py2_puresitedir}/*.egg-info
