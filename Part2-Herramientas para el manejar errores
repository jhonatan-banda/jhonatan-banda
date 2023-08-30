Sin embargo las excepciones son un mecanismo incorporado en C++ para traer los problemas a la superficie y
poder manejarlos para prevenir que un programa finalice por un fallo.
El siguiente código muestra como provocar una excepción y capturarla dentro de un bloque try-catch:

try {
    throw 0;
}
catch(int ex) 
{
    std::cout << "Excepcion: " << ex << std::endl;
}

Cuando se lanza una excepción, el controlador finaliza inmediatamente el bloque try y las variables locales son liberadas
sin embargo los punteros se pierden de la memoria:

#include <iostream>

class Test
{
public:
    Test() = default;
    ~Test() { std::cout << "Destructor" << std::endl; }
};

main()
{
    try
    {
        Test *t_ptr = new Test(); // memoria dinámica
        throw 0;
    }
    catch (int ex)
    {
        // El objeto t_ptr se ha perdido y ya no se puede liberar
        std::cout << "Excepcion: " << ex << std::endl;
    }
}

En C++, si una excepción no se ha capturado en ningún lugar, se llamará la función std::terminate() de la biblioteca <exception>.
Esta función llamará a la función std:abort() de <cstdlib> y matará el programa.

Podemos configurar esta función a nuestro gusto en caso de necesitarlo por alguna razón:
#include <iostream>
#include <exception>
#include <cstdlib>
#include <thread>
#include <chrono>

void terminar_programa()
{
    for (int i{3}; i > 0; i--)
    {
        std::cout << "Finalizando programa en " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "Programa abortado";
    std::abort();
}

main()
{
    // Configuramos la función terminal
    std::set_terminate(&terminar_programa);

    // Provocamos una excepción no manejada
    throw;
}
