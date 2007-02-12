Summary:	A pine--gpg/pgp interface
Summary(de.UTF-8):   Ein Interface zwischen pine und gpg/pgp
Summary(pl.UTF-8):   Interfejs pine--gpg/pgp
Name:		gpg4pine
Version:	4.2
Release:	1
License:	Free (see README)
Group:		Applications/File
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	565f0ee115275419eb40a7fa8e791789
Patch0:		%{name}-rpm.patch
URL:		http://azzie.robotics.net/
Requires:	fileutils
Requires:	textutils
Requires:	sh-utils
Requires:	grep
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
gpg4pine is a program that lets you send messages signed or encrypted
via an OpenPGP backend (GnuPG or PGP) with your favorite mailer (that
is, pine).

%description -l de.UTF-8
gpg4pine ist ein Frontend für OpenPGP-Programme (GnuPG oder PGP), der
erlaubt untergeschriebene oder verschlüsselte Nachrichte mit deinem
Lieblingsmailer (pine) zu schicken.

%description -l pl.UTF-8
gpg4pine jest programem pozwalającym na wysyłanie wiadomości
podpisanych lub zaszyfrowanych przez program OpenPGP (GnuPG lub PGP)
przy użyciu twojego ulubionego programu pocztowego (czytaj: pine'a).

%prep
%setup -q
tar xf %{name}-%{version}.tar -C ..
mv -f README README.orig
cat README.orig|sed '/^CONFIGURATION$/p'|sed \
	'/^INSTALLATION$/,/^CONFIGURATION$/d'>README
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/gpg4pine,%{_mandir}/man1}

%{__make} install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}

install gpg4pinerc $RPM_BUILD_ROOT%{_sysconfdir}/gpg4pine.defaults
cp -a language $RPM_BUILD_ROOT%{_datadir}/gpg4pine/language
touch $RPM_BUILD_ROOT%{_sysconfdir}/gpg4pine.override

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS LICENSE aliases
%doc pgp-patches
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gpg4pine
%config %{_sysconfdir}/*
%{_mandir}/*/*
