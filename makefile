pde.png: ejercicio5.dat pde.py pde.cpp
	python pde.py

%.dat : a.out
	./a.out

a.out: pde.cpp
	c++ pde.cpp

clean:
	rm evolve_A.dat evolve_A.png evolve_B.dat evolve_B.png evolve_C.dat evolve_C.png evolve_D.dat evolve_D.png a.out
