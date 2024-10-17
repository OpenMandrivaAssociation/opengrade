
Summary:	Local and web-based gradebook

Name:		opengrade
Version:	3.1.17
Release:	3
License:	GPLv2
Group:		Education
#Source0:	https://github.com/bcrowell/opengrade/archive/%{name}-%{version}.tar.gz
#Source0:	https://github.com/bcrowell/opengrade/releases/tag/3.1.17/opengrade-3.1.17.zip
Source0:	opengrade-3.1.17.tar.gz
Source1:	%{name}.desktop
Source2:	http://www.lightandmatter.com/ogr/%{name}_doc.pdf
Url:		https://www.lightandmatter.com/ogr/ogr.html
Requires:	tk
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
cp %{SOURCE2} %{name}.pdf
chmod -x *.sty

%build
mv %{name}.pl %{name}
perl -p -i -e 's|/usr/local|/usr||g' %{name}

%install
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_bindir}
install -m644 *.pm %{buildroot}%{perl_vendorlib}
install -m755 %name %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

#icons
mkdir -p %{buildroot}%{_liconsdir}
cp %{name}_icon.png %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
convert -resize 32x32 %{name}_icon.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 16x16 %{name}_icon.png %{buildroot}%{_miconsdir}/%{name}.png

%files
%doc README *.pdf *.gb *.cgi *.sty
%{_bindir}/%{name}
%{perl_vendorlib}/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
