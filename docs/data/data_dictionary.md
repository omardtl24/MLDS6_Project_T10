# Diccionario de datos

Nuestro conjunto de datos está compuesto por imágenes, cada una asociada a una clase específica. La relación entre las imágenes y sus clases no se encuentra en una tabla o archivo estructurado; en cambio, el dataset utiliza una organización basada en una jerarquía de directorios. Cada directorio representa una clase y contiene todas las imágenes correspondientes a esa categoría. Esta estructura permite identificar fácilmente la clase a la que pertenece cada imagen según su ubicación dentro del sistema de archivos. Considerando esta representación, se plantea el siguiente diccionario de datos:

## Datos extraídos de Kaggle

Los datos utilizados son las imágenes correspondientes al dataset [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia), el cual contiene imágenes organizadas según la definición de datos mencionada.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
|----------|-------------|--------------|------------------------|-----------------|
| Imagen   | Imagen asociada a la muestra de la radiografía a analizar | Imagen JPG | Tres canales (RGB) de diferentes dimensiones | [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) |
| Clase    | Clase a la cual la radiografía pertenece | String | Normal, Neumonía Viral, Neumonía Bacteriana | [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) |


