# [Lemmanizer... Lemmanizer... Lemmanizer](https://youtu.be/rMqayQ-U74s)

## Instalacion y uso

Parados en el directorio del proyecto construimos la imagen

```
sudo docker build -t lemmanizer .
```

Una vez terminado iniciamos en container, el parametro `--rm` indica que se borrara el container una vez que se termine su ejecucion.

```
sudo docker run -it --rm -p 80:80 lemmanizer:latest
```

Una vez iniciado el container vamos al navegador e ingresamos la siguiente direccion:

```
http://localhost/lemmanizer?oracion=monitos en la cama saltan sin parar
```

La respuesta sera un json con la siguiente informacion:

```
{
    "response":"monito en el cama saltar sin parar"
}
```