This archive provides a demonstration version of the proof-generating
SAT solver PGPBS, combininig Binary Decision Diagrams (BDDs) and
pseudo-Boolean reasoning.  The solver generates proofs in LRAT format.
A checker for this format is included.

The archive also includes PGBDD, our earlier BDD-based SAT solver.
PGPBS's advantages over PGBDD include:
  * It is fully automated.  No guidance from the user is required
  * It requires no special variable ordering.  To demonstrated this,
    the benchmark files have been "shuffled", randomly permuting
    the variables and the clauses.
  * It runs faster
    
The archive includes the capability to run two classes of benchmarks:
  * Parity problems: Based on exclusive-or operations
  * Cardinality problems: Based on constraints among mismatched sets

All benchmark problems are unsatisfiable.  The task is to generate a
proof of unsatisfiability.  Among all existing proof-generating SAT
solvers that we know, only PGPBS (and possibly PGBDD) can generate an
unsatisfiability proof for any of these benchmarks within a reasonable
amount of effort (less than 5000 seconds and generating a proof with
less than 100 million clauses).


1. System Requirements (Tested with TACAS virtual environment)

       * Python interpreter.  By default, the program runs python3.
         You can change by editing the "INTERP" definition in the
         top-level Makefile

       * C compiler.  The LRAT checker is written in C.  Just about
         any compiler should work.  The default is gcc.

2. Installation and Running Demonstration

All code and benchmark data can be downloaded in two different ways:

A. Using GitHub

   git clone https://github.com/rebryant/pgpbs-artifact

B. Getting the Zip File

   wget http://www.cs.cmu.edu/~bryant/download/pgpbs-artifact.zip
   unzip pgpbs-artifact.zip

Once downloaded, the demonstration can be run as:

   cd pgpbs-artifact
   make run

When running the benchmarks, a lot of stuff gets printed, but the
final summary information is saved in file results-pgpbs.txt in the
top-level directory.  More information about the benchmarks is
included in the README files for the two benchmark classes.  See the
included file "artifact-documentation.pdf" for more information about
the benchmarks and how to interpret the results.

3. Other Makefile options:

install:
  Compiles the LRAT checker.  No other installation steps are
  required.  This is performed automatically when performing "make
  run" and other operations that require the proof checker.

test:
  Run simple examples of the two benchmarks classes.  A lot of stuff
  gets printed out, but you should see the statement "VERIFIED" for
  each benchmark.

run-pgbdd:
  The parity problems can be solved using the earlier solver PGBDD.
  The performance is not as good as PGPBS, but it's better than that
  of any other known proof-generating SAT solver.  The results are
  saved as the file results-pgbdd.txt.

test-pgbdd:
  Run simple examples with PGBDD

clean:
  Delete all generated files, except for any benchmark data

superclean:
  Delete all generated files, including the benchmark data

4. Using PGBDD or PGPBS as a standalone SAT solver

The PGBDD and PGPBS SAT solvers are available as the programs pgbdd.py
and pgpbs.py in the directory pgpbs-artifact/src. There use is
documented in the file pgpbs-artifact/solver/README.txt.

