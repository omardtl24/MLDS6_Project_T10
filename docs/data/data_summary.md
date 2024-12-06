# Reporte de Datos

## Resumen general de los datos
El dataset consta de 5856 imágenes de radiografías de rayos X de pecho divididas en tres conjuntos: entrenamiento (5216 imágenes), prueba (624 imágenes) y validación (16 imágenes). Las imágenes están en formato JPEG y tienen un tamaño total de 1.24 GB. 

## Resumen de calidad de los datos
El dataset muestra una alta calidad: no presenta imágenes faltantes, de mala calidad ni problemas de codificación. Todas las imágenes están bien organizadas y en formato uniforme. Sin embargo, se requiere balanceo de clases en los conjuntos de prueba y validación debido al desbalance entre las categorías. Además, se observa que las imágenes tienen dimensiones variables y algunas cuentan con 3 canales, mientras que otras tienen solo 1. Estos factores se tuvieron en cuenta en el preprocesamiento de los datos.

## Variable objetivo
La variable objetivo es la condición del paciente, categorizada como **NORMAL**, **VIRUS** y **BACTERIA**. Sin embargo, en la estructura de los datos solo se identifican las categorías **NORMAL** y **PNEUMONIA**, por lo que es importante verificar si la clasificación entre **VIRUS** y **BACTERIA** se maneja correctamente.

## Variables individuales
El dataset se compone únicamente de imágenes, sin variables individuales explícitas. Las características relevantes deben extraerse de las imágenes mediante técnicas de procesamiento de imágenes y modelos de aprendizaje profundo como las redes neuronales convolucionales (CNN).

## Ranking de variables
No se pueden aplicar técnicas de ranking de variables como la correlación o PCA directamente. Se deben usar redes neuronales profundas para aprender las características importantes de las imágenes y determinar su relevancia para la clasificación.

## Relación entre variables explicativas y variable objetivo
La relación entre las características visuales de las imágenes y la variable objetivo se modela mediante redes neuronales convolucionales (CNN), que permiten la extracción automática de patrones y la clasificación efectiva de las imágenes.
