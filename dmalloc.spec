Summary:	A library for controlling and tracing dynamic memory allocations
Summary(pl.UTF-8):	Biblioteka do kontroli i śledzenia dynamicznej alokacji pamięci
Name:		dmalloc
Version:	5.5.2
Release:	1
License:	LGPL
Group:		Development/Debuggers
Source0:	http://dmalloc.com/releases/%{name}-%{version}.tgz
# Source0-md5:	f92e5606c23a8092f3d5694e8d1c932e
Source1:	%{name}.1
Patch0:		%{name}-info.patch
Patch1:		%{name}-pic.patch
Patch2:		%{name}-4.8.2-pld_man.patch
URL:		http://dmalloc.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The debug memory allocation or "dmalloc" library has been designed as
a drop in replacement for the system's `malloc', `realloc', `calloc',
`free' and other memory management routines while providing powerful
debugging facilities configurable at runtime. These facilities include
such things as memory-leak tracking, fence-post write detection,
file/line number reporting, and general logging of statistics. It also
provides support for the debugging of threaded programs.

%description -l pl.UTF-8
Biblioteka do odpluskwiania programów zastępuje systemowe funkcje
takie jak `malloc', `realloc', `calloc', `free' i inne funkcje do
zarządzania pamięcią. Możliwości to wykrywanie wycieków pamięci,
wykrywanie zapisów poza zaalokowanym obszarem, informowanie o
pliku/numerze linii, w której występuje problem oraz generalne
statystyki. Biblioteka umożliwia odpluskwianie programów wątkowych.

%package static
Summary:	Static dmalloc libraries
Summary(pl.UTF-8):	Biblioteki statyczne dmalloc
Group:		Development/Debuggers
Requires:	%{name} = %{version}-%{release}

%description static
Static dmalloc libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dmalloc.

%prep
%setup -q
install %{SOURCE1} .
cd docs
%patch0 -p1
cd ..
%patch1 -p1
%patch2 -p0

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-cxx \
	--enable-threads \
	--enable-shlib

%{__make}
%{__make} docs/%{name}.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1}

%{makeinstall} \
	installsl installcxx installth \
	shlibdir=$RPM_BUILD_ROOT%{_libdir} \
	incdir=$RPM_BUILD_ROOT%{_includedir}

install docs/*.info $RPM_BUILD_ROOT%{_infodir}
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
%doc README NEWS ChangeLog*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
