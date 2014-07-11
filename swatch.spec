%define name	swatch
%define version	3.2.3

Summary:	A utility for monitoring system logs files
Name:		swatch
Version:	3.2.3
Release:	10
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
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
perl -pi -e "s|^(INSTALLMAN1DIR\s=\s/usr/share/man/man1)|INSTALLMAN1DIR = \\$\(PREFIX\)/share/man/man1|" $RPM_BUILD_DIR/%{name}-%{version}/Makefile
%{makeinstall_std}
install tools/swatch_oldrc2newrc -D $RPM_BUILD_ROOT%{_bindir}/swatch_oldrc2newrc

mkdir -p %{buildroot}%{_sysconfdir}
bzcat %{SOURCE1} >> %{buildroot}%{_sysconfdir}/swatchrc

bzcat %{SOURCE2} >> $RPM_BUILD_DIR/%{name}-%{version}/README-Mandrake

rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/auto

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES INSTALL COPYRIGHT KNOWN_BUGS README* examples tools
%{_bindir}/swatch
%{_bindir}/swatch_oldrc2newrc
%{_mandir}/man?/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/swatchrc
%dir %{perl_vendorlib}/Swatch
%{perl_vendorlib}/Swatch/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-2mdv2011.0
+ Revision: 670252
- mass rebuild

* Wed Dec 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.3-1mdv2011.0
+ Revision: 604490
- update to 3.2.3

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.1-3mdv2010.1
+ Revision: 524139
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.1-2mdv2010.0
+ Revision: 427219
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 3.2.1-1mdv2009.1
+ Revision: 332995
- New upstream release

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.1.1-4mdv2009.0
+ Revision: 225543
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.1.1-3mdv2008.1
+ Revision: 179562
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 3.1.1-2mdv2008.0
+ Revision: 74783
- Import swatch



* Fri Jun 30 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 3.1.1-2mdv2007.0
- %%mkrel
- move tests to new %%check stage

* Thu Dec 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.1.1-1mdk
- 3.1.1

* Mon May 31 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.1-1mdk
- 3.1
- use %%makeinstall_std macro
- update %%files
- update url

* Mon Jul 21 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.0.4-3mdk
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- rebuild
- remove unpackaged files

* Fri Oct 11 2002 Amaury Amblard-Ladurantie <amaury@mandrakesoft.com> 3.0.4-2mdk
- modified default swatchrc

* Mon Jul 22 2002 Jonathan Gotti <jgotti@mandrakesoft.com> 3.0.4-1mdk
- new release

* Wed Jul 11 2001 Stefan van der Eijk <stefan@eijk.nu> 3.0.2-3mdk
- BuildRequires:	perl-devel

* Wed May 23 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.0.2-2mdk
- s/Copyright/License/;

* Fri Feb 23 2001 Gregory Letoquart <gletoquart@mandrakesoft.com> 3.0.2-1mdk
- Up to version 3.0.2

* Fri Feb 23 2001 Vincent Danen <vdanen@mandrakesoft.com> 3.0.1-2mdk
- include manpages
- include default config file
- new README-Mandrake in docs details some ways to customize and run swatch
  under Linux-Mandrake

* Mon Aug  7 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 3.0.1-1mdk
- Release 3.0.1 (merge from Redhat)

* Fri Jul 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.2-11mdk
- BM + macroszification (update patch file for man dir)
- rename specfile to remove version of filename

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 2.2-10mdk
- relocate to new mandrake group structure 

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrakes release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Tue Mar 16 1999 Preston Brown <pbrown@redhat.com>
- patched to use /var/log/messages as default, not /var/log/syslog (duh)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- fixed paths

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
