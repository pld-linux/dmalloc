Summary:	A library for controlling and tracing dynamic memory allocations
Summary(pl):	Biblioteka do kontroli i ¶ledzenia dynamicznej alokacji pamiêcie
Name:		dmalloc
Version:	4.8.2
Release:	1
License:	LGPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	http://download.sourceforge.net/dmalloc/%{name}-%{version}.tgz
URL:		http://dmalloc.com/
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
Biblioteka do odpluskwiania programów zastêpuje systemowe funkcje
takie jak `malloc', `realloc', `calloc', `free' i inne funkcje do
zarz±dzania pamiêci±. Mo¿liwo¶ci to wykrywanie wycieków pamiêci,
wykrywanie zapisów poza zaalokowanym obszarem, informowanie o
pliku/numerze linii, w której wystêpuje problem oraz generalne
statystyki. Biblioteka umo¿liwia odpluskwianie programów w±tkowych.


%prep
%setup -q

%build
%configure \
	--enable-cxx \
	--enable-threads \
	--enable-shlib
	
%{__make} dmalloc_t all light dmalloc.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{makeinstall} \
	installsl installcxx installth installinfo \
	shlibdir=$RPM_BUILD_ROOT%{_libdir} \
	incdir=$RPM_BUILD_ROOT%{_includedir}

gzip -9nf README NEWS ChangeLog

%post
/sbin/ldconfig
%fix_info_dir

%postun
/sbin/ldconfig
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_infodir}/*
