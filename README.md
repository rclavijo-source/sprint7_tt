# sprint7\_tt

Proyecto Sprint 7 TripleTen

El proyecto del sprint 7 es construir una aplicación visible en la web a partir de un repositorio público en github, y alojar la aplicación en render.com, este repositorio tiene la carpeta main donde se encuentran los archivos README.md, .gitignore los cuales son archivos básicos para todos los repositorios, también tiene app.py, requirements.txt, y vehicules_us.csv, los cuales se usan para construir la app en render.com, app.py es un archivo python que tiene el script necesario para la app, requirements.txt tiene los nombres de las librerías necesarias para que app.py funciones correctamente, y vehicules_us.csv tiene información sobre vehículos usados en venta en los Estados Unidos, sobre la cual se hacen los gráficos que la app muestra.

El repositorio también tiene una carpeta adicional que se llama notebooks, la cual tiene los archivos vehicules_us.csv, EDA.ipynb, y requirements.txt, esta carpeta fue creada para llevar a cabo el análisis exploratorio de datos inicial de la información de vehicules_us.csv, donde se realizaron revisiones sobre la cantidad de datos, la distribución de los mismos, y algunas gráficas para entender la relación entre ellos.    


La aplicación web toma la información y hace dos gráficos, un histograma donde se ve la distribución del uso de los coches en venta haciendo uso de la información del odómetro. También hace un gráfico de dispersión que compara el precio de los vehículos en venta contra la información del odómetro.

La aplicación fue construida haciendo uso de la librería streamlit de python, al acceder a la aplicación el usuario pueda hacer uso de casillas de verificación para decidir si quiere ver solo una de las gráficas, o las dos.

La dirección web de la app en render.com es https://sprint7-tt-h11g.onrender.com/





