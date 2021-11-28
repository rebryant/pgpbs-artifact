clean:
	(cd original-data; make clean)
	(cd reproduced-data; make clean)
	(cd code; make clean)
	(cd doc; make clean)

superclean: clean
	(cd original-data; make superclean)
	(cd reproduced-data; make superclean)

data:
	(cd original-data; make data)
	(cd reproduced-data; make data)
	(cd doc; make all)
	cp doc/graphs.pdf ..


