Name:           gnome-autoar
Version:        0.2.3
Release:        2%{?dist}
Summary:        Archive library

License:        LGPLv2+
URL:            https://git.gnome.org/browse/gnome-autoar
Source0:        https://download.gnome.org/sources/gnome-autoar/0.2/gnome-autoar-%{version}.tar.xz

Patch0:         extractor-Detect-conflict-also-for-directories.patch
Patch1:         extractor-Do-not-follow-symlinks-when-detecting-conf.patch
Patch2:         extractor-Do-not-allow-symlink-in-parents.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  vala

%description
gnome-autoar is a GObject based library for handling archives.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%check
make check


%files
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GnomeAutoar-0.1.typelib
%{_libdir}/girepository-1.0/GnomeAutoarGtk-0.1.typelib
%{_libdir}/libgnome-autoar-0.so.0*
%{_libdir}/libgnome-autoar-gtk-0.so.0*

%files devel
%{_includedir}/gnome-autoar-0/
%{_libdir}/pkgconfig/gnome-autoar-0.pc
%{_libdir}/pkgconfig/gnome-autoar-gtk-0.pc
%{_libdir}/*.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GnomeAutoar-0.1.gir
%{_datadir}/gir-1.0/GnomeAutoarGtk-0.1.gir
%{_datadir}/gtk-doc/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gnome-autoar-0.vapi
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.vapi


%changelog
* Thu Apr 29 2021 Ondrej Holy <oholy@redhat.com> - 0.2.3-2
- CVE-2020-36241, CVE-2021-28650: Do not allow symlink in parents (rhbz#1928701)

* Sat Mar 03 2018 Kalev Lember <klember@redhat.com> - 0.2.3-1
- Update to 0.2.3
- Drop ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-4
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Fri Mar 03 2017 Kalev Lember <klember@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Fri Feb 24 2017 Kalev Lember <klember@redhat.com> - 0.2.0-1
- Update to 0.2.0
- Build with vala support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 0.1.0-1
- Initial Fedora build
