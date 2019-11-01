CSRCS=$(wildcard **/*.c)
COBJS=$(patsubst %.c,%.o,$(CSRCS))

CFLAGS=-std=c99 -g -Wall -pedantic
LDFLAGS=-lm

all: test

test: lib $(EXEC)
	@echo -e '\e[1;34mRun tests...\e[m'
	./test.py

clean:
	@echo -e '\e[1;34mCleaning...\e[m'
	$(RM) $(EXEC) *.o a.out lib$(EXEC).so

.PHONY: test all format build lib
