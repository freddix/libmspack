Summary:	A library for Microsoft compression formats
Name:		libmspack
Version:	0.3alpha
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.cabextract.org.uk/libmspack/%{name}-%{version}.tar.gz
# Source0-md5:	08d08455b6d58ea649b35febd23f6386
URL:		http://www.cabextract.org.uk/libmspack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of libmspack is to provide compressors and decompressors,
archivers and dearchivers for Microsoft compression formats: CAB, CHM,
HLP, KWAJ, LIT and SZDD. It is also designed to be easily embeddable,
stable, robust and resource-efficient.

%package devel
Summary:	Header files for libmspack library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmspack library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %ghost %{_libdir}/libmspack.so.?
%attr(755,root,root) %{_libdir}/libmspack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,css,png}
%attr(755,root,root) %{_libdir}/libmspack.so
%{_libdir}/libmspack.la
%{_includedir}/mspack.h
%{_pkgconfigdir}/*.pc

