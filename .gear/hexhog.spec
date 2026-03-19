%define _unpackaged_files_terminate_build 1

Name:           hexhog
Version:        0.1.3
Release:        alt1

Summary:        A configurable hex viewer/editor
License:        MIT
Group:          File tools
URL:            https://github.com/DVDTSB/hexhog
Vcs:		https://github.com/DVDTSB/hexhog

Source:         %name-%version.tar
Source1:        vendor.tar

BuildRequires(pre): rpm-build-rust

%description
%summary.

%prep
%setup -a 1 -q
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md

%changelog
* Wed Mar 18 2026 Mikhail Kotyukhov <legend@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus.

 


