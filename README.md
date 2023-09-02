# CoderHouse - comision 55630 - curso Python

## Civitelli Aldana - proyecto final

### Sitio Web "Laboratorio privado LABPAI"

Este sitio web tiene el objetivo de administrar un laboratorio, cargando y visualizando profesionales, pacientes , estudios y sus costos, preguntas frecuentes, posibilidad de contactarnos e información del autor.

Esta es la primera versión del mismo.

En la carpeta "laboratorio_app" encontrará las distintas subcarpetas y archivos que componen la aplicacion, iremos explicando cada uno de manera breve.

+ CASOS DE TEST:
  + Aquí se deja un archivo excel con los casos de prueba de la aplicación.

+ MIGRATIONS
  + Corresponde a las migraciones que fuí realizando a la base de datos.

+ STATIC/LABORATORIO_APP
  + assets -> imágenes que fueron usadas para el sitio.
  + css -> archivo que configura el estilo del sitio.
  + js -> Aquí se encuentran funciones de javascript que le dan vida a nuestro sitio.

+ TEMPLATES/LABORATORIO_APP
  + Esta carpeta contiene todas las páginas web del sitio como Estudios, Login, Registro, Edición de perfil, Profesionales, Prestaciones,entre otras. 

+ LABORATORIO.DB Base de datos.

+ MANAGE.PY Administrador del sitio web.

+ URLS.PY podrá visualizar las rutas para ingresar a cada una de las páginas web del sitio, como la carga de formulario, búsqueda, estudios, preguntas frecuentes, contáctenos, login, registros, edición de perfil, profesionales y demas páginas.
  (Cabe aclarar que algunas rutas se encuentran ocultas para el usuario. Para su visualización deberá estar logueado.)

+ VIEWS.PY observará las distintas funciones creadas para llevar a cabo la renderizción de cada página, como la obtención de profesionales, registro de administradores, guardado de cambios de perfil, y demás.  

+ MODELS.PY en este archivo se encuentran las clases del modelo de la base de datos.
  + Class Profesionales
    + Atributos: Nombre, Apellido, Matricula, Mail y Especialización.
  + Class Pacientes
    + Atributos: Nombre, Apellido, Email, Documento y Teléfono.
  + Class Estudios
    + Atributos: Prestación y valor.
  + Class Preguntas Frecuentes
    + Atributos: Pregunta y respuesta.
  + Class Contactos
    + Atributos: Teléfono, Email, Dirección y Horarios.
  + Class Avatar
    + Atributos: Imágen y User.

+ FORMS.PY aquí verá las clases de formularios para que se despliegue después la carga de datos, como por ejemplo, para cada Class de Models.py informado anteriormente.

## Login administrador: 📌

+ Usuario: AdminLABPAI
+ Password: proyectofinal23

## Para ejecutar: 📌

Debe ir a la carpeta raiz, abrir la terminar y escribir el siguiente código

```
py manage.py runserver

```

## Versionado 📌

Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/ACivitelli/Tercera-pre-entrega-Civitelli/tags).

## Autores ✒️

* **Aldana Civitelli** - [aldana](https://github.com/ACivitelli)

## Licencia 📄

[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
