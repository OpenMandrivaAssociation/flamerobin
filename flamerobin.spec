%define name	flamerobin
%define version	0.8.3
%define release	%mkrel 1

Summary:	Graphical client for Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Databases
Source0:	%{name}-%{version}-src.tar.gz
URL:		http://www.flamerobin.org/
BuildRequires:	firebird-devel >= 2.0.0.12748
BuildRequires:	wxgtku-devel >= 2.6
BuildRequires:  ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FlameRobin is a database administration tool for Firebird DBMS based on wxgtk
toolkit.

%prep
%setup -q -n %{name}-%{version}-src

%build
chmod +x configure
%configure \
	--with-wx-config=wx-config-unicode \
	--disable-debug \
	--mandir=%{buildroot}%{_mandir}/
%make -j ${NRPROC:-1}

%install
rm -rf %{buildroot}
%makeinstall

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 16x16 ./res/fricon128.png %{buildroot}%{_miconsdir}/%{name}.png
convert -size 32x32 ./res/fricon128.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 ./res/fricon128.png %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs
%{_mandir}/man1/flamerobin.1*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
