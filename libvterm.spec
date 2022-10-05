#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvterm
Version  : 0.3
Release  : 11
URL      : https://www.leonerd.org.uk/code/libvterm/libvterm-0.3.tar.gz
Source0  : https://www.leonerd.org.uk/code/libvterm/libvterm-0.3.tar.gz
Summary  : Abstract VT220/Xterm/ECMA-48 emulation library
Group    : Development/Tools
License  : MIT
Requires: libvterm-bin = %{version}-%{release}
Requires: libvterm-lib = %{version}-%{release}
Requires: libvterm-license = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the libvterm package.
Group: Binaries
Requires: libvterm-license = %{version}-%{release}

%description bin
bin components for the libvterm package.


%package dev
Summary: dev components for the libvterm package.
Group: Development
Requires: libvterm-lib = %{version}-%{release}
Requires: libvterm-bin = %{version}-%{release}
Provides: libvterm-devel = %{version}-%{release}
Requires: libvterm = %{version}-%{release}

%description dev
dev components for the libvterm package.


%package lib
Summary: lib components for the libvterm package.
Group: Libraries
Requires: libvterm-license = %{version}-%{release}

%description lib
lib components for the libvterm package.


%package license
Summary: license components for the libvterm package.
Group: Default

%description license
license components for the libvterm package.


%prep
%setup -q -n libvterm-0.3
cd %{_builddir}/libvterm-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664931393
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64 CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"


%install
export SOURCE_DATE_EPOCH=1664931393
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvterm
cp %{_builddir}/libvterm-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libvterm/9979f112bdecefd99762f24f6af76972c2a3a1a6 || :
%make_install PREFIX=/usr LIBDIR=/usr/lib64 CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unterm
/usr/bin/vterm-ctrl
/usr/bin/vterm-dump

%files dev
%defattr(-,root,root,-)
/usr/include/vterm.h
/usr/include/vterm_keycodes.h
/usr/lib64/libvterm.so
/usr/lib64/pkgconfig/vterm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvterm.so.0
/usr/lib64/libvterm.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvterm/9979f112bdecefd99762f24f6af76972c2a3a1a6
