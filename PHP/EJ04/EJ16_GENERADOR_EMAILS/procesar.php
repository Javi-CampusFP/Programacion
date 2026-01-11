<?php
// Recoger datos del formulario
$nombre = trim($_POST["nombre"]);
$apellido = trim($_POST["apellido"]);
$dominio_raw = trim($_POST["dominio"]);

// Convertir a minúsculas
$nombre = strtolower($nombre);
$apellido = strtolower($apellido);

// Tomar primera letra del nombre
$primera_letra = substr($nombre, 0, 1);
// Esto mantiene lo que viene después de "q=", lo demas lo quita
if (strpos($dominio_raw, "q=") !== false) {
    $partes = explode("q=", $dominio_raw);
    $dominio = $partes[1];
} else {
    $dominio = $dominio_raw;
}
$email = $primera_letra . $apellido . "@" . $dominio;
echo "<p>Tu nuevo correo es: $email</p>";
?>
