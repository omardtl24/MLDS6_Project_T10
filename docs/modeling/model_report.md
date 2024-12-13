# Reporte del Modelo Final

## Resumen Ejecutivo

Dados los modelos y sus analisis de rendimiento en base a las diferentes métricas, se eligió el modelo que VGG16 Version 1 como aquel que tiene mejor rendimiento y se busca tener listo para un ppsible despliegue.

En ese orden de ideas, definimos un pipeline que dada una imagen, la redimensione, la reescale y la ingrese al modelo para que aplique la predicción sobre la imagen de interés.

## Descripción del Problema

Se realiza una clasificación de imagenes donde las entradas corresponden al total de 5856 imágenes, redimensionadas a un tamaño de (1397,970) con un solo canal (escala de grises)

## Descripción del Modelo

Se realizó transfer-learning sobre un modelo pre-entrenado VGG16 para extraer las características de las imágenes; luego, el resultado de lo anterior, fue introducido en un modelo de capas densas que fue entrenado para realizar la tarea de clasificación en las clases codificadas como 0,1 y 2.

## Evaluación del Modelo

Para la evaluación del modelo final se tuvo en cuenta la métrica de curva AUC para la distinción de desempeño entre los respectivos modelos base. Además, para la selección final se considero el reporte de métricas de sci-kit que incluye precision, recall y f1-score.

## Conclusiones y Recomendaciones

El modelo VGG16 Version 1 fue seleccionado por su desempeño sobresaliente, logrando un balance adecuado entre precisión, recall y F1-score, especialmente en la clase "Normal", con un macro promedio de 0.75 y un accuracy del 76%. Su pipeline de preprocesamiento garantiza consistencia y facilidad de despliegue. Aunque es robusto para datos desbalanceados, identificamos que es indispensable mejorar el rendimiento en las clases "bacteriaPneumonia" y "virusPneumonia" mediante técnicas como aumento de datos o ajustes adicionales para optimizar su desempeño en aplicaciones críticas.
