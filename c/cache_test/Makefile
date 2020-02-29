CC=clang
LD=clang

OPT_LEVEL=-Ofast -march=native -flto -mavx -mavx2 -mfma -ffp-contract=fast -ffast-math -fomit-frame-pointer

CC_OPTS=$(OPT_LEVEL) -fPIC -Wall -Wno-unused-variable -Werror -Wfatal-errors
LD_OPTS=$(OPT_LEVEL) -lm -lc

HEADERS:=$(wildcard *.h) Makefile

.SUFFIXES:

TARGETS=main
all : $(TARGETS)

%.o: %.c $(HEADERS)
	$(CC) -c $< -o $@ $(CC_OPTS)
	$(CC) -c $< -o $@.s -masm=intel -S $(CC_OPTS)

%: %.o main.o
	$(LD) $^ -o $@ $(LD_OPTS)

clean:
	rm -rf $(TARGETS) *.o
