INTERP=python3
VLEVEL = 1
SEED = 123456

SDIR = ../../src
SNAME = pgpbs.py
EDIR = ../../src
LDIR = ../../lrat
FDIR = ../../src

EXTRACTOR = $(INTERP) $(EDIR)/constraint_extractor.py
SOLVER = $(INTERP) $(SDIR)/$(SNAME)
CHECKER = $(LDIR)/lrat-check
FORMATTER = $(INTERP) $(FDIR)/formatter.py

CBFILES = mchess-board-24_shuf.data  mchess-board-32_shuf.data
CTFILES = mchess-torus-24_shuf.data  mchess-torus-32_shuf.data
PFILES = pigeon-sinz-16_shuf.data pigeon-direct-16_shuf.data
RFILES = randomG-B-mix-n19-d05_shuf.data randomG-n20-d05_shuf.data
FILES = $(CBFILES) $(CTFILES) $(PFILES) $(RFILES) 
TFILES=$(RFILES)

run: cardinality-results.txt

test: $(TFILES)
	$(FORMATTER) $(TFILES)

cardinality-results.txt: $(FILES)
	echo "RESULT SUMMARY"
	$(FORMATTER) $(FILES)
	$(FORMATTER) $(FILES) > cardinality-results.txt
	echo "RESULTS SAVED IN FILE 'cardinality-results.txt'"


.SUFFIXES: .cnf .data

.cnf.data:
	$(EXTRACTOR) -i $< -o $*.schedule | tee $@
	$(SOLVER) -v $(VLEVEL) -i $< -s $*.schedule -o $*.lrat 2>&1 | tee -a $@
	$(CHECKER) $< $*.lrat | tee -a $@

clean:
	rm -f *~ *.schedule *.lrat

superclean: clean
	rm -f *.data *.txt




