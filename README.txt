This archive provides a demonstration version of the proof-generating
SAT solver PGPBS, combininig Binary Decision Diagrams (BDDs) and
pseudo-Boolean reasoning.  The solver generates proofs in LRAT format.
A checker for this format is included.

The archive also includes PGBDD, our earlier BDD-based SAT solver.
PGPBS's advantages over PGBDD include:
  * It is fully automated.  No guidance from the user is required
  * It requires no special variable ordering.  It can achieve high
    performance even when the variables have been randomly permuted.
  * It runs faster
    
PGPBS is aided by two included pseudo-Boolean constraint extraction
programs: xor_extractor and constraint_extractor.  These programs use
heuristic methods to detect exclusive-or/nor and cardinality
constraints encoded as clauses in the input file.  They are
automatically invoked when running the benchmarks.

PAPER RESULTS

This artifact accompanies the paper ``Clausal Proofs for
Pseudo-Boolean Reasoning,'' to be published at TACAS 2022.  The
subdirectory `experimental-results' includes the full data from the
paper, as well as the ability to generate either (1) some or (2) most
of that data, depending on the available computing resources.  The
ability to reproduce the full results is subject to the following
limitations:

* We have not included the KISSAT SAT solver in our distribution.
  That prevents generating the results we used to compare our solvers
  to traditional CDCL solvers.  The original data from KISSAT are included.

* For the two sets of Urquhart benchmarks, we used generators that we
  are not authorized to redistribute.  Instead, we have included CNF
  files for some of these benchmarks, but not for the largest ones,
  since the file sizes are too large.

Reproducing the full experimental results requires many hours of
execution on a well-resourced machine (in terms of disk space and
physical memory).  The normal use of the artifact is to run a subset
of the full benchmarks.  Note however, that even these demonstrate a
clear advantage of our solvers over existing CDCL solvers.

The document `graphs.pdf' shows a direct comparison of the results
from the paper and those that are reproduced from this artifact, and a
brief explanation of their signicance.  This document is generated
automatically using the original and reproduced data.

INSTRUCTIONS

1. System Requirements (Tested with TACAS virtual environment)

       * Python interpreter.  By default, the program runs python3.
         You can change by editing the `INTERP' definition in the
         top-level Makefile

       * C compiler.  The LRAT checker is written in C.  Just about
         any compiler should work.  The default is gcc.

       * An installation of pdflatex, along with the tikz graphics
         package

2. Installation

All code, benchmarks, and data can be downloaded in two different
ways:

A. Using GitHub

   git clone https://github.com/rebryant/pgpbs-artifact

B. Getting the Zip File

   wget http://www.cs.cmu.edu/~bryant/download/pgpbs-artifact.zip
   unzip pgpbs-artifact.zip

3. Reproducing Paper Results

Once downloaded, a portion of the experimental results can be generated with the commands:

   cd pgpbs-artifact
   make reproduce

After running the solvers on a set of benchmarks, the data will be
merged and processed to produce the document `graphs.pdf' in this
directory.  This document provides versions of Figures 4--7 of the
paper, showing both the original data (extracted from files in the
artifact) and the reproduced data.  See the included file
`artifact-documentation.pdf' for more information about the results
and their significance..

Those wishing to generate the full results should execute the
following:

   cd pgpbs-artifact
   make reproduce-full

This will require many hours of execution on a well-resourced machine.


4. Other Makefile options:

install:
  Compiles the LRAT checker.  No other installation steps are
  required.  This is performed automatically when performing `make
  reproduce' and other operations that require the proof checker.

test:
  Run simple examples of some benchmarks.  A lot of stuff gets printed
  out, but you should see the statement `VERIFIED' for each benchmark.

test-pgbdd:
  Run simple examples with PGBDD

clean:
  Delete all generated files, except for any demo or reproduced data

superclean:
  Delete all generated files, including the demo and reproduced data

4. Using PGBDD or PGPBS as standalone SAT solvers

The PGBDD and PGPBS SAT solvers are available as the programs pgbdd.py
and pgpbs.py in the directory pgpbs-artifact/src. Their use is
documented in the file pgpbs-artifact/solver/README.txt.

