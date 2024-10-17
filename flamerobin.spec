%define name	flamerobin
%define version	0.9.2
%define release	2

Summary:	Graphical client for Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Databases
Source0:	%{name}-%{version}-src.tar.gz
URL:		https://www.flamerobin.org/
BuildRequires:	firebird-devel >= 2.0.0.12748
BuildRequires:	wxgtku-devel >= 2.6
BuildRequires:  imagemagick
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdv2011.0
+ Revision: 618290
- the mass rebuild of 2010.0 packages

  + Phillipe Makowski <makowski@mandriva.org>
    - remove old upstream src

* Sun Jul 26 2009 Phillipe Makowski <makowski@mandriva.org> 0.9.2-0mdv2010.0
+ Revision: 400208
- New upstream

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.8.3-3mdv2009.0
+ Revision: 245195
- rebuild

* Thu Jan 31 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 160873
- New upstream: 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 18 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.8.1-1mdv2008.1
+ Revision: 99959
- Fix configure permission.
- New upstream: 0.8.1
- New upstream: 0.8.0

* Tue May 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-3mdv2008.0
+ Revision: 26964
- Rebuilt against new wx stuff.


* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.7.6-2mdv2007.0
+ Revision: 100700
- rebuild

* Mon Nov 27 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.6-1mdv2007.1
+ Revision: 87367
- New upstream: 0.7.6
- Added menu icon.

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-5mdv2007.1
+ Revision: 84903
- Added BuildRequires for ImageMagick: due to convert usage.
- Rebuilt against firebird 2.0 final.

* Thu Sep 07 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.5-4mdv2007.0
+ Revision: 60258
- New upstream: 0.7.5

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.7.2-4mdv2007.0
+ Revision: 59989
- Removed old-style menu entry. The new one (.desktop) will be added later.
- Import flamerobin

* Sat Sep 02 2006 Marcelo Ricardo Leitner <mrl@mandriva.com>
- Fixed BuildRequires.
- Removed hardcoded buildrequires to libraries: they should be automatic.
- Enhanced package description.

* Thu Aug 24 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 
- change Requires to libfirebird2

* Thu Aug 17 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 
- initial release

