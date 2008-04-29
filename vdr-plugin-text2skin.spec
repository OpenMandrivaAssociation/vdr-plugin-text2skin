
%define plugin	text2skin
%define name	vdr-plugin-%plugin
%define version	1.1
%define cvsrev	20060904
%define rel	9
%define release	%mkrel 0.%cvsrev.%rel

Summary:	VDR plugin: Loader for text-based skins
Name:		%name
Version:	%version
Release:	%release
Group:		Video
License:	GPL
URL:		http://www.magoa.net/linux/
# http://text2skin.vdr-developer.org/
Source:		vdr-%plugin-%cvsrev.tar.bz2
Patch1:		vdr-text2skin-notext.diff
Patch2:		94_text2skin-1.1-cvs_ext-0.10-vdr-1.5.4.dpatch
Patch3:		95_text2skin-1.1-cvs-locale.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	freetype2-devel libMagick-devel
Requires:	vdr-abi = %vdr_abi

%description
This plugin is designed to load and interpret a set of files describing the
layout of the On Screen Display and to make this "Skin" available to VDR via
Setup -> OSD in the main menu. Of course it is possible to load more than one
text-based skin this way and to choose between them while running VDR. All
skins may be themeable (you can create your own color-theme) and translateable
as the author of the skin wishes.

%prep
%setup -q -n %plugin
find -type d -name 'CVS' -print0 | xargs -0 rm -rf
%patch1 -p1 -b .ft22
%patch2 -p1
%patch3 -p1
# (04/2008) Fixes build
sed -i 's,-lMagick ,,' Makefile
%vdr_plugin_prep

%build
VDR_PLUGIN_FLAGS="%vdr_plugin_flags $(pkg-config --cflags ImageMagick++)"
%vdr_plugin_build

%install
rm -rf %{buildroot}

%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} 	%{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY CONTRIBUTORS
%doc contrib Docs/*
%{_vdr_plugin_datadir}/%{plugin}
%{_vdr_plugin_cfgdir}/%{plugin}

