# Python-Reconocimiento
Reconocimiento facial de cubreboca con python y camara IP

*****************************+ LEOBARDO URQUIZA RAMIREZ & JOSE IVAN PEREZ UGALDE ********

* Pasos para la ejecución del programa
 1) Descargar la APP : 
https://play.google.com/store/apps/details?id=com.shenyaocn.android.WebCam&hl=es_MX&gl=US
2) Ejecutar la app y abrir en el navegador la camara , insertar el usuario admin y contraseña 
admin(puede variar)
3) Modificar la siguiente linea de codigo con el siguiente reemplazo, en el archivo baseDatos.py y Reconocimiento.py : 
celularCam = "http://admin:admin@"URL DEL TELEFONO":8081/"
cap = cv2.VideoCapture(0)

4) Ejecutar en el siguiente orden los archivos  = 

1:baseDatos.py
2:Modelo.py
3.Reconocimiento.py

**** NOTA ***********
PUEDEN EJECUTARSE LOS ARCHIVOS CON LA CAMARA DEL TELEFONO O SIN *