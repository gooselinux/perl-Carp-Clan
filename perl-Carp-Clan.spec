Name:           perl-Carp-Clan
Version:        6.03
Release:        2%{?dist}
Summary:        Perl module to print improved warning messages

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Carp-Clan/
Source0:        http://www.cpan.org/authors/id/J/JJ/JJORE/Carp-Clan-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Object::Deadly)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.


%prep
%setup -q -n Carp-Clan-%{version}

# Filter unwanted Provides:
cat << EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/perl(DB)/d'
EOF

%define __perl_provides %{_builddir}/Carp-Clan-%{version}/%{name}-prov
chmod +x %{__perl_provides}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Artistic.txt Changes GNU_GPL.txt README
%{perl_vendorlib}/Carp/
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 6.03-2
- rebuild against perl 5.10.1

* Mon Oct 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 6.031
- update to 6.03

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Robert Scheck <robert@fedoraproject.org> - 6.00-4
- Really remove the no-prompt patch to avoid RPM rebuild errors

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 22 2008 Marcela Maslanova <mmaslano@redhat.com> - 6.0-1
- update to 6.0

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.9-5
- rebuild for new perl (normally)

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.9-4.1
- temporarily disable BR on Object::Deadly, tests

* Mon Nov 19 2007 Robin Norwood <rnorwood@redhat.com> - 5.9-4
- Add BR: perl-Object-Deadly now that it is included in Fedora

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 5.9-3
- Fix BuildRequires
- Various specfile cleanups

* Thu Aug 23 2007 Robin Norwood <rnorwood@redhat.com> - 5.9-2
- Update license tag.

* Mon Jun 04 2007 Robin Norwood <rnorwood@redhat.com> - 5.9-1
- Update to latest CPAN version: 5.9
- Upstream Makefile.PL prompts for user input to include
  Object::Deadly as a prerequisite.  We don't ship Object::Deadly, so
  just comment out the prompt.

* Fri Jan 26 2007 Robin Norwood <rnorwood@redhat.com> - 5.8-2
- Resolves: bz#224571 - Remove erroneous rpm 'provides' of perl(DB)

* Sat Dec 02 2006 Robin Norwood <rnorwood@redhat.com> - 5.8-1
- New version

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 5.3-2
- rebuild for perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Sat Apr 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.3-1
- First build.
