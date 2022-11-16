Name:		texlive-glossaries-french
Version:	42873
Release:	1
Summary:	French language module for glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-french
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
French language module for glossaries package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/glossaries-french
%{_texmfdistdir}/tex/latex/glossaries-french
%doc %{_texmfdistdir}/doc/latex/glossaries-french

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
