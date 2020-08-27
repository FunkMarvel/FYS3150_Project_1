CC := g++
FLAGS := -Wall -O2
LIBS := -larmadillo

.PHONY: all clean

all: main.exe

main.exe: main.o
    $(CC) main.o $(LIBS) -o main.exe

main.o: main.cpp
    $(CC) $(FLAGS) main.cpp -c $(LIBS)

clean:
    rm -f *.o
    rm -f *.exe

print-% : ; @echo $* = $($*)
