# Proyecto Final - Curso de Python - CoderHouse
### Comisión: 54140
### Estudiante: Martinez, Pablo Daniel

## Nombre del Proyecto 
### - Pawiki

## Descripción
> Esta pagina web cumple la función de registrar tus mascotas y poder llevar el control médico de cada una.

- Se puede registrar un usuario, el cual será el responsable de cargar mascotas y controles médicos. (Cada usuario solo puede ver sus mascotas y controles médicos)

- dentro del perfil, cada usuario puede ver todas las mascotas y los controles registrados.

- Cada una de las mascotas o controles se pueden ver en detalle, editar y eliminar.

- A cada mascota se le puede cargar una foto, que posteriormente la veremos en la lista de mascotas, lista de controles médicos y las vista en detalle de las anteriores mencionadas.

- Dentro del registro de las mascotas podemos acceder al registro de Razas y dentro del registro del control médico podemos acceder al registro de vacunas.

> La página también muestra las fotos de las mascotas registradas y brinda una sección "comunidad"

- En la galería de fotos se pueden ver todas las mascotas registradas en la página.

- En la sección comunidad se pueden ver veterinarias, tips y curiosidades.

- En caso que haya iniciado sesión, se pueden cargar, editar y eliminar las veterinarias, tips y curiosidades.

## Código

> En el código se pueden ver 4 apps, "core", "login", "perfil" y "comunidad".

> Core:
- En core encontramos la página principal que se ingresa desde la ruta base.

- La galeria de fotos que trae todos los objetos de "perfil.models.mascota" para poder mostrar las fotos que estan cargadas en la base de datos.

- Y tambien encontramos el apartado "Sobre mí" que cuenta un poco de quien soy.

- Por otro lado también está el template base que se usa en todos los html del proyecto.

> Login:

- Login trabaja con los usuarios, su creación, inicio de sesión, cierre de sesión, cambio de nombre de usuario y cambio de contraseña.

> Perfil:

- En perfil se encuentra la la parte del CRUD de mascota y controles médicos. También la creación de razas y vacunas.

> Comunidad:

- En comunidad encontramos el CRUD de veterinarias y tips/curiosidades. Como también encontramos los formularios para crear un nuevo animal y localidad.

*En la ruta "admin" podemos encontrar el CRUD de todo lo anterior mencionado, pero "razas", "vacunas", "animal" y "localidad" desde el html solo se pueden crear. 

## Video

> En el video muestro como es el funcionamiento visual de la página.

- https://www.youtube.com/watch?v=NLBVi7JMkIY
