clean:
	(cd original-data; make clean)
	(cd reproduced-data; make clean)
	(cd code; make clean)
	(cd doc; make clean)
	rm -f *~

superclean: clean
	(cd original-data; make superclean)
	(cd reproduced-data; make superclean)

reproduce:
	(cd reproduced-data; make reproduce)
	(cd original-data; make data)
	(cd doc; make document)
	cp doc/graphs.pdf ..

reproduce-full:
	(cd reproduced-data; make reproduce-full)
	(cd original-data; make data)
	(cd doc; make documentl)
	cp doc/graphs.pdf ..


