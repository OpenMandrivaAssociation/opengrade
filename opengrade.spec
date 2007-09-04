%define name	opengrade
%define version	2.7.15
%define release	%mkrel 1

Summary:	Local and web-based gradebook
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Office
Source0:	http://www.lightandmatter.com/ogr/%name-%version.tar.gz
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
Source4:	%{name}_doc.pdf.bz2
Url:		http://www.lightandmatter.com/ogr/ogr.html
Requires:	perl-Term-ReadKey perl-Date-Calc perl-Digest-SHA1 perl-Tk
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
bzcat %SOURCE4 > %name.pdf

%build
make
mv %name.pl %name
perl -p -i -e 's|/usr/local|/usr||g' %name
chmod 755 %name

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%perl_vendorlib
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp *.pm $RPM_BUILD_ROOT/%perl_vendorlib
cp %name $RPM_BUILD_ROOT/%_bindir

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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README Copying %{name}.pdf *.gb *.cgi *.sty
%_bindir/%name
%perl_vendorlib/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
