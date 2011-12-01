%define name	swatch
%define version	3.2.3

Summary:	A utility for monitoring system logs files
Name:		swatch
Version:	3.2.3
Release:	%mkrel 2
License:	GPLv2
Group:		Monitoring
Source0:	%{name}-%{version}.tar.gz
URL:		http://swatch.sourceforge.net/
Source1:	swatchrc.bz2
Source2:	README-mandrake.bz2
BuildRequires:	perl-devel perl-File-Tail perl-Date-Calc perl-Time-HiRes perl-TimeDate
Requires:	perl perl-File-Tail perl-Date-Calc perl-Time-HiRes perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Swatch utility monitors system log files, filters out unwanted data
and takes specified actions (i.e., sending email, executing a script,
etc.) based upon what it finds in the log files.

Install the swatch package if you need a program that will monitor log
files and alert you in certain situations.

%prep
%setup -q
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}
eval `perl '-V:installarchlib'`
mkdir -p %{buildroot}/$installarchlib
perl -pi -e "s|^(INSTALLMAN1DIR\s=\s/usr/share/man/man1)|INSTALLMAN1DIR = \\$\(PREFIX\)/share/man/man1|" %{_builddir}/%{name}-%{version}/Makefile
%{makeinstall_std}
install tools/swatch_oldrc2newrc -D %{buildroot}%{_bindir}/swatch_oldrc2newrc

mkdir -p %{buildroot}%{_sysconfdir}
bzcat %{SOURCE1} >> %{buildroot}%{_sysconfdir}/swatchrc

bzcat %{SOURCE2} >> %{_builddir}/%{name}-%{version}/README-Mandrake

rm -rf %{buildroot}%{perl_vendorlib}/auto

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL COPYRIGHT KNOWN_BUGS README* examples tools
%{_bindir}/swatch
%{_bindir}/swatch_oldrc2newrc
%{_mandir}/man?/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/swatchrc
%dir %{perl_vendorlib}/Swatch
%{perl_vendorlib}/Swatch/*
