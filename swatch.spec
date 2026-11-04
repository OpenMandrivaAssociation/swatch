%define name	swatch
%define version	3.2.4

Summary:	A utility for monitoring system logs files
Name:		swatch
Version:	3.2.4
Release:	2
License:	GPLv2
Group:		Monitoring
Source0:	%{name}-%{version}.tar.gz
URL:		https://swatch.sourceforge.net/
Source1:	swatchrc.bz2
Source2:	README-mandrake.bz2
BuildRequires:	make
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
# 3.2.4 ships the program as swatchdog and unpacks as swatchdog-%{version}.
%setup -q -n swatchdog-%{version}
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
perl -pi -e "s|^(INSTALLMAN1DIR\s=\s/usr/share/man/man1)|INSTALLMAN1DIR = \\$\(PREFIX\)/share/man/man1|" $RPM_BUILD_DIR/swatchdog-%{version}/Makefile
%{makeinstall_std}
ln -s swatchdog $RPM_BUILD_ROOT%{_bindir}/swatch
# man follows the upstream rename; keep the historical name working.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
echo '.so man1/swatchdog.1' > $RPM_BUILD_ROOT%{_mandir}/man1/swatch.1

mkdir -p %{buildroot}%{_sysconfdir}
bzcat %{SOURCE1} >> %{buildroot}%{_sysconfdir}/swatchrc

bzcat %{SOURCE2} >> $RPM_BUILD_DIR/swatchdog-%{version}/README-Mandrake

rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/auto

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES INSTALL COPYRIGHT KNOWN_BUGS README* examples
%{_bindir}/swatch
%{_bindir}/swatchdog
%{_mandir}/man?/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/swatchrc
%dir %{perl_vendorlib}/Swatchdog
%{perl_vendorlib}/Swatchdog/*
