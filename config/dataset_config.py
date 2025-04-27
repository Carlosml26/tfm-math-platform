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
    "DEA:Alumno con dificultades de aprendizaje (lectura/escritura/matemáticas)",
    "Superdotado:Alumno con alta capacidad intelectual y ritmo acelerado",
    "TDAH:Alumno con trastorno de atención con/sin hiperactividad",
    "Otro:Otro perfil educativo no especificado"
]

DIFICULTADES = [
    "Básico:Nivel introductorio, conceptos fundamentales",
    "Intermedio:Aplicación de conocimientos con cierto nivel de abstracción",
    "Avanzado:Ejercicios complejos, resolución no directa, requiere razonamiento"
]

TIPOS_ACTIVIDAD = [
    "Ejercicio:Aplicación directa, especificando claramente qué debe hacerse",
    "Problema:Planteamiento contextualizado que requiere razonamiento lógico"
]
