INTERP=python3
VLEVEL = 1
SEED = 123456

SDIR = ../../src
SNAME = pgpbs.py
PSNAME = pgbdd.py
EDIR = ../../src
LDIR = ../../lrat
FDIR = ../../src


EXTRACTOR = $(INTERP) $(EDIR)/xor_extractor.py
SOLVER = $(INTERP) $(SDIR)/$(SNAME)
PSOLVER = $(INTERP) $(SDIR)/$(PSNAME)
CHECKER = $(LDIR)/lrat-check
FORMATTER = $(INTERP) $(FDIR)/formatter.py

UFILES = urquhart-li-03_shuf.data urquhart-li-06_shuf.data urquhart-li-09_shuf.data urquhart-li-12_shuf.data
TFILES = tseitingrid7x165_shuf.data tseitingrid7x185_shuf.data tseitingrid7x195_shuf.data tseitingrid7x200_shuf.data
FILES = $(UFILES) $(TFILES)
TUFILES = urquhart-li-03_shuf.data urquhart-li-06_shuf.data urquhart-li-09_shuf.data 

PUFILES = urquhart-li-03_shuf.pdata urquhart-li-06_shuf.pdata urquhart-li-09_shuf.pdata urquhart-li-12_shuf.pdata
PTFILES = tseitingrid7x165_shuf.pdata tseitingrid7x185_shuf.pdata tseitingrid7x195_shuf.pdata tseitingrid7x200_shuf.pdata
PFILES = $(PUFILES) $(PTFILES)
PTUFILES = urquhart-li-03_shuf.pdata urquhart-li-06_shuf.pdata urquhart-li-09_shuf.pdata 

run: parity-results.txt

run-pgbdd: parity-results-pgbdd.txt

test: $(TUFILES)
	$(FORMATTER) $(TUFILES)

test-pgbdd: $(PTUFILES)
	$(FORMATTER) $(PTUFILES)

parity-results.txt: $(FILES)
	echo "PGPBS RESULT SUMMARY"
	$(FORMATTER) $(FILES)
	$(FORMATTER) $(FILES) > parity-results.txt
	echo "PGPBS RESULTS SAVED IN FILE 'parity-results.txt'"

parity-results-pgbdd.txt: $(PFILES)
	echo "PGBDD RESULT SUMMARY"
	$(FORMATTER) $(FILES)
	$(FORMATTER) $(FILES) > parity-results-pgbdd.txt
	echo "PGPDD RESULTS SAVED IN FILE 'parity-results-pgbdd.txt'"


.SUFFIXES: .cnf .data .pdata

.cnf.data:
	$(EXTRACTOR) -i $< -o $*.schedule | tee $@
	$(SOLVER) -v $(VLEVEL) -r $(SEED) -i $< -s $*.schedule -o $*.lrat 2>&1 | tee -a $@
	$(CHECKER) $< $*.lrat | tee -a $@

.cnf.pdata:
	$(PSOLVER) -v $(VLEVEL) -i $< -b -o $*.lrat 2>&1 | tee -a $@
	$(CHECKER) $< $*.lrat | tee -a $@

clean:
	rm -f *~ *.schedule *.lrat

superclean: clean
	rm -f *.pdata *.data *.txt




