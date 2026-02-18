<?php
$antiguos = $antiguos ?? ['nombre' => '', 'email' => '', 'edad' => ''];
?>
<?php if (!empty($error)): ?>
	<div class="error"><?php echo htmlspecialchars($error); ?></div>
<?php endif; ?>
<div class="tarjeta">
<h2>Formulario de alta</h2>
	<form method="POST" action="index.php?accion=guardar">
    	<label>Nombre</label>
    	<input type="text" name="nombre" value="<?php echo htmlspecialchars($antiguos['nombre']); ?>" required>
    	<label>Email (opcional)</label>
    	<input type="text" name="email" value="<?php echo htmlspecialchars($antiguos['email']); ?>">
    	<label>Edad</label>
    	<input type="text" name="edad" value="<?php echo htmlspecialchars($antiguos['edad']); ?>" required>
    	<button type="submit">Guardar alumno</button>
  </form>
</div>