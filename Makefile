CSRCS=$(wildcard **/*.c)
CEXECS=$(patsubst %.c,%.out,$(CSRCS))

CFLAGS=-std=c11 -g -Wall -pedantic
LDFLAGS=-lm

$(CEXECS): %.out: %.c
	gcc 
all: test

test: lib $(EXEC)
	python3 -mbaygon 

clean:
	$(RM) $(EXEC) *.o a.out lib$(EXEC).so

.PHONY: test all
