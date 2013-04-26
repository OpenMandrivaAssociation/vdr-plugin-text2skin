
%define plugin	text2skin
%define name	vdr-plugin-%plugin
%define version	1.3.1
%define snap	0
%define rel	4

%define debug_package %{nil}

%if %snap
%define release	%mkrel 0.%snap.%rel
%else
%define release	%mkrel %rel
%endif

Summary:	VDR plugin: Loader for text-based skins
Name:		%name
Version:	%version
Release:	%release
Group:		Video
License:	GPL+
URL:		http://projects.vdr-developer.org/projects/list_files/plg-text2skin
%if %snap
Source:		vdr-%plugin-%snap.tar.bz2
%else
Source:		vdr-%plugin-%version.tgz
%endif
Patch0:		text2skin-imagemagick-6.6.2.patch
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	pkgconfig(freetype2-devel) imagemagick-devel
Requires:	vdr-abi = %vdr_abi

%description
This plugin is designed to load and interpret a set of files describing the
layout of the On Screen Display and to make this "Skin" available to VDR via
Setup -> OSD in the main menu. Of course it is possible to load more than one
text-based skin this way and to choose between them while running VDR. All
skins may be themeable (you can create your own color-theme) and translateable
as the author of the skin wishes.

%prep
%setup -q -n %plugin-%version
%apply_patches
%vdr_plugin_prep

%build
%vdr_plugin_build

%install

%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
ln -s %{vdr_plugin_datadir}/%{plugin} %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY CONTRIBUTORS
%doc contrib Docs/*
%{vdr_plugin_datadir}/%{plugin}
%{vdr_plugin_cfgdir}/%{plugin}



%changelog
* Sat Aug 14 2010 Anssi Hannula <anssi@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 569796
- fix build with imagemagick 6.6.2+ (imagemagick-6.6.2.patch)
- new version
- new URL
- drop patches, fixed upstream

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 1.1-0.20060904.12mdv2011.0
+ Revision: 553586
- rebuild

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.11mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- adapt for vdr compilation flags handling changes, bump buildrequires

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.10mdv2009.1
+ Revision: 359784
- fix types (types.patch)
- rebuild for new vdr
- use backward-compatible pkg-config call for libmagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.9mdv2009.0
+ Revision: 197987
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.8mdv2009.0
+ Revision: 197733
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt for api changes of VDR 1.5.4 (P2 from e-tobi)
- adapt to gettext i18n of VDR 1.6 (P3 from e-tobi)
- fix build with recent libmagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new imagemagick libs

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.6mdv2008.1
+ Revision: 145221
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.5mdv2008.1
+ Revision: 103222
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.4mdv2008.0
+ Revision: 50056
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.3mdv2008.0
+ Revision: 42139
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.2mdv2008.0
+ Revision: 22712
- rebuild for new vdr

* Fri Apr 20 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20060904.1mdv
+ Revision: 16274
- new snapshot


* Sun Feb 18 2007 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.12mdv2007.0
+ Revision: 122357
- rebuild for new ImageMagick

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.11mdv2007.1
+ Revision: 90978
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.10mdv2007.1
+ Revision: 74089
- rebuild for new vdr
- Import vdr-plugin-text2skin

* Sat Sep 09 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.9mdv2007.0
- rebuild for new imagemagick

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.8mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.7mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.6mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.5mdv2007.0
- rebuild for new vdr

* Thu Jul 13 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.4mdv2007.0
- patch1: fix fonts with libfreetype 2.2

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.3mdv2007.0
- use _ prefix for system path macros

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.2mdv2007.0
- rebuild for new vdr

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 1.1-0.20051217.1mdv2007.0
- initial Mandriva release

