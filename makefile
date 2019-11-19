pde.png: ejercicio5.dat pde.py pde.cpp
	python pde.py

%.dat : a.out
	./a.out

a.out: pde.cpp
	c++ pde.cpp

clean:
	rm ejercicio5.dat pde.png a.out
