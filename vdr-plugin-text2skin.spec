
%define plugin	text2skin
%define name	vdr-plugin-%plugin
%define version	1.3.1
%define snap	0
%define rel	1

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
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	freetype2-devel imagemagick-devel
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
rm -rf %{buildroot}

%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

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

