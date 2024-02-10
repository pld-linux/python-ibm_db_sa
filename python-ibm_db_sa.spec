#
# Conditional build:
%bcond_with	tests	# unit tests (require sqlalchemy.testing.runner and some DB)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	SQLAlchemy support for IBM Data Servers
Summary(pl.UTF-8):	Obsługa serwerów baz danych IBM dla SQLAlchemy
Name:		python-ibm_db_sa
Version:	0.4.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ibm-db-sa/
Source0:	https://files.pythonhosted.org/packages/source/i/ibm-db-sa/ibm_db_sa-%{version}.tar.gz
# Source0-md5:	79d4aba8471c380306069b6bb03276c6
URL:		https://pypi.org/project/ibm-db-sa/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-ibm_db >= 1.0.1
BuildRequires:	python-nose >= 0.11
BuildRequires:	python-sqlalchemy >= 0.7.3
BuildRequires:	python-sqlalchemy < 2.1
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-ibm_db >= 1.0.1
BuildRequires:	python3-nose >= 0.11
BuildRequires:	python3-sqlalchemy >= 0.7.3
BuildRequires:	python3-sqlalchemy < 2.1
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IBM_DB_SA adapter provides the Python/SQLAlchemy interface to IBM
Data Servers (IBM DB2).

%description -l pl.UTF-8
Adapter IBM_DB_SA dostarcza interfejs Pythona/SQLAlchemy do serwerów
baz danych IBM (IBM DB2).

%package -n python3-ibm_db_sa
Summary:	SQLAlchemy support for IBM Data Servers
Summary(pl.UTF-8):	Obsługa serwerów baz danych IBM dla SQLAlchemy
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-ibm_db_sa
The IBM_DB_SA adapter provides the Python/SQLAlchemy interface to IBM
Data Servers (IBM DB2).

%description -n python3-ibm_db_sa -l pl.UTF-8
Adapter IBM_DB_SA dostarcza interfejs Pythona/SQLAlchemy do serwerów
baz danych IBM (IBM DB2).

%prep
%setup -q -n ibm_db_sa-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} run_tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} run_tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%{py_sitescriptdir}/ibm_db_sa
%{py_sitescriptdir}/ibm_db_sa-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ibm_db_sa
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%{py3_sitescriptdir}/ibm_db_sa
%{py3_sitescriptdir}/ibm_db_sa-%{version}-py*.egg-info
%endif
