Summary:	A library for controlling and tracing dynamic memory allocations
Summary(pl):	Biblioteka do kontroli i �ledzenia dynamicznej alokacji pami�cie
Name:		dmalloc
Version:	4.8.2
Release:	2
License:	LGPL
Group:		Development/Debuggers
Source0:	http://download.sourceforge.net/dmalloc/%{name}-%{version}.tgz
# Source0-md5:	e9e961b844cc0179b7899eb7a6cd3e6a
Source1:	%{name}.1
Patch0:		%{name}-info.patch
Patch1:		%{name}-pic.patch
Patch2:		%{name}-4.8.2-pld_man.patch
URL:		http://dmalloc.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The debug memory allocation or "dmalloc" library has been designed as
a drop in replacement for the system's `malloc', `realloc', `calloc',
`free' and other memory management routines while providing powerful
debugging facilities configurable at runtime. These facilities include
such things as memory-leak tracking, fence-post write detection,
file/line number reporting, and general logging of statistics. It also
provides support for the debugging of threaded programs.

%description -l pl
Biblioteka do odpluskwiania program�w zast�puje systemowe funkcje
takie jak `malloc', `realloc', `calloc', `free' i inne funkcje do
zarz�dzania pami�ci�. Mo�liwo�ci to wykrywanie wyciek�w pami�ci,
wykrywanie zapis�w poza zaalokowanym obszarem, informowanie o
pliku/numerze linii, w kt�rej wyst�puje problem oraz generalne
statystyki. Biblioteka umo�liwia odpluskwianie program�w w�tkowych.

%package static
Summary:	Static dmalloc libraries
Summary(pl):	Biblioteki statyczne dmalloc
Group:		Development/Debuggers
Requires:	%{name} = %{version}

%description static
Static dmalloc libraries.

%description static -l pl
Biblioteki statyczne dmalloc.

%prep
%setup -q
install %{SOURCE1} .
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-cxx \
	--enable-threads \
	--enable-shlib

%{__make} dmalloc_t all light dmalloc.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1}

%{makeinstall} \
	installsl installcxx installth installinfo \
	shlibdir=$RPM_BUILD_ROOT%{_libdir} \
	incdir=$RPM_BUILD_ROOT%{_includedir}

install dmalloc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/*
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
