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

UFILES = urquhart-li-03_shuf.data urquhart-li-12_shuf.data
TFILES = tseitingrid7x165_shuf.data tseitingrid7x185_shuf.data
FILES = $(UFILES) $(TFILES)
TUFILES = urquhart-li-03_shuf.data 

PUFILES = urquhart-li-03_shuf.pdata urquhart-li-12_shuf.pdata
PTFILES = tseitingrid7x165_shuf.pdata tseitingrid7x185_shuf.pdata
PFILES = $(PUFILES) $(PTFILES)
PTUFILES = urquhart-li-03_shuf.pdata

run: results-pgpbs-parity.txt

run-pgbdd: results-pgbdd-parity.txt

test: $(TUFILES)
	$(FORMATTER) $(TUFILES)

test-pgbdd: $(PTUFILES)
	$(FORMATTER) $(PTUFILES)

results-pgpbs-parity.txt: $(FILES)
	echo "PGPBS RESULT SUMMARY"
	$(FORMATTER) $(FILES)
	$(FORMATTER) $(FILES) > results-pgpbs-parity.txt

results-pgbdd-parity.txt: $(PFILES)
	echo "PGBDD RESULT SUMMARY"
	$(FORMATTER) $(PFILES)
	$(FORMATTER) $(PFILES) > results-pgbdd-parity.txt


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
	rm -f *.pdata *.data *results*.txt




