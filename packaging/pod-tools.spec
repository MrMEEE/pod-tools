# ── Suppress debuginfo (scripts have no ELF binaries) ─────────────────────────
%global debug_package %{nil}

Name:           pod-tools
Version:        %{version_string}
Release:        1%{?dist}
Summary:        Collection of Podman helper scripts
License:        MIT
URL:            https://github.com/MrMEEE/pod-tools
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
A collection of helper scripts for working with Podman containers.

Scripts are installed into /usr/bin/ and are ready to use after installation.

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
find scripts/ -maxdepth 1 -type f -exec install -m 0755 {} %{buildroot}%{_bindir}/ \;

%files
%{_bindir}/*

%changelog

* Thu May 28 2026 Release Bot <release@pod-tools> - 0.1.2-1
- Release 0.1.2

* Thu May 28 2026 Release Bot <release@pod-tools> - 0.1.1-1
- Release 0.1.1
