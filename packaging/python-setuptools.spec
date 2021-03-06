Name:       python-setuptools
Summary:    Easily build and distribute Python packages
Version:    0.6c11
Release:    2
Group:      Applications/System
License:    Python or ZPLv2.0
BuildArch:  noarch
URL:        http://pypi.python.org/pypi/setuptools
Source0:    http://pypi.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
Source1:    psfl.txt
Source2:    zpl.txt
Source1001: packaging/python-setuptools.manifest 
BuildRequires:  python-devel


%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.



%package devel
Summary:    Download, install, upgrade, and uninstall Python packages
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Requires:   python-devel

%description devel
setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package contains the components necessary to build and install software
requiring setuptools.



%prep
%setup -q -n setuptools-%{version}

%build
cp %{SOURCE1001} .
find -name '*.txt' | xargs chmod -x
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --root $RPM_BUILD_ROOT \
    --prefix %{_prefix} \
    --single-version-externally-managed

rm -rf $RPM_BUILD_ROOT%{python_sitelib}/setuptools/tests

install -p -m 0644 %{SOURCE1} %{SOURCE2} .
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.exe' | xargs rm -f
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/setuptools/command/easy_install.py


%files
%manifest python-setuptools.manifest
%{python_sitelib}/*
%exclude %{python_sitelib}/easy_install*


%files devel
%manifest python-setuptools.manifest
%{python_sitelib}/easy_install*
%{_bindir}/*

