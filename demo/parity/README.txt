This directory contains unsatisfiable benchmark problems based on
mismatched formulas computing the parity of a set of values.  All have
been processed with the program scranfilize to randomize the ordering
of variables and clauses.


1. Benchmarks:

urquhart-li-M_shuf.cnf
	Li's implementation of benchmark problem defined by Urquhart.
	Defined over a M^2 X M^2 bipartite graph, for M=3,12.  This
	problem is notoriously difficult for most SAT solvers.  We
	know of no solver, other than ours, that can generate proofs
	for even the smallest (M=3) instance.  Both PGBDD and PGPBS
	can handle them easily.

tseitingrid-7xN_shuf.cnf
	Elffer's Tseitin grid formula, introduced for the 2016 SAT
	competition.  Defined over a grid graph with 7 rows and N
	columns, for N=165,185.  These were used in the 2020 SAT
	competition.  None of the entrants could generate proofs
	within the 5000s time limit.  Both PGBDD and PGBPBS can handle
	them easily.

2. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         results-parity.txt

   run-pgbdd: Run all benchmarks with PGBDD.  Tabulate results in
              results-parity-pgbdd.txt	 

   test: Like run, but with smaller set of benchmarks

   test-pgbdd: Like run-pgbdd, but with smaller set of benchmarks.

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

