CREATE DATABASE sistema_login;
USE sistema_login;

CREATE TABLE actividad_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    fecha_hora DATETIME,
    accion VARCHAR(100),
    ruta_imagen VARCHAR(255)
);

