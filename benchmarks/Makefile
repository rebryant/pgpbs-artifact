run:
	(pushd cardinality; make run; popd)
	(pushd parity; make run; popd)

run-pgbdd:
	(pushd parity; make run-pgbdd; popd)

test:
	(pushd cardinality; make test; popd)
	(pushd parity; make test; popd)

test-pgbdd:
	(pushd parity; make test-pgbdd; popd)

clean:
	(pushd cardinality; make clean; popd)
	(pushd parity; make clean; popd)
	rm -f *~

superclean:
	(pushd cardinality; make superclean; popd)
	(pushd parity; make superclean; popd)
	rm -f *~


