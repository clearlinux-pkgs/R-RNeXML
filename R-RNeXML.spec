#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RNeXML
Version  : 2.2.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/RNeXML_2.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RNeXML_2.2.0.tar.gz
Summary  : Semantically Rich I/O for the 'NeXML' Format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-XML
Requires: R-ape
Requires: R-coda
Requires: R-deSolve
Requires: R-geiger
Requires: R-httr
Requires: R-lazyeval
Requires: R-mvtnorm
Requires: R-plyr
Requires: R-reshape2
Requires: R-subplex
Requires: R-tidyr
Requires: R-uuid
Requires: R-xml2
BuildRequires : R-XML
BuildRequires : R-ape
BuildRequires : R-coda
BuildRequires : R-deSolve
BuildRequires : R-geiger
BuildRequires : R-httr
BuildRequires : R-lazyeval
BuildRequires : R-mvtnorm
BuildRequires : R-plyr
BuildRequires : R-reshape2
BuildRequires : R-subplex
BuildRequires : R-tidyr
BuildRequires : R-uuid
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
package should add new functionality to R such as the possibility to
    manipulate 'NeXML' objects in more various and refined way and compatibility
    with 'ape' objects.

%prep
%setup -q -c -n RNeXML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541151896

%install
export SOURCE_DATE_EPOCH=1541151896
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNeXML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNeXML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNeXML
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RNeXML|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RNeXML/CITATION
/usr/lib64/R/library/RNeXML/DESCRIPTION
/usr/lib64/R/library/RNeXML/INDEX
/usr/lib64/R/library/RNeXML/LICENSE
/usr/lib64/R/library/RNeXML/Meta/Rd.rds
/usr/lib64/R/library/RNeXML/Meta/data.rds
/usr/lib64/R/library/RNeXML/Meta/features.rds
/usr/lib64/R/library/RNeXML/Meta/hsearch.rds
/usr/lib64/R/library/RNeXML/Meta/links.rds
/usr/lib64/R/library/RNeXML/Meta/nsInfo.rds
/usr/lib64/R/library/RNeXML/Meta/package.rds
/usr/lib64/R/library/RNeXML/Meta/vignette.rds
/usr/lib64/R/library/RNeXML/NAMESPACE
/usr/lib64/R/library/RNeXML/NEWS.md
/usr/lib64/R/library/RNeXML/R/RNeXML
/usr/lib64/R/library/RNeXML/R/RNeXML.rdb
/usr/lib64/R/library/RNeXML/R/RNeXML.rdx
/usr/lib64/R/library/RNeXML/WORDLIST
/usr/lib64/R/library/RNeXML/data/simmap_ex.rda
/usr/lib64/R/library/RNeXML/doc/S4.R
/usr/lib64/R/library/RNeXML/doc/S4.Rmd
/usr/lib64/R/library/RNeXML/doc/S4.html
/usr/lib64/R/library/RNeXML/doc/index.html
/usr/lib64/R/library/RNeXML/doc/metadata.R
/usr/lib64/R/library/RNeXML/doc/metadata.Rmd
/usr/lib64/R/library/RNeXML/doc/metadata.html
/usr/lib64/R/library/RNeXML/doc/simmap.R
/usr/lib64/R/library/RNeXML/doc/simmap.Rmd
/usr/lib64/R/library/RNeXML/doc/simmap.html
/usr/lib64/R/library/RNeXML/doc/sparql.R
/usr/lib64/R/library/RNeXML/doc/sparql.Rmd
/usr/lib64/R/library/RNeXML/doc/sparql.html
/usr/lib64/R/library/RNeXML/examples/RDFa2RDFXML.xsl
/usr/lib64/R/library/RNeXML/examples/biophylo.xml
/usr/lib64/R/library/RNeXML/examples/characters.xml
/usr/lib64/R/library/RNeXML/examples/comp_analysis.xml
/usr/lib64/R/library/RNeXML/examples/gardiner_1984.xml
/usr/lib64/R/library/RNeXML/examples/geospiza.xml
/usr/lib64/R/library/RNeXML/examples/jsonld-ex.R
/usr/lib64/R/library/RNeXML/examples/mbank_X962_11-22-2013_1534.nex
/usr/lib64/R/library/RNeXML/examples/merge_data.Rmd
/usr/lib64/R/library/RNeXML/examples/merge_data.md
/usr/lib64/R/library/RNeXML/examples/meta_example.xml
/usr/lib64/R/library/RNeXML/examples/meta_taxa.xml
/usr/lib64/R/library/RNeXML/examples/missing_some_branchlengths.xml
/usr/lib64/R/library/RNeXML/examples/multitrees.xml
/usr/lib64/R/library/RNeXML/examples/ncbii.xml
/usr/lib64/R/library/RNeXML/examples/ontotrace-result.xml
/usr/lib64/R/library/RNeXML/examples/phenoscape.xml
/usr/lib64/R/library/RNeXML/examples/primates.xml
/usr/lib64/R/library/RNeXML/examples/primates_from_R.xml
/usr/lib64/R/library/RNeXML/examples/primates_meta.xml
/usr/lib64/R/library/RNeXML/examples/primates_meta_xslt.xml
/usr/lib64/R/library/RNeXML/examples/simmap.nex
/usr/lib64/R/library/RNeXML/examples/simmap.xml
/usr/lib64/R/library/RNeXML/examples/some_missing_branchlengths.xml
/usr/lib64/R/library/RNeXML/examples/sparql.newick
/usr/lib64/R/library/RNeXML/examples/taxa.xml
/usr/lib64/R/library/RNeXML/examples/treebase-record.xml
/usr/lib64/R/library/RNeXML/examples/trees.xml
/usr/lib64/R/library/RNeXML/help/AnIndex
/usr/lib64/R/library/RNeXML/help/RNeXML.rdb
/usr/lib64/R/library/RNeXML/help/RNeXML.rdx
/usr/lib64/R/library/RNeXML/help/aliases.rds
/usr/lib64/R/library/RNeXML/help/paths.rds
/usr/lib64/R/library/RNeXML/html/00Index.html
/usr/lib64/R/library/RNeXML/html/R.css
/usr/lib64/R/library/RNeXML/simmap.md
