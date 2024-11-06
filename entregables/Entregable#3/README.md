El codigo consta de 2 partes:

1. La función recursiva
2. Obtención del número del usuario

La función recursiva lo que hace es tomar el número y multiplicarlo por la factorial(n-1), esto parara esta que n = 0.

Ejemplo n = 3:

Se hace un return de n * factorial(n-1) lo cual no es más que
3 * factorial(2) pero factorial(2) es igual a 2 * factorial(1) y factorial(1) es igual a  1 * factorial(0) y simplemente factorial(0) = 1 finalizando así el programa.

Reemplazando los datos nos queda que:
factorial(3) = 3*2*1*1 = 6

La segunda parte de este codigo es más simple, ya que simplemente se hace una solicitud de un número y se tranforma en un entero, ahora bien, si ese número es negativo, por la definición del factorial este no se puede, por lo tanto el programa devolvera que este valor no es positivo, y además si el valor ingresado no es un número el except devolvera esa indicación