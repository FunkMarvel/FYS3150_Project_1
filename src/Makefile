CC := g++
FLAGS := -Wall -O2 -march=native
LIBS := -larmadillo

.PHONY: all clean run

all: main.exe

main.exe: main.o general_algorithm.o special_algorithm.o relative_error.o general_main.o
	$(CC) $(FLAGS) main.o general_algorithm.o special_algorithm.o relative_error.o general_main.o -o main.exe $(LIBS)

main.o: main.cpp
	$(CC) $(FLAGS) main.cpp -c

general_algorithm.o: general_algorithm.cpp
	$(CC) $(FLAGS) general_algorithm.cpp -c

general_main.o: general_main.cpp
	$(CC) $(FLAGS) general_main.cpp -c

relative_error.o: relative_error.cpp
	$(CC) $(FLAGS) relative_error.cpp -c

special_algorithm.o: special_algorithm.cpp
	$(CC) $(FLAGS) special_algorithm.cpp -c

clean:
	rm -f *.o
	rm -f *.exe

run:
	./main.exe

print-% : ; @echo $* = $($*)
