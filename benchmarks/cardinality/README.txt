This directory contains unsatisfiable benchmark problems based on
mismatched set sizes.

1. Benchmarks:

mchess-board-N_shuf.cnf:
	The NxN mutilated chessboard.

mchess-torus-N_shuf.cnf:
	Defined over a torus, with the edges of the board wrapping
	around for both top-bottom and left-right

randomG-XXXX-nN-d05_shuf.cnf
	Attempt to find perfect mapping in a random N X (N+1) bipartite
	graph with 50% density.

2. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         results-cardinality.txt

   test: Like run, but with smaller set of benchmarks

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

