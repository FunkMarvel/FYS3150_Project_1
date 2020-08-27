CC := g++
FLAGS := -Wall -O2 -march=native
LIBS := -larmadillo

.PHONY: all clean run

all: main.exe

main.exe: main.o
	$(CC) $(FLAGS) main.o -o main.exe $(LIBS)

main.o: main.cpp
	$(CC) $(FLAGS) main.cpp -c

clean:
	rm -f *.o
	rm -f *.exe

run:
	./main.exe

print-% : ; @echo $* = $($*)
