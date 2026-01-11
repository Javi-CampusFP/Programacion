<?php
$usuario = $_POST["usuario"]; // Coger el usuario del index.html
$password = $_POST["password"]; // Coger la contraseña del index.html
$simbolos = ['@', '#', '$', '%', '&']; // Caracteres especiales
$longitud_minima = 8; // Definir la longitud mínima

$longitud = strlen($password); // Calcular la longitud de la contraseña

// Validación : longitud mínima
if ($longitud < $longitud_minima) {
    echo "<p style='color: red;'>Error. La contraseña debe ser al menos de 8 caracteres de largo.</p>";
}
// Validación : contraseña diferente al usuario
else if ($usuario == $password) {
    echo "<p style='color: red;'>Error. La contraseña no puede ser la misma que el nombre de usuario.</p>";
} 
else {
    // Validación : al menos un carácter especial
    $tieneEspecial = false;
    foreach ($simbolos as $simbolo) {
        if (strpos($password, $simbolo) !== false) {
            $tieneEspecial = true;
            break;
        }
    }

    if (!$tieneEspecial) {
        echo "<p style='color: red;'>Error. La contraseña debe contener al menos un carácter especial (@, #, $, %, &).</p>";
    } else {
        echo "<p style='color: green;'>Contraseña válida</p>";
    }
}
?>
