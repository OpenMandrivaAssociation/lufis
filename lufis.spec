%define	name	lufis
%define	version	0.3
%define	rel	1
%define	release	%mkrel %{rel}

Summary:	Modified LUFS daemon which uses the FUSE kernel module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		File tools
Source0:	%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/fuse/
Requires:	lufs >= 0.9.1 fuse >= 1.1
BuildRequires:	fuse-devel >= 1.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a modified LUFS daemon, which uses the FUSE kernel module.  It
is binary compatible with existing LUFS filesystems, so no
recompilation is needed.

%prep
%setup -q 

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 lufis -D $RPM_BUILD_ROOT%{_bindir}/lufis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/lufis

