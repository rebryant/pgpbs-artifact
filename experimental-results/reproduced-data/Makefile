short:
	(cd fig4; make short)
	(cd fig5; make short)
	(cd fig6; make short)
	(cd fig7; make short)

full:
	(cd fig4; make full)
	(cd fig5; make full)
	(cd fig6; make full)
	(cd fig7; make full)

clean:
	(cd fig4; make clean)
	(cd fig5; make clean)
	(cd fig6; make clean)
	(cd fig7; make clean)

superclean:
	(cd fig4; make superclean)
	(cd fig5; make superclean)
	(cd fig6; make superclean)
	(cd fig7; make superclean)

reproduce: short
	rm -rf csv
	mkdir csv
	cp -p */*.csv csv

reproduce-full: full
	rm -rf csv
	mkdir csv
	cp -p */*.csv csv
