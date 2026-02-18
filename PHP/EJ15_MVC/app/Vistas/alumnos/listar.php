<!-- app/Vistas/alumnos/listar.php -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Listado de Alumnos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container mt-4">

    <h2 class="mb-3">Listado de Alumnos</h2>

    <?php if (!empty($error)): ?>
        <div class="alert alert-danger"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>

    <?php if (empty($alumnos)): ?>
        <div class="alert alert-info">No hay alumnos todavía en la base de datos.</div>
    <?php else: ?>
        
        <div class="card shadow-sm">
            <div class="card-body p-0">
                <table class="table table-hover mb-0">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Email</th>
                            <th>Edad</th>
                            <th class="text-center">Acción</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($alumnos as $a): ?>
                            <tr>
                                <td><?php echo htmlspecialchars($a->id); ?></td>
                                <td><?php echo htmlspecialchars($a->nombre); ?></td>
                                <td><?php echo htmlspecialchars($a->email); ?></td>
                                <td><?php echo htmlspecialchars($a->edad); ?></td>
                                <td class="text-center">
                                    <a href="index.php?accion=borrar&id=<?php echo $a->id; ?>" 
                                       class="btn btn-sm btn-danger"
                                       onclick="return confirm('¿Eliminar este alumno?');">
                                        Eliminar
                                    </a>
                                </td>
                            </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </div>
    <?php endif; ?>
</div>

</body>
</html>