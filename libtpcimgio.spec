Summary:	PET Image I/O library
Summary(pl.UTF-8):	Biblioteka PET Image I/O
Name:		libtpcimgio
Version:	1.3.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.turkupetcentre.net/software/libsrc/%{name}_%(echo %{version} | tr . _)_src.zip
# Source0-md5:	34cc246a99fe5d21e08af7cdf34ef8bf
Patch0:		%{name}-shared.patch
URL:		http://www.turkupetcentre.net/software/libdoc/libtpcimgio/
BuildRequires:	libtpcmisc-devel >= 1.3.0
BuildRequires:	unzip
Requires:	libtpcmisc >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PET Image I/O library by Turku PET Centre.

%description -l pl.UTF-8
PET Image I/O - biblioteka wejścia/wyjścia obrazów Turku PET Centre.

%package devel
Summary:	Header files for libtpcimgio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtpcimgio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtpcmisc-devel >= 1.3.0

%description devel
Header files for libtpcimgio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtpcimgio.

%package static
Summary:	Static libtpcimgio library
Summary(pl.UTF-8):	Statyczna biblioteka libtpcimgio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtpcimgio library.

%description static -l pl.UTF-8
Statyczna biblioteka libtpcimgio.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} libtpcimgio.la \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -I/usr/include/tpc -Iinclude \$(INCLUDE) \$(ANSI)" \
	LDFLAGS="%{rpmldflags}" \
	PET_LIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} libinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	PET_LIB=%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/tpc
install include/*.h $RPM_BUILD_ROOT%{_includedir}/tpc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc History Readme TODO
%attr(755,root,root) %{_libdir}/libtpcimgio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtpcimgio.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtpcimgio.so
%{_libdir}/libtpcimgio.la
%{_includedir}/tpc/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtpcimgio.a
