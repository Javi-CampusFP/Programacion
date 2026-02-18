<div class="tarjeta">
  <h2>Listado de alumnos</h2>

  <?php if (empty($alumnos)): ?>
    <p>No hay alumnos todavía.</p>
  <?php else: ?>
    <table>
      <thead>
        <tr>
          <th>Fecha</th>
          <th>Nombre</th>
          <th>Email</th> </tr>
      </thead>
      <tbody>
        <?php foreach ($alumnos as $alumno): ?>
          <tr>
            <td><?php echo htmlspecialchars($alumno->fechaCreacion); ?></td>
            <td><?php echo htmlspecialchars($alumno->nombre); ?></td>
            <td><?php echo htmlspecialchars($alumno->email); ?></td>
          </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  <?php endif; ?>
</div>