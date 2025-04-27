"""
Contiene configuraciones de datos fijos:
- Temas y subtemas
- Perfiles de alumno
- Dificultad
- Tipo de actividad
"""

TEMAS_SUBTEMAS = {
    "Geometría:Estudio de formas, figuras y sus propiedades": [
        "Polígonos y Triángulos:Clasificación y propiedades de triángulos y figuras poligonales",
        "Cuadriláteros:Estudio de paralelogramos, trapecios y rombos",
        "Circunferencia y Círculo:Elementos, ángulos y áreas en figuras circulares",
        "Semejanza y Escalas:Proporciones entre figuras semejantes y reducción/ampliación de figuras",
        "Ángulos y Transformaciones Geométricas:Giros, simetrías, traslaciones y sus efectos sobre ángulos"
    ],
    "Ecuaciones:Resolución de igualdades algebraicas": [
        "Ecuaciones de Primer Grado:Igualdades con incógnitas de primer grado",
        "Ecuaciones de Segundo Grado:Resolución con fórmula general o factorización",
        "Sistemas de Ecuaciones Lineales (2x2):Solución de sistemas con dos incógnitas",
        "Ecuaciones Exponenciales o Racionales:Ecuaciones con potencias o fracciones algebraicas"
    ]
}

PERFILES = [
    "Base:Alumno promedio sin necesidades específicas",
    "DEA:Alumno con dificultades de aprendizaje (lectura/escritura/matemáticas). El ejercicio y la solucion deben remarcarse en la lectura y escritura. Da pistas.",
    "Superdotado:Alumno con alta capacidad intelectual y ritmo acelerado. El ejercicio tiene que ser más complejo y la solución mas matematica.",
    "TDAH:Alumno con trastorno de atención con/sin hiperactividad. El ejercicio tiene que tener un lenguaje claro, directo y llamativo.",
    "Otro:Otro perfil educativo no especificado"
]

DIFICULTADES = [
    "Básico:Nivel introductorio, conceptos fundamentales",
    "Intermedio:Aplicación de conocimientos con cierto nivel de abstracción",
    "Avanzado:Ejercicios complejos, resolución no directa, requiere razonamiento"
]

TIPOS_ACTIVIDAD = [
    "Ejercicio: Resolución de una tarea con datos explícitos y procedimientos conocidos, sin necesidad de interpretar la situación.",
    "Problema: Situación abierta que requiere interpretar los datos, analizar la información y decidir qué estrategias aplicar para llegar a una solución."
]
