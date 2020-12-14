#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Shapely
Version  : 1.7.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/44/ec/4eddbf9d17a917c51fb4ad159aa7137f506681e91ab559cf87d120e1d78d/Shapely-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/ec/4eddbf9d17a917c51fb4ad159aa7137f506681e91ab559cf87d120e1d78d/Shapely-1.7.0.tar.gz
Summary  : Geometric objects, predicates, and operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Shapely-license = %{version}-%{release}
Requires: Shapely-python = %{version}-%{release}
Requires: Shapely-python3 = %{version}-%{release}
Requires: numpy
BuildRequires : buildreq-distutils3
BuildRequires : geos-dev
BuildRequires : numpy
BuildRequires : python3-dev

%description
Shapely
        =======
        
        |travis| |appveyor| |coveralls|

%package license
Summary: license components for the Shapely package.
Group: Default

%description license
license components for the Shapely package.


%package python
Summary: python components for the Shapely package.
Group: Default
Requires: Shapely-python3 = %{version}-%{release}
Provides: shapely-python

%description python
python components for the Shapely package.


%package python3
Summary: python3 components for the Shapely package.
Group: Default
Requires: python3-core
Provides: pypi(shapely)

%description python3
python3 components for the Shapely package.


%prep
%setup -q -n Shapely-1.7.0
cd %{_builddir}/Shapely-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596045471
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Shapely
cp %{_builddir}/Shapely-1.7.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/Shapely/eb14a25dd1cea155c4fa3e201dd54eee8bbb62eb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Shapely/eb14a25dd1cea155c4fa3e201dd54eee8bbb62eb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
