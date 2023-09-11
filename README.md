# PROYECTO CONSTRUCCIÓN Y EVOLUCIÓN DE SOFTWARE - GRUPO 5
## Integrantes:
- Kevin Condor
- Jackson Ramón
- Jean Villacis
## Descripción
La API ha sido diseñada para gestionar eficientemente información sobre libros permitiendo realizar las operaciones de crear, leer, actualizar y eliminar (CRUD). 

Se puede usar este recurso a traves de Postman o, a su vez, se puede utilizar la interfaz gráfica que genera la propia API debido a que fue creada usando el framework "FastAPI". En este caso, se hará uso de la interfaz que facilita FastAPI, más adelante, se explicará a detalle este apartado.
## Documentación
### Pasos previos
1. Descargar Python desde Microsoft Store (en Windows) o desde la página oficial de Python (https://www.python.org/downloads/).
2. Seleccionar una ubicación en el disco para clonar el repositorio de GitHub. 
3. Usando la herramienta Git Bash, moverse a la ubicación seleccionada para clonar.

    `cd "C:\Ruta_Ejemplo"`
4. Clonar el repositorio usando el comando:

    `git clone https://github.com/JeanPierreVillacis/ProyectoGrupo5CYESW.git`
5. Abrir el **Símbolo del sistema** (Windows) o la **Terminal** (Linux o Mac) y dirigirse al directorio donde se clonó el repositorio.
6. Crear un entorno virtual de Python, en este caso tendrá el nombre de apicys pero puede ser cualquiera.

    `python -m venv apicys-env`
7. Activar el entorno virtual.

    Windows: `apicys-env\Scripts\activate.bat`
    
    Linux o Mac: `source apicys-env/bin/activate`
8. Verificar que el entorno virtual esté activado, para esto se tiene que observar que en la linea de comandos se haya puesto el nombre del entorno virtual entre parentesis antes de la ruta sobre la que se esté trabajando, por ejemplo:

    `(apicys-env) C:\Ruta_Ejemplo`
9. Instalar **fastapi** y el servidor **uvicorn**.

    `pip install fastapi`

    `pip install uvicorn`
10. Levantar el servidor de **uvicorn** para comenzar a usar la API usando el siguiente comando.

    `uvicorn main:app --reload`

    En este caso, se está especificando a uvicorn que busque dentro del fichero *main.py* la variable *app* que deberá ser una instancia de la clase *FastAPI*.

Varias partes de la información presentada en este apartado no son de autoría del grupo de desarrollo. A continuación, se facilitan los enlaces a la documentación para la creación de **Entornos virtuales en Python** y para la instalación del framework **FastAPI**.

**Entornos virtuales en Python**: https://docs.python.org/es/3/tutorial/venv.html

**Framework FastAPI**: https://fastapi.tiangolo.com/

### Uso de la API
1. Tomar la dirección IP asiganada al momento de levantar el servidor de uvicorn.

    `Uvicorn running on ←[1mhttp://127.0.0.1:8000←[`
2. Pegar la dirección IP en cualquier navegador y de esta forma se podría empezar a interactuar con la API. No obstante, en este caso unicamente se podrán hacer peticiones GET.
3. Para trabajar con las demas peticiones HTTP se puede usar **Postman** o usar la **Interfaz Web** que provee FastAPI, para este caso, se usará la segunda opción mencionada.
4. Luego de ingresar la dirección IP en el navegador, especificar que se desea acceder al recurso **docs** de la API, como se muestra a continuación.

    `http://127.0.0.1:8000/docs`

    De esta forma, se accederá a una interfaz web como la que se muestra a continuación.

    ![Alt text](image.png)
