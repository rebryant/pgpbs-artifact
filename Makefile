install:
	(pushd lrat; make install)

run: install
	(pushd benchmarks; make run; popd)
	cp benchmarks/cardinality/cardinality-results.txt .
	cp benchmarks/parity/parity-results.txt .

run-pgbdd: install
	(pushd benchmarks; make run-pgbdd; popd)
	cp benchmarks/parity/parity-results-pgbdd.txt .

test: install
	(pushd benchmarks; make test; popd)

test-pgbdd: install
	(pushd benchmarks; make test-pgbdd; popd)

clean:
	(pushd benchmarks; make clean; popd)
	(pushd lrat; make clean; popd)
	(pushd src; make clean; popd)
	rm -f *~	


superclean:
	(pushd benchmarks; make superclean; popd)
	(pushd lrat; make clean; popd)
	(pushd src; make clean; popd)
	rm -f *~	




