![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# SAMU REST API

## ESTRUCTURA DE CARPETAS
```
SAMU_BACKEND
│ .gitignore
│ integration_script.py
│ manage.py
│ Readme.MD
│ requirements.txt
│
├───apps
│ ├───uploadcsv
│ │ │ admin.py
│ │ │ apps.py
│ │ │ custom_errors.py
│ │ │ mixins.py
│ │ │ models.py
│ │ │ serializers.py
│ │ │ sucesss_custom.py
│ │ │ testOperation.py
│ │ │ tests.py
│ │ │ urls.py
│ │ │ utils.py
│ │ │ views.py
│ │ │ **init**.py
│ │ │
│ │ └───views
│ │ maestro_actividad_views.py
│ │ maestro_centropoblado_views.py
│ │ maestro_colegio_views.py
│ │ maestro_condicion_contrato_views.py
│ │ maestro_cpms_views.py
│ │ maestro_establecimiento_views.py
│ │ maestro_etnia_views.py
│ │ maestro_financiador.py
│ │ maestro_NOMINAL_relations_views.py
│ │ maestro_otra_condicion_views.py
│ │ maestro_paciente_relation.py
│ │ maestro_pais_views.py
│ │ maestro_personal_relation_views.py
│ │ maestro_profesion_relation_views.py
│ │ maestro_registrador_relation_views.py
│ │ maestro_tipodoc_views.py
│ │ maestro_ubigeo_views.py
│ │ maestro_ups_views.py
│ │ **init**.py
│ │
│ └───user
│ admin.py
│ apps.py
│ countries.py
│ languages.py
│ models.py
│ serializers.py
│ tests.py
│ views.py
│ **init**.py
│
├───core
│ .env
│ .env.example
│ asgi.py
│ settings.py
│ urls.py
│ wsgi.py
│ **init**.py
│
├───env
└───render
build.sh
```
## RUTAS DE LA REST API

- **Centro Poblado**
  - `upload-csv-centropoblado`
  - `delete-all-centropoblado`
  - `get-all-centropoblado`
- **Colegios**
  - `upload-csv-colegios`
  - `delete-all-colegios`
  - `get-all-colegios`
- **Condición Contrato**
  - `upload-csv-condicioncontrato`
  - `delete-all-condicioncontrato`
  - `get-all-condicioncontrato`
- **CPMS**
  - `upload-csv-cpms`
  - `delete-all-cpms`
  - `get-all-cpms`
- **Tipo Documento**
  - `upload-csv-tipodoc`
  - `delete-all-tipodoc`
  - `get-all-tipodoc`
- **Establecimiento**
  - `upload-csv-establecimiento`
  - `delete-all-establecimiento`
  - `get-all-establecimiento`
- **Etnias**
  - `upload-csv-etnias`
  - `delete-all-etnias`
  - `get-all-etnias`
- **Otra Condición**
  - `upload-csv-otra-condicion`
  - `delete-all-otra-condicion`
  - `get-all-otra-condicion`
- **Ubigeo**
  - `upload-csv-ubigeo`
  - `delete-all-ubigeo`
  - `get-all-ubigeo`
- **UPS**
  - `upload-csv-ups`
  - `delete-all-ups`
  - `get-all-ups`
- **Financiador**
  - `upload-csv-financiador`
  - `delete-all-financiador`
  - `get-all-financiador`
- **País**
  - `upload-csv-pais`
  - `delete-all-pais`
  - `get-all-pais`
- **Profesión**
  - `upload-csv-profesion`
  - `delete-all-profesion`
  - `get-all-profesion`
- **Registrador**
  - `upload-csv-registrador`
  - `delete-all-registrador`
  - `get-all-registrador`
- **Personal**
  - `upload-csv-personal`
  - `delete-all-personal`
  - `get-all-personal`
- **Paciente**
  - `upload-csv-paciente`
  - `delete-all-paciente`
  - `get-all-paciente`
- **Nominal Test**
  - `upload-csv-nominal_test`
  - `delete-all-nominal_test`
  - `get-all-nominal_test`
    ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Vistas (Ejemplo de vistas de un Modelo)

### MAESTRO_HIS_PROFESION_CSV_View

Esta vista se encarga de procesar y cargar los datos de un archivo CSV en el modelo MAESTRO_HIS_PROFESION.

**Método:**

- `post()`: Recibe un archivo CSV y procesa sus datos para cargarlos en el modelo MAESTRO_HIS_PROFESION. Si el proceso es exitoso, devuelve un mensaje indicando cuántos registros se agregaron. Si se encuentra un error durante el proceso, se devuelve un mensaje de error con detalles.

### MAESTRO_HIS_PROFESION_Delete_View

Esta vista se encarga de eliminar todos los registros del modelo MAESTRO_HIS_PROFESION.

**Método:**

- `delete()`: Elimina todos los registros del modelo MAESTRO_HIS_PROFESION y reinicia los contadores de secuencia de la tabla.

### MAESTRO_HIS_PROFESION_List_View

Esta vista se encarga de listar los registros del modelo MAESTRO_HIS_PROFESION.

**Método:**

- `get()`: Devuelve una lista paginada de los registros del modelo MAESTRO_HIS_PROFESION, utilizando el serializador MAESTRO_HIS_PROFESION_Serializer y la clase de paginación CustomPageNumberPagination.
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## FUNCIONES Y CLASES

## Clase DataValidator

La clase `DataValidator` se encarga de validar, leer y limpiar los datos contenidos en un archivo CSV.

### Atributos:

- `data`: DataFrame de pandas que contiene los datos del archivo CSV.
- `file`: Archivo CSV a procesar.
- `count_data_orignal_csv`: Cantidad de registros en el archivo CSV original.
- `count_part_data`: Cantidad de registros en el DataFrame después de dividirlo (si se aplica).
- `count_data_processing`: Cantidad de registros en el DataFrame después de la limpieza y procesamiento.

### Métodos:

- `indexar()`: Agrega una columna 'Id' al DataFrame con valores secuenciales.
- `validate_file_type()`: Verifica si el archivo proporcionado es de tipo CSV. Si no lo es, genera un error personalizado.
- `read_csv_file(delimiter=";", encoding='utf-8')`: Lee el archivo CSV utilizando el delimitador y la codificación proporcionados.
- `clean_data(columns_to_string=[], columns_to_int=[], columns_to_float=[])`: Limpia el DataFrame convirtiendo los valores faltantes a None y convirtiendo las columnas a los tipos de datos correspondientes (int, float, str).
- `replace_none_strange_values(values_=[])`: Reemplaza los valores extraños que representan valores faltantes o nulos en el DataFrame con None.
- `split_data(num)`: Divide el DataFrame para mantener solo las primeras `num` filas.

## Clase ObjectOperations

La clase `ObjectOperations` se encarga de validar y operar con los datos del DataFrame.

### Atributos:

- `data`: DataFrame de pandas que contiene los datos.
- `field_names`: Lista de nombres de campos del modelo de Django asociado.

### Métodos:

- `validate_columns(expected_columns)`: Verifica si las columnas del DataFrame coinciden con las columnas esperadas. Si no coinciden, genera un error personalizado.
- `get_field_names_from_instance(instance: models.Model)`: Obtiene los nombres de los campos del modelo de Django proporcionado y los almacena en el atributo `field_names`.

## Clase ServiceDatabase

La clase `ServiceDatabase` se encarga de crear objetos del modelo de Django a partir de los datos del DataFrame y guardarlos en la base de datos.

### Atributos:

- `data`: DataFrame de pandas que contiene los datos.
- `model`: Modelo de Django al que se agregarán los datos.
- `identifier_field`: Campo identificador utilizado para filtrar objetos duplicados.
- `added_objects_count`: Cantidad de objetos creados a partir del DataFrame.
- `objects`: Lista de objetos creados a partir del DataFrame.
- `data_count_save`: Cantidad de registros en la base de datos después de guardar los objetos.
- `count_data_before`: Cantidad de registros en la base de datos antes de guardar los objetos.

### Métodos:

- `create_objects_from_data_nominal(foreign_keys=None)`: Crea objetos del modelo de Django a partir del DataFrame, considerando las relaciones de clave foránea.
- `create_objects_from_data()`: Crea objetos del modelo de Django a partir del DataFrame sin considerar relaciones de clave foránea.
- `saveData(ignore_conflicts=False)`: Guarda los objetos creados en la base de datos utilizando `bulk_create()`.

Esta documentación proporciona una descripción general de cada clase y sus métodos. Puede usar esta información para comprender el propósito y la funcionalidad del código
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## FUNCIONALIDAD DE UNA VISTA PARA SUBIR UN CSV

## Vista MAESTRO_HIS_PROFESION_CSV_View

La clase `MAESTRO_HIS_PROFESION_CSV_View` es una vista de API que se encarga de procesar archivos CSV subidos y guardar los datos en el modelo `MAESTRO_HIS_PROFESION`.

### Métodos:

- `post(request)`: Este método se ejecuta cuando se realiza una solicitud POST a la vista de API. Procesa el archivo CSV y guarda los datos en el modelo `MAESTRO_HIS_PROFESION`.

  - **Parámetros**:

    - `request`: Objeto de solicitud HTTP que contiene el archivo CSV y otros datos relacionados con la solicitud.

  - **Pasos del método**:

    1. Define el modelo `MAESTRO_HIS_PROFESION` y crea una instancia de este modelo.
    2. Define el campo identificador `Id_Profesion`.
    3. Intenta realizar las siguientes operaciones:
       a. Leer el archivo CSV de la solicitud.
       b. Crear un objeto `DataValidator` para procesar el archivo CSV.
       c. Validar el tipo de archivo y leer el contenido del archivo CSV.
       d. Limpiar y reemplazar los valores nulos en los datos del DataFrame.
       e. Crear un objeto `ObjectOperations` para realizar operaciones en el DataFrame.
       f. Validar las columnas del DataFrame con las columnas esperadas del modelo.
       g. Crear objetos del modelo a partir de los datos del DataFrame utilizando la clase `ServiceDatabase`.
       h. Guardar los objetos creados en la base de datos.
       i. Devolver una respuesta HTTP con información sobre el proceso y los registros agregados.

  - **Manejo de errores**:

    El método maneja varios tipos de errores, como errores personalizados (`CustomError`), errores de validación (`ValidationError`), errores de clave (`KeyError`), errores de valor (`ValueError`), errores de tipo (`TypeError`) y errores genéricos (`Exception`). Cada tipo de error devuelve una respuesta HTTP con un mensaje de error y un código de estado 400 (BAD REQUEST).

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Mixins y dependencias:

- `APIView`: Clase base de Django REST Framework para vistas de API.
- `MAESTRO_HIS_COLEGIO`: Modelo relacionado que representa el colegio asociado a la profesión.
- `MAESTRO_HIS_PROFESION`: Modelo principal en el que se guardarán los datos del archivo CSV.
- `MAESTRO_HIS_PROFESION_Serializer`: Serializador utilizado para convertir los objetos del modelo en representaciones JSON.
- `DataValidator`: Clase utilizada para validar, leer y limpiar los datos del archivo CSV.
- `ObjectOperations`: Clase utilizada para realizar operaciones y validaciones en los datos del DataFrame.
- `ServiceDatabase`: Clase utilizada para crear objetos del modelo y guardarlos en la base de datos.
- `CustomPageNumberPagination`: Clase utilizada para paginar los resultados de la API.
- `ResultType`: Clase utilizada para representar el resultado del proceso.
- `SuccessType`: Enumeración que define los tipos de éxito en el proceso.

## MEMASOS

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/240255574_910327919920724_8106483054201585770_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=DhmS_N8oB6wAX8pnale&_nc_ht=scontent.fpio2-1.fna&oh=00_AfD3slQS_Ibdr0rGuOkfSxk4BrCj7uPYXm5dWGkTEeYb0Q&oe=645A17B9)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/239930870_908542000099316_4233707510567284201_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=nT7UECgM2rMAX92vDGh&_nc_ht=scontent.fpio2-1.fna&oh=00_AfC8eHGojpQTEOYZ05fPesF41DvwsGUL8X17j5adsoL7iQ&oe=645B28A0)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/240657496_911703873116462_4020472033319140915_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=wjcUnsS5EyYAX8nsOy4&_nc_ht=scontent.fpio2-1.fna&oh=00_AfDUp81L8FoxFIK7Jiaq6W8Z7OdG6e09OxkJCo5pZ-S06g&oe=645A0CB4)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/240740051_918994772387372_7208755643465731788_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=ECHSrbJAxl8AX9bVfEw&_nc_ht=scontent.fpio2-1.fna&oh=00_AfBXW0gn4zgxBcFetP-PI1WgT3S4qJIY08-G_7IYE6GniQ&oe=645A26BA)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/242043746_924012495218933_557887158828996793_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=KBIxsRKoezQAX9FHNxf&_nc_ht=scontent.fpio2-1.fna&oh=00_AfBPORVJJKW5g8qCVEPYdw0OsaZSeq05FAC4qjMh-XDD_A&oe=645A58EE)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/242223188_926022975017885_5957921541138286474_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=y2OY34sYdJYAX_ExEtj&_nc_ht=scontent.fpio2-1.fna&oh=00_AfDTOqUfHaXvSbRGSb6J_iFLnegxwNnOQxT9Z4lygZNH7Q&oe=645AC274)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/242149845_929320868021429_5201173932227002325_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=PqK9zPbpkmkAX-Af9DU&_nc_ht=scontent.fpio2-1.fna&oh=00_AfBQqbbEkJC5o82OKsKhcygItnec6jZIzvLdDS8qQOQ2Ug&oe=645B765F)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/242322437_929321418021374_5169658895339138252_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=zFotOEaI16AAX_2SWun&_nc_ht=scontent.fpio2-1.fna&oh=00_AfASpzhDVyUnRa4qMztHCJ53l_HwUoi-jBUCIUpj52bNsg&oe=645A038B)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/243347145_932868760999973_7768603834086409592_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=7kp_t5HJMg4AX8sirH4&_nc_ht=scontent.fpio2-1.fna&oh=00_AfAVPSi87vtPc2gFo-XuZqALjoS293kKyDkwBZV4lkSGCg&oe=645A906A)

![](https://scontent.fpio2-1.fna.fbcdn.net/v/t39.30808-6/245091390_939707243649458_3359903494443819469_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=AuEWgKvOyz0AX_M8I2I&_nc_ht=scontent.fpio2-1.fna&oh=00_AfDdU81_mxQSou-7eoGEid2doYZuzcoXrwjfoaqxffozVA&oe=645AB2AC)
