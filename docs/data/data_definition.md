# Definición de los datos

## Origen de los datos

El dataset utilizado para este proyecto proviene del Guangzhou Women and Children’s Medical Center y cuenta con un total de 5,856 imágenes de rayos X de tórax en formato JPEG, organizadas en tres categorías: neumonía viral, neumonía bacterial y normal. Además, estas imágenes se tomaron de pacientes pediátricos de entre uno y cinco años, como parte de su atención clínica rutinaria. El conjunto de datos se divide en carpetas de entrenamiento, prueba y validación, con subcarpetas que clasifican las imágenes según su categoría. Este dataset se encuentra disponible en la librería de Kaggle y es posible acceder al mismo mediante el siguiente enlace https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

La extracción de estos datos se hizo a través de la API de Kaggle.

## Especificación de los scripts para la carga de datos

La carga de datos se lleva a cabo mediante la API proporcionada por Kaggle, que permite acceder a la información disponible en su plataforma. Para abordar este proceso, se han definido dos clases principales: la primera está enfocada en la interacción con la API de Kaggle, mientras que la segunda se encarga de la gestión de archivos en el equipo o servidor.

## Referencias a rutas o bases de datos origen y destino

La ruta se obtiene directamente del enlace proporcionado en la plataforma de Kaggle, por ejemplo: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia. Sin embargo, el destino de los datos es una carpeta gestionada localmente en el mismo equipo, asegurándose de que no se encuentre incluida en el repositorio.

### Rutas de origen de datos

1. **Ubicación de los archivos de origen de los datos**  
   Los datos se obtienen directamente desde el repositorio público de Kaggle a través del enlace:  
   [https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).  
   Una vez descargados, los archivos se descomprimen en una carpeta local gestionada en el mismo equipo, asegurándose de que esta carpeta no esté incluida en el repositorio.

2. **Estructura de los archivos de origen de los datos**  
   El dataset se organiza en tres subcarpetas principales, cada una con un propósito específico:  
   - `./chest_xray/test`: Archivos de prueba.  
   - `./chest_xray/train`: Archivos de entrenamiento.  
   - `./chest_xray/val`: Archivos de validación.  

   En total, se contabilizaron **5856 archivos** distribuidos en estas carpetas. Las extensiones de los archivos dentro del dataset se identificaron mediante un análisis de sus rutas y son las siguientes: **{'.jpeg'}**.

3. **Procedimientos de transformación y limpieza de los datos**  
   - **Descarga y descompresión**: Los datos se descargan desde Kaggle utilizando el comando `kaggle datasets download` y luego se descomprimen con `unzip`.  
   - **Verificación de la estructura de los datos**: Se contó el número total de archivos en cada subcarpeta para asegurar la integridad del dataset.  
   - **Identificación de formatos**: Se analizó la estructura de archivos para determinar las extensiones presentes, asegurando la compatibilidad con los procesos posteriores.
   - Para estandarizar las imágenes correspondientes a las radiografías con neumonía viral en el conjunto de prueba (`./chest_xray/test`), se planeó calcular el promedio de la relación de aspecto. La relación de aspecto se define como:  
    Ancho = Relación de aspecto × 500, Alto = 500




### Base de datos de destino

Debido a la naturaleza de nuestra implementacion, no existe una base de datos a la cual cargar los datos.
