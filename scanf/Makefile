CSRCS=$(wildcard *.c)
CEXECS=$(patsubst %.c,%.out,$(CSRCS))

CFLAGS=-std=c11 -g -Wall -pedantic
LDFLAGS=-lm

all: $(CEXECS)

$(CEXECS): %.out : %.c
	$(CC) $(CFLAGS) $< -o$@ $(LDFLAGS)

test: $(CEXECS)
	baygon

clean:
	$(RM) $(EXECS)

.PHONY: test all
