<?php 
require_once __DIR__ . '/../Modelos/RepositorioAlumnos.php';
require_once __DIR__ . '/../Modelos/Alumno.php';
class ControladorAlumnos{
    private static $repositorio;
    public function __construct(){
        self::$repositorio = new RepositorioAlumnos;
    }

    // Renderiza la vista correspondiente
    public function crear(){
        $this->renderizar("alumnos/crear");
    }
    
    // El cerebro del controlador, este comprueba si los datos son correctos y los mete en la base de datos
    public function guardar(){
        try{
            // Si el método es GET, ni se procesa.
            if ($_SERVER['REQUEST_METHOD'] === 'GET'){
                throw new Exception("El método GET no es reconocido como un método válido.");
            }
            // Coger los datos del formulario
            $nombre = $_POST['nombre'];
            $edad = $_POST['edad'];
            $email = $_POST['email'];
            // Validar los datos proporcionados, si es true, se ejecuta la función insertar
            if ($this->validar($nombre,$edad,$email)){
                $alumno = new Alumno($nombre,$email,$edad,date("Y-m-d H:i:s"));
                self::$repositorio->insertar($alumno);
                header("Location: index.php?accion=correcto");
            // Si no es true, se para la ejecución
            } else{
                $this->renderizar("alumnos/crear");
            };
    
        // Recoger los errores de ejecución y mandarlo a "crear" otra vez
        } catch (Exception $error){
            $this->registrarError($error->getMessage(), 'GUARDAR');
            header("Location: index.php?accion=crear");
        }
    }
    
    // Renderiza la vista correspondiente
    public function correcto(){
        $this->renderizar("alumnos/correcto");
    }

    // Renderizar la vista con el layout, esta vez no hace falta pasarle datos, asi que solo la vista que se quiere renderizar
    public function renderizar($vista){
        $vistaRuta = __DIR__ . '/../Vistas/' . $vista . '.php';
        // Comprueba si el archivo existe
        if (!file_exists($vistaRuta)){
            echo "La vista $vista no existe.";
            throw new Exception("La vista $vista no existe.");
        }
        $vistaContenido = $vistaRuta;
        require_once __DIR__ . '/../Vistas/layout.php';
    }

    // Registrar errores de forma fácil. La hago static para poder usarla en otros lados como en ConexionDB.php
    public static function registrarError($contexto, $error){
        $ruta = __DIR__ . '/../../storage/errores.log';
        $fecha = date("Y-m-d H:i:s");
        $linea = "$fecha | $contexto | $error";
        file_put_contents($ruta,$linea,FILE_APPEND);
        
    }

    // Validar los valores que se introducen en el formulario
    public function validar($nombre, $edad, $email){
        // Si el nombre tiene una longitud menor a 3, se lanza una excepción
        if (strlen($nombre) < 3){
            echo "El nombre no puede ser menor a 3 carácteres";
            throw new Exception("El nombre no puede ser menor a 3 carácteres.");
            return false;
        }

        // Comprobar el rango de edad
        if ($edad < 1 || $edad > 120){
            echo "La edad no puede ser menor que 1 ni mayor que 120";
            throw new Exception("La edad no puede ser menor que 1 ni mayor que 120");
            return false;
        }

        // Comprueba si la longitud es mayor a 0 y no hay un email valido se lanza una excepción 
        if (strlen($email) > 0 && !str_contains($email,"@")){
            echo "El email no es válido.";
            throw new Exception("El email no es válido.");
            return false;
        }
        return true;
    }
}
?>
