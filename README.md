# plagiarism-detector
## Autores
Amananda Noris Hernández

Juan Miguel Pérez Martínez 

Marcos Antonio Pérez Lorenzo

## Descripción del problema
Nuestro problema consiste en desarrollar un detector de plagio entre dos documentos dados por el usuario 

## Consideraciones tomadas a la hora de desarrollar la solución
Se tuvo en cuenta la definicion de plagio y los diferentes tipos de este que existen 
## Explicación de cómo ejecutar el proyecto. Posibles entradas de parámetros
 
Para ejecutar el proyecto basta correr en wsl /startup.sh en windows basta con ejecutar el archivo main.py

## Explicación de la solución desarrollada

La solución desarrollada es un detector de plagio basado en la similitud léxica y semántica de los textos. Aquí te explico cada parte del código:

1. **Preprocesamiento de texto**: Se utiliza la clase `TextPreprocessor` para preprocesar los textos. Esta clase realiza varias operaciones de preprocesamiento, como convertir el texto a minúsculas, eliminar la puntuación, expandir las contracciones, eliminar las palabras de parada, raíces de palabras y lematización.

2. **Vectorización de texto**: Se utiliza la clase `SemanticVectorizer` para vectorizar los textos. Esta clase utiliza el modelo BERT preentrenado para convertir los textos en vectores semánticos.

3. **Detección de plagio**: Se utiliza la clase `PlagiarismDetector` para detectar el plagio. Esta clase divide los textos en segmentos y compara cada segmento del primer texto con cada segmento del segundo texto. Si la similitud de dos segmentos es mayor que un umbral dado, se considera que hay plagio.

4. **Cálculo de similitud léxica y semántica**: Se utilizan las funciones `calcular_similitud_coseno` y `calcular_similitud_semantica` para calcular la similitud léxica y semántica entre los textos. La similitud léxica se calcula utilizando el vectorizador TF-IDF y la similitud coseno, mientras que la similitud semántica se calcula utilizando el modelo Word2Vec.

5. **Interfaz de usuario**: Se utiliza Flask para crear una interfaz de usuario web donde los usuarios pueden subir dos documentos para comparar. Los documentos se cargan en el servidor, se preprocesan y se comparan para detectar el plagio. Los resultados se muestran en la página web.

En cuanto a las definiciones matemáticas de los algoritmos utilizados:

- **Vectorización TF-IDF**: El vectorizador TF-IDF (Term Frequency-Inverse Document Frequency) convierte el texto en un vector de números reales. Cada número representa la importancia de una palabra en el texto. Las palabras que aparecen con frecuencia en el texto pero raramente en otros documentos tienen un número más alto.

- **Similitud Coseno**: La similitud coseno es una medida de la similitud entre dos vectores. Se calcula como el coseno del ángulo entre los dos vectores. Un valor de  1 indica una similitud perfecta, mientras que un valor de  0 indica que los vectores son ortogonales (no tienen ninguna similitud).

- **Modelo Word2Vec**: Word2Vec es un modelo de aprendizaje automático que se utiliza para aprender representaciones vectoriales de palabras. Cada palabra se representa como un vector en un espacio de alta dimensión. Las palabras que tienen significados similares se agrupan cerca en el espacio de representación.

- **BERT**: BERT (Bidirectional Encoder Representations from Transformers) es un modelo de aprendizaje automático para el procesamiento del lenguaje natural. A diferencia de otros modelos, BERT toma en cuenta el contexto en el que se utiliza una palabra. Esto significa que BERT puede entender la semántica de las palabras y puede generar representaciones más precisas de las palabras.

En resumen, la solución desarrollada utiliza una combinación de técnicas de preprocesamiento de texto, vectorización de texto y comparación de similitud para detectar el plagio en los textos.

## Insuficiencias de la solución y mejoras propuestas:

-**Insuficiente Prueba de Calidad y Corrección de Errores**: La detección de plagio es un proceso complejo y puede ser propenso a errores, especialmente si el texto contiene jerga o terminología especializada. Además, el rendimiento de la detección de plagio puede verse afectado por la calidad de las pruebas realizadas 12.
-**Falta de Automatización de Pruebas**: La detección de plagio puede ser un proceso intensivo en tiempo y recursos. La automatización de pruebas podría mejorar la eficiencia y permitir un análisis más rápido y exhaustivo 12.
-**Complejidad del Código**: El código proporcionado es bastante extenso y podría ser difícil de mantener y entender. La simplificación del código y la modularización podrían mejorar la legibilidad y facilitar la colaboración 2.
-**Seguridad de Datos**: Si el sistema maneja documentos sensibles, es crucial implementar medidas de seguridad robustas para proteger la información del usuario. Esto incluye el cifrado de datos y la autenticación de usuarios 2.
-**Gestión del Desarrollo Técnico**: La acumulación de deuda técnica puede afectar la productividad y la escalabilidad del sistema. Es importante priorizar la refactorización y las revisiones de código para manejar la deuda técnica y mantener un software estable y mantenible 2.
-**Influencias en el Diseño del Producto**: El diseño del producto debe ser flexible para adaptarse a los cambios sin necesidad de rediseñar la solución completa. Además, se deben considerar las necesidades y expectativas del usuario para proporcionar una experiencia consistente en todas las plataformas y dispositivos 4.
-**Mantenimiento de la Competitividad**: Es importante innovar y mejorar continuamente los productos y servicios para mantenerse al día con los avances tecnológicos y las demandas del mercado. Esto incluye la monitorización de las últimas tendencias y la exploración de nuevas tecnologías 5.

Mejoras propuestas:

-**Implementar Pruebas Automatizadas**: Adoptar herramientas de pruebas automatizadas puede ahorrar tiempo y mejorar la eficiencia del proceso de detección de plagio 12.
-**Refactorización y Revisión de Código**: Priorizar la refactorización y las revisiones de código puede ayudar a mejorar la legibilidad del código y facilitar la colaboración 2.
-**Mejorar la Seguridad**: Implementar prácticas de seguridad robustas, como el cifrado y la autenticación, para proteger la información del usuario 2.
-**Gestión Eficaz de la Deuda Técnica**: Dedicar tiempo para la refactorización y las revisiones de código, y priorizar las prácticas de código limpio pueden ayudar a manejar la deuda técnica y mantener un software estable y mantenible 2.
-**Diseño de Producto Flexible**: Considerar un diseño de producto flexible que pueda adaptarse a los cambios y proporcionar una experiencia de usuario coherente en todas las plataformas y dispositivos 4.
-**Innovación y Mejora Continua**: Mantenerse al día con los avances tecnológicos y las demandas del mercado a través de la innovación y la mejora continua puede ayudar a mantener la competitividad 5.
