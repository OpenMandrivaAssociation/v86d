%define debug_package %{nil}

Name: v86d
Version: 0.1.10
Release: 13
Source0: %name-%version.tar.xz
Patch0: v86d-dietlibc.patch
Summary: Userspace helper for uvesafb
URL: https://github.com/mjanusz/v86d
License: GPL
Group: System/Base
BuildRequires: dietlibc

%description
Userspace helper for uvesafb

%prep
%setup -q
%autopatch -p1
./configure --with-x86emu
sed -i -e "s|-Wall -g -O2|$RPM_OPT_FLAGS -Os|g" Makefile

%build
# Makefile isn't smp clean
make KDIR=%_prefix CC="diet gcc -Os -D__KERNEL_STRICT_NAMES"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
/sbin/v86d
