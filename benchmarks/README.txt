This is the parent directory to two sets of unsatisfiable benchmark problems.

cardinality: Mismatched set sizes
parity: Mismatched parity computations over a set of Boolean variables

1. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         cardinality/results-cardinality.txt parity/results-parity.txt

   run-pgbdd: Run all parity benchmarks with PGBDD.  Tabulate results in
              parity/results-parity-pgbdd.txt	 

   test: Like run, but with smaller set of benchmarks

   test-pgbdd: Like run-pgbdd, but with smaller set of benchmarks.

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

