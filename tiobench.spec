Summary:	Threaded I/O tester
Summary(pl.UTF-8):	Wielowątkowy tester I/O
Name:		tiobench
Version:	0.3.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/tiobench/%{name}-%{version}.tar.gz
# Source0-md5:	bf485bf820e693c79e6bd2a38702a128
Patch0:		%{name}-format-security.patch
Patch1:		%{name}-fix-conflicting-types.patch
URL:		http://sf.net/projects/tiobench/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable, robust, fully-threaded I/O benchmark program.

%description -l pl.UTF-8
Przenośny, potężny, w pełni wątkowy program testujący wydajność I/O.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LINK="%{__cc} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}-null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
