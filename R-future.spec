#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: 356da62
#
Name     : R-future
Version  : 1.34.0
Release  : 75
URL      : https://cran.r-project.org/src/contrib/future_1.34.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/future_1.34.0.tar.gz
Summary  : Unified Parallel and Distributed Processing in R for Everyone
Group    : Development/Tools
License  : LGPL-2.1+
Requires: R-digest
Requires: R-globals
Requires: R-listenv
Requires: R-parallelly
BuildRequires : R-digest
BuildRequires : R-globals
BuildRequires : R-listenv
BuildRequires : R-parallelly
BuildRequires : buildreq-R

%description
unified Future API for sequential and parallel processing of R
    expression via futures.  The simplest way to evaluate an expression
    in parallel is to use `x %<-% { expression }` with `plan(multisession)`.
    This package implements sequential, multicore, multisession, and
    cluster futures.  With these, R expressions can be evaluated on the
    local machine, in parallel a set of local machines, or distributed
    on a mix of local and remote machines.
    Extensions to this package implement additional backends for
    processing futures via compute cluster schedulers, etc.
    Because of its unified API, there is no need to modify any code in order
    switch from sequential on the local machine to, say, distributed
    processing on a remote compute cluster.
    Another strength of this package is that global variables and functions
    are automatically identified and exported as needed, making it
    straightforward to tweak existing code to make use of futures.

%prep
%setup -q -n future
pushd ..
cp -a future buildavx2
popd
pushd ..
cp -a future buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722298597

