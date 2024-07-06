Para ver el proyecto 1:
	- Descargue la carpeta wiki
	- Instale python en su PC
	- Instale Django en su PC pip install django
	- En shell de windows ir a la direccion de la carpeta wiki
	- Escribir: python manage.py runserver
	- Aparecera un link similara a este http://127.0.0.1:80000/, copiarlo en un navegador

Especificación
	- Página de entrada : al visitar /wiki/TITLE, donde TITLEes el título de una entrada de enciclopedia, debería aparecer una página que muestre el contenido de esa entrada de enciclopedia.
	- La vista debe obtener el contenido de la entrada de la enciclopedia llamando a la utilfunción adecuada.
	- Si se solicita una entrada que no existe, se le debe presentar al usuario una página de error indicando que no se encontró la página solicitada.
	- Si la entrada existe, se debe mostrar al usuario una página que muestre el contenido de la entrada. El título de la página debe incluir el nombre de la entrada.
	- Página de índice : actualización index.htmlde modo que, en lugar de simplemente enumerar los nombres de todas las páginas de la enciclopedia, el usuario pueda hacer clic en el nombre de cualquier entrada para ser llevado directamente a la página de esa entrada.
	- Buscar : permite al usuario escribir una consulta en el cuadro de búsqueda de la barra lateral para buscar una entrada de enciclopedia.
	- Si la consulta coincide con el nombre de una entrada de enciclopedia, el usuario debe ser redirigido a la página de esa entrada.
	- Si la consulta no coincide con el nombre de una entrada de enciclopedia, el usuario debería ser redirigido a una página de resultados de búsqueda que muestra una lista de todas las entradas de enciclopedia que tienen la consulta como subcadena. Por ejemplo, si la consulta de búsqueda fuera ytho, entonces Pythondebería aparecer en los resultados de búsqueda.
	- Al hacer clic en cualquiera de los nombres de entrada en la página de resultados de búsqueda, el usuario debería ir a la página de esa entrada.
	- Nueva página : al hacer clic en “Crear nueva página” en la barra lateral, el usuario debería acceder a una página donde puede crear una nueva entrada de enciclopedia.
	- Los usuarios deberían poder ingresar un título para la página y, en un textarea, deberían poder ingresar el contenido Markdown para la página.
	- Los usuarios deberían poder hacer clic en un botón para guardar su nueva página.
	- Cuando se guarda la página, si ya existe una entrada de enciclopedia con el título proporcionado, se le debe presentar al usuario un mensaje de error.
	- De lo contrario, la entrada de la enciclopedia debe guardarse en el disco y el usuario debe ser llevado a la página de la nueva entrada.
	- Editar página : en cada página de entrada, el usuario debe poder hacer clic en un enlace para acceder a una página donde pueda editar el contenido Markdown de esa entrada en un formato textarea.
	- El textareadebe completarse previamente con el contenido Markdown existente de la página (es decir, el contenido existente debe ser la inicial valuedel textarea).
	- El usuario debe poder hacer clic en un botón para guardar los cambios realizados en la entrada.
	- Una vez guardada la entrada, el usuario debe ser redirigido nuevamente a la página de esa entrada.
	- Página aleatoria : al hacer clic en “Página aleatoria” en la barra lateral, el usuario debería acceder a una entrada de enciclopedia aleatoria.
	 