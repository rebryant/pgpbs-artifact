run: install
	cd benchmarks; make run
	cp benchmarks/results-pgpbs.txt .
	cat results-pgpbs.txt

install:
	cd lrat; make install

run-pgbdd: install
	cd benchmarks; make run-pgbdd
	cp benchmarks/results-pgbdd.txt .
	cat results-pgbdd.txt

test: install
	cd benchmarks; make test

test-pgbdd: install
	cd benchmarks; make test-pgbdd

clean:
	cd benchmarks; make clean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt


superclean:
	cd benchmarks; make superclean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt




