# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** *PNEURADNET* (Pneumonia radiograph net)
- **Plataforma de despliegue:** El endpoint con el modelo y la aplicación con interfaz estan desplegados en Railways.
- **Requisitos técnicos:** De hardware, se recomienda un minimo de 2 GB de ram y 1 vCPu core. Ademas, para otros requerimientos, es posible  mirar las respectivas listas de los paquetes. Es importante tener en cuenta que los requisitos principales se basan en que el equipo sea capaz de cargar el modelo. (Dado que esto se encuentra en un entorno web, el usuario final puede desentenderse de este apartado)
- **Requisitos de seguridad:** En este caso, la seguridad de la información de los datos y del proyecto está dada por los requerimientos de seguridad establecidos en la plataforma de despliegue. Adicionalmente, la transferencia de infomación de datos se realiza a través de protocolos seguros (https)
- **Diagrama de arquitectura:** En este caso, el servicio de lógica se encuentra desplegado como una API que puede recibir entradas del modelo a través de peticiones que se realizan a través de protocolos de red de la capa de aplicación. Del mismo modo modo, este servicio envía los resultados de la predicción usando el mismo mecanismo. A continuación, se muestra un esquema sencillo que muestar como se realiza dicha operación:

![Arquitectura](API.png)

## Código de despliegue

Para el despliegue, debemos tener en cuenta que se manejo una parte de la apliación de lógica con el modelo; y otra parte para la interacción gráfica del usuario. 

Para el caso del back que era aquel que disponía de los modelos, tenemos:

- **Archivo principal:** Main.py
- **Rutas de acceso a los archivos:** Debido a la naturaleza del proyecto y del proveedor del despliegue, todos los archivos se encuentran en la misma carpeta y disponen rutas simples.
Estos archivos son:
1. dataTranformation.py
2. Dockerfile
3. Procfile
4. requirements.txt

- **Variables de entorno:** api.

Para el caso del front que era aquel que disponía del entorno final para el usuarui, tenemos:

- **Archivo principal:** app.py
- **Rutas de acceso a los archivos:** Debido a la naturaleza del proyecto y del proveedor del despliegue (Que fue el mismo del backend), todos los archivos se encuentran en la misma carpeta y disponen rutas simples.
Estos archivos son:
1. Dockerfile
2. requirements.txt

- **Variables de entorno:** API_URL.

El código del backend fue manejado en un repositorio aparte a este. Este repositorio se puede encontrar en el siguiente enlace:

[Lógica de despliegue](https://github.com/dfadames/MLDS6_project_frontend_and_api)

Para el caso del front, el código se puede encontrar en la raíz de este proyecto.

El para acceder al servicio desplegado para el usuario final es: (Página desplegada)[https://mlds6projectt10-production.up.railway.app]

(Dichos servicios de back y front pueden estar deshabilitados dado el costo que implica mantenerlos)

## Documentación del despliegue

### **Instrucciones de instalación**  
Pasos generales:


1. **Instalar dependencias requeridas:**  
   Asegúrate de cumplir con las versiones exactas de las liberias que se encuentran en el requirements.txt,  ademas, en el entorno de desarollo se necesitaron otras dependencias explicitas en el archivo Dockerfile. 


2. **Configurar variables de entorno obligatorias:**  
   Para el correcto funcionamiento del despliegue, es necesario configurar algunas variables del entorno, estas son:
   ```bash
   export CUDA_VISIBLE_DEVICES=-1
   export TF_ENABLE_ONEDNN_OPTS=0
   ```

3. **Ejecutar el servidor:**  
   Ejecuta el servidor con `uvicorn`:  
   ```bash
   uvicorn main:app --reload
   ```  
   Aquí, `main` es el nombre del archivo que contiene el código FastAPI (sin extensión `.py`).

---

Pasos expecificos de railway:

1. **Asegurar la integridad de los archivos:** 
    Es necesario tener todos los archivos necesarios para el correcto despliegue, entre los cuales estan requirements.txt, Dockerfile y Procfile.  Cada uno da instrucciones 
    obligatorias para el correcto funcionamiento, no obstante, es bueno puntualizar que unicamente es necesario tenerlos en la carpeta raiz, no es necesario configurar ni ejecutar nada, railways se encarga de eso.
2. Esperar a que el el build y el despliegue se realicen con exito

### **Instrucciones de configuración**  

1. **Configurar recursos del modelo:**  
   - Es necesario aclarar que el modelo necesita como minimo 1 GB de ram y 1 vcpu para funcionar, no obstante, es recomendable tener una ram de 2 GB para evitar posibles problemas al momento de realizar la inferencia.

2. **Configurar rutas del modelo:**  
   - Es necesario asegurar  que la variable `MODEL_PATH` apunta a la ubicación correcta del archivo del modelo.

3. **Ajuste de preprocesamiento:**  
   - Configura las dimensiones deseadas para el redimensionamiento en `(500, 720)` según sea necesario, y de igual forma, verificar el correcto funcionamiento de las funciones de preprocesamiento en las imagenes. No obstante, el unico parametro verdaderamente "configurable" es la dimension.

4. **Puerto y host del servidor:**  
   - Es necesario configurar el puerto 8000 para el correcto funcionamiento, no obstante, en el despliegue de railways el archivo dockerfile se encarga de proporcionarlo.

---

### **Instrucciones de uso**  

1. **Subir imágenes:**  
    A traves de la interfaz grafica, se tiene la opcion de subir una imagen (sea en formato png, jpg, o jpeg) para el posterior procesamiento, tal como se puede ver a continuacion:
    ![alt text](image.png)
    ![alt text](image-1.png)
    Posteriormente, se da clic en predict para obtener los resultados y esperamos un par de segundos.
2. **Formato de respuesta:**  
   El servicio devolverá un JSON con:  
   - `filename`: Nombre del archivo subido.  
   - `predictions`: Array con las probabilidades de cada clase.  
   - `predicted_class`: Etiqueta de la clase con mayor probabilidad.  
   - `confidence`: Probabilidad asociada a la predicción.  
    No obstante, esta informacion es procesada por  el front dando como resultado una visualizacion mas amigable, tal que:
    ![alt text](image-2.png)

### **Instrucciones de mantenimiento**  

1. **Actualización del modelo:**  
   - Si actualizas el modelo, reemplaza el archivo `finalModel.keras` y reinicia el servidor.

2. **Revisión de dependencias:**  
   - Regularmente, ejecuta:  
     ```bash
     pip list --outdated
     ```  
     para identificar actualizaciones en las bibliotecas utilizadas.

3. **Monitoreo del servidor:**  
   - Railways permite dashboards que brindan la informacion necesaria para hacerle un seguimiento tanto a los recursos como a posibles cuellos de botella o errores que puedan surgir, por lo cual es importante mantenerse al tanto de los mismos

4. **Log de errores:**  
   - En caso de fallos, ademas, existe unos logs detallados que nos permiten trazar y entender de manera clara los problemas por los cuales la aplicacion pudo haber fallado.


