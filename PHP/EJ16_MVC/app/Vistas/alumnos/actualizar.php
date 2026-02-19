<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Alumno</title>
</head>
<body>
    <h2>Editar alumno</h2>
    <?php if (!empty($error)): ?>
        <div style="color: red;"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>
    <form action="index.php?accion=editar" method="POST">
        <input type="hidden" name="id" value="<?php echo htmlspecialchars($alumno->id ?? ''); ?>">
        <div>
            <label for="nombre">Nombre</label>
            <input type="text" name="nombre" id="nombre" value="<?php echo htmlspecialchars($alumno->nombre ?? ''); ?>">
        </div>
        <div>
            <label for="email">Email</label>
            <input type="email" name="email" id="email" value="<?php echo htmlspecialchars($alumno->email ?? ''); ?>">
        </div>
        <div>
            <label for="edad">Edad</label>
            <input type="number" name="edad" id="edad" value="<?php echo htmlspecialchars($alumno->edad ?? ''); ?>">
        </div>
        <br>
        <button type="submit">Guardar</button>
        <a href="index.php?accion=listar">Volver</a>
    </form>
</body>
</html>