%install
export SOURCE_DATE_EPOCH=1722298597
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/future/CITATION
/usr/lib64/R/library/future/DESCRIPTION
/usr/lib64/R/library/future/INDEX
/usr/lib64/R/library/future/Meta/Rd.rds
/usr/lib64/R/library/future/Meta/demo.rds
/usr/lib64/R/library/future/Meta/features.rds
/usr/lib64/R/library/future/Meta/hsearch.rds
/usr/lib64/R/library/future/Meta/links.rds
/usr/lib64/R/library/future/Meta/nsInfo.rds
/usr/lib64/R/library/future/Meta/package.rds
/usr/lib64/R/library/future/Meta/vignette.rds
/usr/lib64/R/library/future/NAMESPACE
/usr/lib64/R/library/future/NEWS.md
/usr/lib64/R/library/future/R/future
/usr/lib64/R/library/future/R/future.rdb
/usr/lib64/R/library/future/R/future.rdx
/usr/lib64/R/library/future/WORDLIST
/usr/lib64/R/library/future/demo/fibonacci.R
/usr/lib64/R/library/future/demo/mandelbrot.R
/usr/lib64/R/library/future/doc/future-1-overview.html
/usr/lib64/R/library/future/doc/future-1-overview.md.rsp
/usr/lib64/R/library/future/doc/future-2-output.html
/usr/lib64/R/library/future/doc/future-2-output.md.rsp
/usr/lib64/R/library/future/doc/future-3-topologies.html
/usr/lib64/R/library/future/doc/future-3-topologies.md.rsp
/usr/lib64/R/library/future/doc/future-4-issues.html
/usr/lib64/R/library/future/doc/future-4-issues.md.rsp
/usr/lib64/R/library/future/doc/future-4-non-exportable-objects.html
/usr/lib64/R/library/future/doc/future-4-non-exportable-objects.md.rsp
/usr/lib64/R/library/future/doc/future-5-startup.html
/usr/lib64/R/library/future/doc/future-5-startup.md.rsp
/usr/lib64/R/library/future/doc/future-6-future-api-backend-specification.html
/usr/lib64/R/library/future/doc/future-6-future-api-backend-specification.md.rsp
/usr/lib64/R/library/future/doc/future-7-for-package-developers.html
/usr/lib64/R/library/future/doc/future-7-for-package-developers.md.rsp
/usr/lib64/R/library/future/doc/future-8-how-future-is-validated.html
/usr/lib64/R/library/future/doc/future-8-how-future-is-validated.md.rsp
/usr/lib64/R/library/future/doc/index.html
/usr/lib64/R/library/future/help/AnIndex
/usr/lib64/R/library/future/help/aliases.rds
/usr/lib64/R/library/future/help/figures/logo.png
/usr/lib64/R/library/future/help/future.rdb
/usr/lib64/R/library/future/help/future.rdx
/usr/lib64/R/library/future/help/paths.rds
/usr/lib64/R/library/future/html/00Index.html
/usr/lib64/R/library/future/html/R.css
/usr/lib64/R/library/future/tests/000.sessionDetails.R
/usr/lib64/R/library/future/tests/ClusterRegistry.R
/usr/lib64/R/library/future/tests/Future-class.R
/usr/lib64/R/library/future/tests/FutureError.R
/usr/lib64/R/library/future/tests/FutureGlobals.R
/usr/lib64/R/library/future/tests/FutureRegistry.R
/usr/lib64/R/library/future/tests/adhoc_native_to_utf8.R
/usr/lib64/R/library/future/tests/backtrace.R
/usr/lib64/R/library/future/tests/bquote.R
/usr/lib64/R/library/future/tests/capture_journals.R
/usr/lib64/R/library/future/tests/cluster,worker-termination.R
/usr/lib64/R/library/future/tests/cluster-missing-future-pkg.R
/usr/lib64/R/library/future/tests/cluster.R
/usr/lib64/R/library/future/tests/constant.R
/usr/lib64/R/library/future/tests/demo.R
/usr/lib64/R/library/future/tests/dotdotdot.R
/usr/lib64/R/library/future/tests/early-signaling.R
/usr/lib64/R/library/future/tests/future,labels.R
/usr/lib64/R/library/future/tests/future,optsenvvars.R
/usr/lib64/R/library/future/tests/future.R
/usr/lib64/R/library/future/tests/futureAssign.R
/usr/lib64/R/library/future/tests/futureAssign_OP.R
/usr/lib64/R/library/future/tests/futureAssign_OP_with_environment.R
/usr/lib64/R/library/future/tests/futureAssign_OP_with_listenv.R
/usr/lib64/R/library/future/tests/futureCall.R
/usr/lib64/R/library/future/tests/futureOf.R
/usr/lib64/R/library/future/tests/futureOf_with_environment.R
/usr/lib64/R/library/future/tests/futureOf_with_listenv.R
/usr/lib64/R/library/future/tests/futureSessionInfo.R
/usr/lib64/R/library/future/tests/futures.R
/usr/lib64/R/library/future/tests/globals,NSE.R
/usr/lib64/R/library/future/tests/globals,S4methods.R
/usr/lib64/R/library/future/tests/globals,formulas.R
/usr/lib64/R/library/future/tests/globals,locals.R
/usr/lib64/R/library/future/tests/globals,manual.R
/usr/lib64/R/library/future/tests/globals,resolve.R
/usr/lib64/R/library/future/tests/globals,subassignment.R
/usr/lib64/R/library/future/tests/globals,toolarge.R
/usr/lib64/R/library/future/tests/globals,tricky.R
/usr/lib64/R/library/future/tests/globals,tricky_recursive.R
/usr/lib64/R/library/future/tests/globalsOf,tweaks.R
/usr/lib64/R/library/future/tests/immediateCondition.R
/usr/lib64/R/library/future/tests/incl/end.R
/usr/lib64/R/library/future/tests/incl/start,load-only.R
/usr/lib64/R/library/future/tests/incl/start.R
/usr/lib64/R/library/future/tests/invalid-owner.R
/usr/lib64/R/library/future/tests/mandelbrot.R
/usr/lib64/R/library/future/tests/mpi.R
/usr/lib64/R/library/future/tests/multicore,multithreading.R
/usr/lib64/R/library/future/tests/multicore,worker-termination.R
/usr/lib64/R/library/future/tests/multicore.R
/usr/lib64/R/library/future/tests/multisession.R
/usr/lib64/R/library/future/tests/nbrOfWorkers.R
/usr/lib64/R/library/future/tests/nested_futures,mc.cores.R
/usr/lib64/R/library/future/tests/nested_futures.R
/usr/lib64/R/library/future/tests/non-exportable,connections.R
/usr/lib64/R/library/future/tests/objectSize.R
/usr/lib64/R/library/future/tests/plan.R
/usr/lib64/R/library/future/tests/relaying,muffle.R
/usr/lib64/R/library/future/tests/relaying,split.R
/usr/lib64/R/library/future/tests/relaying.R
/usr/lib64/R/library/future/tests/requestCore.R
/usr/lib64/R/library/future/tests/requestNode.R
/usr/lib64/R/library/future/tests/reserved-keyword-functions.R
/usr/lib64/R/library/future/tests/resolve.R
/usr/lib64/R/library/future/tests/resolved-non-blocking-test.R
/usr/lib64/R/library/future/tests/rng.R
/usr/lib64/R/library/future/tests/rng_utils.R
/usr/lib64/R/library/future/tests/sequential.R
/usr/lib64/R/library/future/tests/sessionDetails.R
/usr/lib64/R/library/future/tests/startup.R
/usr/lib64/R/library/future/tests/stdout.R
/usr/lib64/R/library/future/tests/tweak.R
/usr/lib64/R/library/future/tests/utils.R
/usr/lib64/R/library/future/tests/uuid.R
/usr/lib64/R/library/future/tests/whichIndex.R
/usr/lib64/R/library/future/vignettes-static/future-1-overview.md.rsp.rsp
/usr/lib64/R/library/future/vignettes-static/incl/future-1-overview-example2.R
/usr/lib64/R/library/future/vignettes-static/incl/future-1-overview-example3.R
