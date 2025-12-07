CREATE DATABASE IF NOT EXISTS sistema_login;
USE sistema_login;

CREATE TABLE IF NOT EXISTS actividad_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255),
    fecha_hora DATETIME,
    accion VARCHAR(255),
    ruta_imagen VARCHAR(255)
);
