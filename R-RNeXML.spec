#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RNeXML
Version  : 2.4.5
Release  : 32
URL      : https://cran.r-project.org/src/contrib/RNeXML_2.4.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RNeXML_2.4.5.tar.gz
Summary  : Semantically Rich I/O for the 'NeXML' Format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-XML
Requires: R-ape
Requires: R-dplyr
Requires: R-httr
Requires: R-lazyeval
Requires: R-plyr
Requires: R-reshape2
Requires: R-stringi
Requires: R-stringr
Requires: R-tidyr
Requires: R-uuid
Requires: R-xml2
BuildRequires : R-XML
BuildRequires : R-ape
BuildRequires : R-dplyr
BuildRequires : R-httr
BuildRequires : R-lazyeval
BuildRequires : R-plyr
BuildRequires : R-reshape2
BuildRequires : R-stringi
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : R-uuid
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
Provides access to phyloinformatic data in 'NeXML' format. The package should
add new functionality to R such as the possibility to manipulate 'NeXML'
objects in more various and refined way and compatibility with 'ape' objects.

%prep
%setup -q -c -n RNeXML
cd %{_builddir}/RNeXML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592587276

%install
export SOURCE_DATE_EPOCH=1592587276
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RNeXML || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RNeXML/CITATION
/usr/lib64/R/library/RNeXML/DESCRIPTION
/usr/lib64/R/library/RNeXML/INDEX
/usr/lib64/R/library/RNeXML/LICENSE
/usr/lib64/R/library/RNeXML/Meta/Rd.rds
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
/usr/lib64/R/library/RNeXML/doc/S4.Rmd
/usr/lib64/R/library/RNeXML/doc/S4.html
/usr/lib64/R/library/RNeXML/doc/index.html
/usr/lib64/R/library/RNeXML/doc/intro.Rmd
/usr/lib64/R/library/RNeXML/doc/intro.html
/usr/lib64/R/library/RNeXML/doc/metadata.Rmd
/usr/lib64/R/library/RNeXML/doc/metadata.html
/usr/lib64/R/library/RNeXML/doc/simmap.Rmd
/usr/lib64/R/library/RNeXML/doc/simmap.html
/usr/lib64/R/library/RNeXML/doc/sparql.Rmd
/usr/lib64/R/library/RNeXML/doc/sparql.html
/usr/lib64/R/library/RNeXML/examples/RDFa2RDFXML.xsl
/usr/lib64/R/library/RNeXML/examples/biophylo.xml
/usr/lib64/R/library/RNeXML/examples/characters.xml
/usr/lib64/R/library/RNeXML/examples/coal.xml
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
/usr/lib64/R/library/RNeXML/examples/no-base-ns.xml
/usr/lib64/R/library/RNeXML/examples/ontotrace-result.xml
/usr/lib64/R/library/RNeXML/examples/phenex.xml
/usr/lib64/R/library/RNeXML/examples/phenoscape.xml
/usr/lib64/R/library/RNeXML/examples/primates.xml
/usr/lib64/R/library/RNeXML/examples/primates_from_R.xml
/usr/lib64/R/library/RNeXML/examples/primates_meta.xml
/usr/lib64/R/library/RNeXML/examples/primates_meta_xslt.xml
/usr/lib64/R/library/RNeXML/examples/simmap.nex
/usr/lib64/R/library/RNeXML/examples/simmap.xml
/usr/lib64/R/library/RNeXML/examples/simmap_ex.xml
/usr/lib64/R/library/RNeXML/examples/some_missing_branchlengths.xml
/usr/lib64/R/library/RNeXML/examples/sparql.newick
/usr/lib64/R/library/RNeXML/examples/taxa.xml
/usr/lib64/R/library/RNeXML/examples/treebase-record.xml
/usr/lib64/R/library/RNeXML/examples/trees.xml
/usr/lib64/R/library/RNeXML/help/AnIndex
/usr/lib64/R/library/RNeXML/help/RNeXML.rdb
/usr/lib64/R/library/RNeXML/help/RNeXML.rdx
/usr/lib64/R/library/RNeXML/help/aliases.rds
/usr/lib64/R/library/RNeXML/help/figures/Figure1-1.png
/usr/lib64/R/library/RNeXML/help/figures/logo.svg
/usr/lib64/R/library/RNeXML/help/figures/unnamed-chunk-5-1.png
/usr/lib64/R/library/RNeXML/help/figures/unnamed-chunk-8-1.png
/usr/lib64/R/library/RNeXML/help/paths.rds
/usr/lib64/R/library/RNeXML/html/00Index.html
/usr/lib64/R/library/RNeXML/html/R.css
/usr/lib64/R/library/RNeXML/simmap.md
/usr/lib64/R/library/RNeXML/tests/spelling.R
/usr/lib64/R/library/RNeXML/tests/test-all.R
/usr/lib64/R/library/RNeXML/tests/testthat/conversions.R
/usr/lib64/R/library/RNeXML/tests/testthat/geiger_test.R
/usr/lib64/R/library/RNeXML/tests/testthat/helper-RNeXML.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_01_exported_util.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_01_utils.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_02_summary.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_ape.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_characters.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_comp_analysis.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_concatenate.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_get_characters.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_get_level.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_global_ids.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_inheritance.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_meta.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_meta_extract.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_nexml_read.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_parsing.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_publish.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_rdf.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_serializing.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_simmap.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_taxonomy.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_toplevel_api.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_validate.R
/usr/lib64/R/library/RNeXML/tests/testthat/test_zzz_cleanup.R
/usr/lib64/R/library/RNeXML/tests/testthat/treebase_test.R
