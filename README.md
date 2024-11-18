Gestión de Encuestas

Este proyecto es una aplicación de escritorio para la gestión de encuestas, desarrollada en Python utilizando Tkinter para la interfaz gráfica y MySQL para la base de datos.

Requisitos

- Python 3.x
- Tkinter
- MySQL
- pip (Python package installer)

Instalación

1. Clonar el repositorio

git clone https://github.com/adrianlopez26/gestion-de-encuestas.git
cd gestion-de-encuestas

2. Instalar dependencias

Instalar las dependencias necesarias utilizando pip:

pip install -r requirements.txt

3. Instalar Tkinter

Tkinter generalmente viene preinstalado con Python. Si no lo tienes, puedes instalarlo con:

- Windows:

pip install tk

- Linux:

sudo apt-get install python3-tk

4. Instalar MySQL

Sigue las instrucciones en el sitio oficial de MySQL para instalar MySQL en tu sistema operativo: https://dev.mysql.com/doc/refman/8.0/en/installing.html

5. Configurar la base de datos

1. Inicia sesión en MySQL:

mysql -u root -p

2. Crea una base de datos para el proyecto:

CREATE DATABASE gestion_encuestas;

3. Usa la base de datos creada:

USE gestion_encuestas;

4. Importa el archivo SQL para crear las tablas y datos necesarios:

source path/to/Resources/bd.sql;

6. Configurar la conexión a MySQL

Edita el archivo `config.py` para incluir tus credenciales de MySQL:

# config.py
MYSQL_HOST = 'localhost'
MYSQL_USER = 'tu_usuario'
MYSQL_PASSWORD = 'tu_contraseña'
MYSQL_DB = 'gestion_encuestas'

Ejecución

1. Ejecutar la aplicación

Para iniciar la aplicación, ejecuta el siguiente comando:

python Repository/interfaz.py

2. Operaciones CRUD

- Agregar Encuesta: Completa los campos de entrada y haz clic en "Agregar Encuesta".
- Ver Encuestas: Haz clic en "Ver Encuestas" para cargar y mostrar todas las encuestas en la tabla.
- Actualizar Encuesta: Selecciona una encuesta de la tabla, edita los campos y haz clic en "Actualizar Encuesta".
- Eliminar Encuesta: Selecciona una encuesta de la tabla y haz clic en "Eliminar Encuesta".

3. Exportar a Excel

Haz clic en "Exportar a Excel" para exportar los datos de las encuestas a un archivo Excel.

4. Generar Gráfico

Haz clic en "Generar Gráfico" para visualizar un gráfico de distribución de edades por sexo basado en los datos de las encuestas.

Notas

- Asegúrate de que el servidor MySQL esté en ejecución antes de iniciar la aplicación.
- Si encuentras algún problema, revisa los mensajes de error en la consola para obtener más detalles.

¡Disfruta usando la aplicación de gestión de encuestas!
