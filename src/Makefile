CC := g++
FLAGS := -Wall -O2 -march=native
LIBS := -larmadillo
OFILES := *.o

.PHONY: all clean run

all: main.exe

main.exe: $(OFILES)
	$(CC) $(FLAGS) $(OFILES) -o main.exe $(LIBS)

*.o: *.cpp
	$(CC) $(FLAGS) *.cpp -c

clean:
	rm -f *.o
	rm -f *.exe

run:
	./main.exe

print-% : ; @echo $* = $($*)
