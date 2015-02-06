%define name	opengrade
%define version	3.1.11
%define release	2

Summary:	Local and web-based gradebook
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2
Group:		Office
Source0:	http://www.lightandmatter.com/ogr/%name-%version.tar.gz
Source4:	http://www.lightandmatter.com/ogr/%{name}_doc.pdf
Url:		http://www.lightandmatter.com/ogr/ogr.html
Requires:	tk
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	imagemagick
Provides:	perl(FileDialogPatched)

%description
OpenGrade is software for teachers to keep track of grades.
* A variety of reports can be created.
* Grades can be uploaded to a web server, where students can have
  password-protected access to them. (see /usr/share/doc/opengrade*)
* If you use a set grading scale, you can have the software use it to compute
  letter grades automatically.
* Grades can be based on total points, or on a weighted average of scores in
  various categories such as exams and quizzes.
* You can drop the lowest grade (or the N lowest grades) from a given category.
* Students can be dropped and later reinstated without losing all their grades.
* Gradebook files can be automatically backed up on a web server.
* There is support for extra-credit categories, and for categories that don't
  count towards the student's grade.
* Gradebook files are password-protected with a digital watermark, so you can
  detect tampering.
* Gradebook files are in a plain-text format, which makes it easy to work with
  them using Unix utilities. 

%prep
%setup -q
cp %SOURCE4 %{name}.pdf

%build
mv %name.pl %name
perl -p -i -e 's|/usr/local|/usr||g' %name

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%perl_vendorlib
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m644 *.pm $RPM_BUILD_ROOT/%perl_vendorlib
install -m755 %name $RPM_BUILD_ROOT/%_bindir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenGrade
Comment=Digital Gradebook
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp opengrade_icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -resize 32x32 opengrade_icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -resize 16x16 opengrade_icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

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

%files
%defattr(-,root,root)
%doc README *.pdf *.gb *.cgi *.sty
%_bindir/%name
%perl_vendorlib/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Sun Jan 09 2011 Funda Wang <fwang@mandriva.org> 3.1.11-1mdv2011.0
+ Revision: 630830
- update to new version 3.1.11

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 3.1.10-1mdv2011.0
+ Revision: 604303
- update to new version 3.1.10

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 3.1.7-1mdv2011.0
+ Revision: 504710
- new version 3.1.7

* Mon Nov 16 2009 Funda Wang <fwang@mandriva.org> 3.1.5-1mdv2010.1
+ Revision: 466409
- new version 3.1.5

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 3.1.4-1mdv2010.0
+ Revision: 451966
- New version 3.1.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 3.1.1-1mdv2009.1
+ Revision: 337386
- update to new version 3.1.1

* Sun Feb 01 2009 Funda Wang <fwang@mandriva.org> 3.1.0-1mdv2009.1
+ Revision: 336081
- new version 3.1.0

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 3.0.2-1mdv2009.1
+ Revision: 330558
- update to new version 3.0.2

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 3.0.0-1mdv2009.1
+ Revision: 328221
- New version 3.0.0

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 2.9.4-1mdv2009.1
+ Revision: 328177
- update to new version 2.9.4

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 2.9.3-1mdv2009.1
+ Revision: 326084
- update to new version 2.9.3

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 2.9.2-1mdv2009.1
+ Revision: 324507
- New version 2.9.2

* Thu Jan 01 2009 Funda Wang <fwang@mandriva.org> 2.9.0-1mdv2009.1
+ Revision: 323170
- New version 2.9.0

* Tue Dec 02 2008 Funda Wang <fwang@mandriva.org> 2.8.3-1mdv2009.1
+ Revision: 308966
- new version 2.8.3

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.8.2-2mdv2009.0
+ Revision: 268351
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 2.8.2-1mdv2009.0
+ Revision: 208302
- New version 2.8.2

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 2.8.1-1mdv2008.1
+ Revision: 161420
- update to new version 2.8.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Funda Wang <fwang@mandriva.org> 2.7.15-1mdv2008.0
+ Revision: 78945
- spec file clean
- New version 2.7.15

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Wed Oct 25 2006 Lenny Cartier <lenny@mandriva.com> 2.7.13-1mdv2007.0
+ Revision: 72282
- Update to 2.7.13
- Import opengrade

