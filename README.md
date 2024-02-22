# plagiarism-detector
## Autores
Amananda Noris Hernández

Juan Miguel Pérez Martínez 

Marcos Antonio Pérez Lorenzo

## Descripción del problema
Nuestro problema consiste en desarrollar un detector de plagio entre dos documentos dados por el usuario.

## Consideraciones tomadas a la hora de desarrollar la solución
Se tuvo en cuenta la definicion de plagio y sus diferentes formas, así como varios métodos para detectarlo.

## Explicación de cómo ejecutar el proyecto. Posibles entradas de parámetros
 
Para ejecutar el proyecto basta correr en wsl /startup.sh y en windows, con ejecutar el archivo main.py .

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

-**Falsos positivos**: Nuestro programa suele devolver falsos positivos en documentos que son sacados de una misma fuente.

Mejoras propuestas:

-**Implementación de una métrica más adecuada**: Proponemos la búsqueda de una métrica para detección de plagio a partir de los valores analizados que muestre mejores resultados a la hora de filtrar falsos positivos.

-**Optimización de los modelos**: Proponemos trabajar en la optimización de los modelos de procesamiento de lenguaje natural utilizados.

-**Mejora de la inerfaz visual**: Proponemos ampliar la información que se le brinda al usuario mediante el mostrado de conclusiones a las que se llegan mediante el análisis de las métricas. Además planteamos un mejor manejo de las excepciones.
