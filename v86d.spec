Name: v86d
Version: 0.1.10
Release: 7
Source0: %name-%version.tar.xz
Patch0: v86d-dietlibc.patch
Summary: Userspace helper for uvesafb
URL: http://github.com/mjanusz/v86d
License: GPL
Group: System/Base
BuildRequires: dietlibc

%description
Userspace helper for uvesafb

%prep
%setup -q
%apply_patches
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
