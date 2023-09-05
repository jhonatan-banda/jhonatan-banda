Se trata de un esquema desarrollado por IBM para clasificar defectos con el fin de proveer
retroalimentación sobre el progreso de un proyecto, a través del mismo. El objetivo de su
creación es obtener un paradigma para medir las relaciones causa-efecto de los defectos,
donde se pudiera encontrar la causa raíz de un defecto. Al mismo tiempo se deseaba desarrollar
una clasificación de defectos que fuera simple y que estuviera lo más libre posible de errores humanos.

A partir de las investigaciones que permitieran obtener esta clasificación se demostró que al
clasificar de forma única los defectos utilizando un conjunto de tipos de defectos que reflejaran
la semántica de las reparaciones hechas, se puede asociar los tipos de defectos con las fases de desarrollo.

ODC significa esencialmente que se clasifica a un defecto en uno de varios posibles tipos,
los cuales apuntan a la parte del proceso que necesita atención.Para esto se agregó dos atributos
a los defectos: tipo de defecto y desencadenador (trigger) de un defecto.

Los tipos de defectos definidos son:
-Función. Afecta las interfaces de usuario, las interfaces del producto, las interfaces con el hardware, y las estructuras de datos.
Requiere un cambio formal en el diseño.
- Asignación. Generalmente indica errores en el código, al inicializar o asignar valores de variables o estructuras de datos.
- Interfase. Se refiere a errores en las interacciones entre componentes, módulos u otros dispositivos a través de las llamadas a funciones, paso de parámetros, etc.
- Chequeo. Errores en la lógica del programa, el cual no hace la verificación de los datos y valores antes de ser usados.
- Serialización/temporal. Errores que tienen que ver con los recursos compartidos y de tiempo real.
- Construcción/Empaquetado (Build/Package/Merge). Errores que ocurren debido a problemas en las librerías, así como problemas en el control de cambios y versiones.
- Documentación. Errores que pueden afectar a la documentación de los artefactos o al mantenimiento del sistema.
- Algoritmo. Problemas de eficiencia o corrección de una tarea, a través del algoritmo que define a esa tarea.

El objetivo de los tipos de defectos también es poder relacionar cada tipo con algunas de las
fases del proceso de desarrollo. Se trata de determinar dónde fueron inyectados los defectos en el sistema.
Se encontró que cada tipo de defecto tiende a ser inyectado en relativamente pocas áreas o fases de desarrollo.
Por ejemplo, los defectos de asignación tienden a ser inyectados en su mayoría en la fase de codificación,
y los defectos de algoritmo tienden a ser inyectados especialmente en la fase de diseño de bajo nivel.

La asociación encontrada entre los tipos de defectos y el proceso de desarrollo
se muestra en la siguiente tabla: 

----------------------------------------------------------
|Tipo de defecto           |Asociación al proceso.       |

|Función                   |Diseño                       |

|Interfase                 |Diseño de bajo nivel         |

|Chequeo                   |Diseño de bajo nivel o código|

|Asignación                |Código                       |

|Serialización y temporales|Diseño de bajo nivel         |

|Construcción/Empaquetado  |Librerías                    |

|Documentación             |Documentación                |

|Algoritmo                 |Diseño de bajo nivel         |

----------------------------------------------------------

Al final de cada fase de desarrollo, se generan gráficas que muestran el número de defectos de cada tipo encontrados en esa fase. 
