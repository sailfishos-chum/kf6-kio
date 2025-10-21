%global  kf_version 6.7.0

Name:    kf6-kio
Version: 6.18.0
Release: 0%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for filesystem abstraction

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: %{name}-%{version}.tar.bz2
Patch0:  sailfishos-no-kcrash.patch


BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

# General deps:
BuildRequires:  kf6-kconfig-devel
BuildRequires:  pkgconfig(KF6CoreAddons)
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kservice-devel
#BuildRequires:  pkgconfig(KF6DocTools)
BuildRequires:  kf6-solid-devel
#BuildRequires:  pkgconfig(KF6Crash)

# If not KIOCORE_ONLY:
BuildRequires:  pkgconfig(KF6WindowSystem)

# If not KIOGUI_ONLY:
BuildRequires:  kf6-kbookmarks-devel
BuildRequires:  kf6-kcompletion-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kitemviews-devel
BuildRequires:  kf6-kjobwidgets-devel
BuildRequires:  kf6-kwidgetsaddons-devel


BuildRequires:  kf6-kauth-devel
#BuildRequires:  pkgconfig(KF6Auth)

#BuildRequires:  pkgconfig(KF6KDED)

#BuildRequires:  pkgconfig(KF6Archive)
#BuildRequires:  switcheroo-control
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-knotifications-devel
#BuildRequires:  pkgconfig(KF6Wallet)
BuildRequires:  kf6-kxmlgui-devel

BuildRequires:  pkgconfig(libacl)
#%%if !0%%{?flatpak}
#BuildRequires:  libxml2-devel
#BuildRequires:  libxslt-devel
#%%endif
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)

BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)


BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(Qt6UiPlugin)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(Qt6Core5Compat)

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

#Requires: kf6-kded

%description
KDE Frameworks 6 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
#Requires:       pkgconfig(KF6Bookmarks)
#Requires:       kf6-kbookmarks-devel
#Requires:       pkgconfig(KF6Completion)
#Requires:       pkgconfig(KF6Config)
Requires:       kf6-kconfig-devel
Requires:       pkgconfig(KF6CoreAddons)
#Requires:       pkgconfig(KF6ItemViews)
Requires:       kf6-kitemviews-devel
#Requires:       pkgconfig(KF6JobWidgets)
#Requires:       pkgconfig(KF6Service)
Requires:       kf6-kservice-devel
#Requires:       pkgconfig(KF6Solid)
Requires:       kf6-solid-devel
#Requires:       pkgconfig(KF6XmlGui)
Requires:       kf6-kxmlgui-devel
Requires:       pkgconfig(KF6WindowSystem)
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

#%%package        doc
#Summary:        Documentation files for %%{name}
#Requires:       %%{name}-core = %%{version}-%%{release}
#BuildArch:      noarch
#%%description    doc
#Documentation for %%{name}.

%package        core
Summary:        Core components of the KIO Framework
%{?kf6_kinit_requires}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
#Requires:       kf6-filesystem
Recommends:     switcheroo-control
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
## org.kde.klauncher6 service referenced from : widgets/krun.cpp
## included here for completeness, even those -core already has a dependency.
%{?kf6_kinit_requires}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    gui
%{summary}.

#%%package        qch-doc
#Summary:        Developer Documentation files for %%{name}
#BuildArch:      noarch
#%%description    qch-doc
#Developer Documentation files for %%{name} for use with KDevelop or QtCreator.

#%%package        html
#Summary:        Developer Documentation files for %%{name}
#BuildArch:      noarch
#%%description    html
#Developer Documentation files for %%{name} in HTML format

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6 \
  -DBUILD_DESIGNERPLUGIN=OFF \
  -DUSE_DBUS=ON \
  -DWITH_X11=OFF \
  -DWITH_WAYLAND=ON \
  %{nil}

%cmake_build

%install
%cmake_install

%find_lang kio6

%files
%license LICENSES/*.txt
%doc README.md

%files core -f kio6.lang
#%%{_kf6_libexecdir}/kioexec
%{_kf6_libexecdir}/kiod6
%{_kf6_libexecdir}/kioworker
%{_kf6_bindir}/ktelnetservice6
%{_kf6_bindir}/ktrash6
%{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kded/
%{_kf6_plugindir}/kiod/
#%%{_kf6_plugindir}/kio_dnd/
#%%{_kf6_datadir}/kf6/searchproviders/*.desktop
%{_kf6_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.kde.*.service
%{_kf6_datadir}/qlogging-categories6/*categories

%files core-libs
%{_kf6_libdir}/libKF6KIOCore.so.*

%files gui
%{_kf6_libdir}/libKF6KIOGui.so.*

%files widgets
%dir %{_kf6_plugindir}/urifilters/
%{_kf6_plugindir}/urifilters/*.so
#%%{_kf6_libdir}/libkuriikwsfiltereng_private.so.*

%files widgets-libs
%{_kf6_libdir}/libKF6KIOWidgets.so.*

%files file-widgets
%{_kf6_libdir}/libKF6KIOFileWidgets.so.*

%files devel
%{_kf6_includedir}/*
%{_kf6_libdir}/*.so
%{_kf6_libdir}/cmake/KF6KIO/
%{_kf6_datadir}/kdevappwizard/templates/kioworker6.tar.bz2
#%%{_kf6_qtplugindir}/designer/kio6widgets.so

#%%files qch-doc
#%%{_qt6_docdir}/*.qch

#%%files html
#%%{_qt6_docdir}/*/*
#%%exclude %%{_qt6_docdir}/*/*.tags
#%%exclude %%{_qt6_docdir}/*/*.index
 
