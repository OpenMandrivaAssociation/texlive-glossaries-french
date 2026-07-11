%global tl_name glossaries-french
%global tl_revision 42873

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	French language module for glossaries package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-french
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-french.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
French language module for glossaries package.

