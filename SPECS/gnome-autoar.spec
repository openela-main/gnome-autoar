Name:           gnome-autoar
Version:        0.4.1
Release:        2%{?dist}
Summary:        Archive library

License:        LGPLv2+
URL:            https://git.gnome.org/browse/gnome-autoar
Source0:        https://download.gnome.org/sources/gnome-autoar/0.4/gnome-autoar-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/gnome-autoar/-/issues/38
Patch0:         extractor-Fix-extraction-of-raw-format-archives.patch
Patch1:         extractor-Fix-extraction-to-root-directory.patch

# https://gitlab.gnome.org/GNOME/gnome-autoar/-/issues/34
Patch2:         tests-Do-not-left-read-only-directory-in-the-tree.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk-doc
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
%meson -Dvapi=true \
       -Dgtk_doc=true \
       -Dtests=true \
        %{nil}
%meson_build


%install
%meson_install


%check
%meson_test


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
%{_datadir}/vala/vapi/gnome-autoar-0.deps
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.deps


%changelog
* Tue Dec 07 2021 Ondrej Holy <oholy@redhat.com> - 0.4.1-2
- Fix extraction of raw format archives
- Run embedded test suite as a part of the build

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Tue Aug 10 2021 Ondrej Holy <oholy@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.3.3-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 0.3.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
