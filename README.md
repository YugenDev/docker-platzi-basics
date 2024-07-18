Docker es una plataforma de contenedores que permite empaquetar, distribuir y ejecutar aplicaciones en entornos aislados y reproducibles. Aquí tienes una introducción a algunos de los comandos más comunes de Docker:

1. **docker run**: Este comando crea y ejecuta un contenedor a partir de una imagen. Por ejemplo:
   ```bash
   docker run nombre_de_la_imagen
   ```

2. **docker build**: Utilizado para construir una imagen Docker a partir de un Dockerfile y un contexto de construcción. El contexto es el directorio desde donde se ejecuta el comando `docker build`.
   ```bash
   docker build -t nombre_de_la_imagen ruta_al_Dockerfile
   ```

3. **docker pull**: Descarga una imagen de Docker desde un registro, como Docker Hub. Por ejemplo:
   ```bash
   docker pull nombre_de_la_imagen
   ```

4. **docker push**: Sube una imagen local a un registro de imágenes (como Docker Hub).
   ```bash
   docker push nombre_de_la_imagen
   ```

5. **docker ps**: Muestra los contenedores en ejecución actualmente.
   ```bash
   docker ps
   ```

6. **docker stop**: Detiene uno o más contenedores en ejecución.
   ```bash
   docker stop nombre_del_contenedor_o_ID
   ```

7. **docker rm**: Elimina uno o más contenedores. Se puede utilizar con el flag `-f` para forzar la eliminación.
   ```bash
   docker rm nombre_del_contenedor_o_ID
   ```

8. **docker rmi**: Elimina una o más imágenes de Docker.
   ```bash
   docker rmi nombre_de_la_imagen
   ```

9. **docker exec**: Ejecuta un comando dentro de un contenedor en ejecución.
   ```bash
   docker exec -it nombre_del_contenedor comando
   ```

10. **docker logs**: Muestra los logs de un contenedor específico.
    ```bash
    docker logs nombre_del_contenedor
    ```

Estos son solo algunos de los comandos más utilizados en Docker. Cada comando tiene opciones adicionales que puedes explorar utilizando `docker comando --help` para obtener más detalles y personalizar su comportamiento según tus necesidades.