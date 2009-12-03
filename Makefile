CFLAGS=-fPIC -O3

all: lookup3.so

lookup3.so: lookup3.o
	$(CC) -shared -Wl,-soname,jenkins -o lookup3.so lookup3.o

lookup3.o: lookup3.c
	$(CC) $(CFLAGS) -c $< -o lookup3.o

clean:
	\rm -f *.o *.so
