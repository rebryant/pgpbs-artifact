This directory contains unsatisfiable benchmark problems based on
mismatched formulas computing the parity of a set of values.

1. Benchmarks:

urquhart-li-M_shuf.cnf
	Li's implementation of benchmark problem defined by Urquhart.
	Defined over a M^2 X M^2 bipartite graph

tseitingrid-N_shuf.cnf
	Ellfer's Tseitin grid formula.  Defined over a grid graph with
	N rows and 7 columns


2. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         results-parity.txt

   run-pgbdd: Run all benchmarks with PGBDD.  Tabulate results in
              results-parity-pgbdd.txt	 

   test: Like run, but with smaller set of benchmarks

   test-pgbdd: Like run-pgbdd, but with smaller set of benchmarks.

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

