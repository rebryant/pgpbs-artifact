install:
	cd lrat; make install

run: install
	cd benchmarks; make run
	cp benchmarks/cardinality/cardinality-results.txt .
	cp benchmarks/parity/parity-results.txt .

run-pgbdd: install
	cd benchmarks; make run-pgbdd
	cp benchmarks/parity/parity-results-pgbdd.txt .

test: install
	cd benchmarks; make test

test-pgbdd: install
	cd benchmarks; make test-pgbdd

clean:
	cd benchmarks; make clean
	cd lrat; make clean
	cd src; make clean
	rm -f *~	


superclean:
	cd benchmarks; make superclean
	cd lrat; make clean
	cd src; make clean
	rm -f *~	




