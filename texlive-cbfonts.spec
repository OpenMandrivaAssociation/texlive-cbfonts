%global tl_name cbfonts
%global tl_revision 54080

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Complete set of Greek fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/cbfonts
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(cbfonts-fd)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle presents the whole of Beccari's original Greek font set,
which use the 'Lispiakos' font shape derived from the shape of the fonts
used in printers' shops in Lispia. The fonts are available both as
Metafont source and in Adobe Type 1 format, and at the same wide set of
design sizes as are such font sets as the EC fonts. Please note that
this package needs the complementary cbfonts-fd package to work
properly.

