#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-parso
Version  : 0.8.3
Release  : 63
URL      : https://files.pythonhosted.org/packages/a2/0e/41f0cca4b85a6ea74d66d2226a7cda8e41206a624f5b330b958ef48e2e52/parso-0.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/0e/41f0cca4b85a6ea74d66d2226a7cda8e41206a624f5b330b958ef48e2e52/parso-0.8.3.tar.gz
Summary  : A Python Parser
Group    : Development/Tools
License  : BSD-3-Clause MIT Python-2.0
Requires: pypi-parso-license = %{version}-%{release}
Requires: pypi-parso-python = %{version}-%{release}
Requires: pypi-parso-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
parso - A Python Parser
        ###################################################################

%package license
Summary: license components for the pypi-parso package.
Group: Default

%description license
license components for the pypi-parso package.


%package python
Summary: python components for the pypi-parso package.
Group: Default
Requires: pypi-parso-python3 = %{version}-%{release}

%description python
python components for the pypi-parso package.


%package python3
Summary: python3 components for the pypi-parso package.
Group: Default
Requires: python3-core
Provides: pypi(parso)

%description python3
python3 components for the pypi-parso package.


%prep
%setup -q -n parso-0.8.3
cd %{_builddir}/parso-0.8.3
pushd ..
cp -a parso-0.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392969
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-parso
cp %{_builddir}/parso-0.8.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-parso/b1a7c6c0bf49fd5b62cca57a802166f291273c9a
cp %{_builddir}/parso-0.8.3/docs/_themes/flask/LICENSE %{buildroot}/usr/share/package-licenses/pypi-parso/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/parso-0.8.3/test/normalizer_issue_files/LICENSE %{buildroot}/usr/share/package-licenses/pypi-parso/f71a77bff7a0853ddf32ea962ef8582fe808d9f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-parso/b1a7c6c0bf49fd5b62cca57a802166f291273c9a
/usr/share/package-licenses/pypi-parso/d0eff60551064b040266867c393e035d747b0ae5
/usr/share/package-licenses/pypi-parso/f71a77bff7a0853ddf32ea962ef8582fe808d9f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
