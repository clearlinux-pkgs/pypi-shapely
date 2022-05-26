#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-shapely
Version  : 1.8.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/93/3c/cda77e57a08c49569de5bd90376c547bcb981420100adcb0f3770ed681b1/Shapely-1.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/3c/cda77e57a08c49569de5bd90376c547bcb981420100adcb0f3770ed681b1/Shapely-1.8.2.tar.gz
Summary  : Geometric objects, predicates, and operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-shapely-license = %{version}-%{release}
Requires: pypi-shapely-python = %{version}-%{release}
Requires: pypi-shapely-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : geos-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
=======
Shapely
=======
|github-actions| |coveralls|
.. |github-actions| image:: https://github.com/shapely/shapely/workflows/Tests/badge.svg?branch=maint-1.8
:target: https://github.com/shapely/shapely/actions?query=branch%3Amaint-1.8

%package license
Summary: license components for the pypi-shapely package.
Group: Default

%description license
license components for the pypi-shapely package.


%package python
Summary: python components for the pypi-shapely package.
Group: Default
Requires: pypi-shapely-python3 = %{version}-%{release}

%description python
python components for the pypi-shapely package.


%package python3
Summary: python3 components for the pypi-shapely package.
Group: Default
Requires: python3-core
Provides: pypi(shapely)

%description python3
python3 components for the pypi-shapely package.


%prep
%setup -q -n Shapely-1.8.2
cd %{_builddir}/Shapely-1.8.2
pushd ..
cp -a Shapely-1.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653601988
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-shapely
cp %{_builddir}/Shapely-1.8.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-shapely/eb14a25dd1cea155c4fa3e201dd54eee8bbb62eb
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-shapely/eb14a25dd1cea155c4fa3e201dd54eee8bbb62eb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
