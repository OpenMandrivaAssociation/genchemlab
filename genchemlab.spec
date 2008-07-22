%define name	genchemlab
%define version	1.0
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	General Chemistry Lab Simulator - "GenChemLab"
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/genchemlab/genchemlab-%{version}.tar.bz2
URL:		http://genchemlab.sourceforge.net/
License:	GPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel qt4-devel
BuildRequires:  MesaGLU-devel
BuildRequires:  ImageMagick

%description
GenChemLab is an OpenGL-based application intended to simulate several common
general chemistry exercises. It is meant to be used to help students prepare
for actual lab experience. It could also be used in cases where laboratory
facilites are not accessible, for instance in K-12 schools or home schooling.

At present, supported experiments include titration, calorimetry, freezing
point depression, vapor pressure, and spectrophotometry. 

%prep
%setup -q

%build
%configure2_5x
perl -p -i -e 's/usr\/X11R6\/lib\/qt/usr\/X11R6\/lib/g' program/Makefile
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=GenChemLab
Comment=Chemistry Lab Simulations
Categories=Science;Chemistry;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 program/genchemlab.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 program/genchemlab.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 program/genchemlab.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.txt doc/*
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

