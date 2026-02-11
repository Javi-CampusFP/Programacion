<?php
    require_once __DIR__ . '/../Modelo/RepositorioCursos.php';
    class ControladorCursos {
        private $repositorio;

        public function __construct(){
            $this->repositorio = new RepositorioCursos();
        }

        public function crear(){
            $this->renderizar('cursos/crear', [
                'antiguos' => ['nombre' => '', 'horas' => '']
            ]);
        }

        public function listar(){
            try {
                $cursos = $this->repositorio->obtenerTodos();

                $this->renderizar('cursos/listar', [
                    'cursos' => $cursos,
                    'error' => null
                ]);

            } catch(Exception $e){
                $this->registrarError("LISTAR", $e);

                $this->renderizar('cursos/listar', [
                    'cursos' => [],
                    'error' => 'No se pudieron cargar los cursos. Revisa errores.log'
                ]);
            }
        }


        public function guardar(){
            if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST'){
                header("Location: index.php?accion=listar");
                exit;
            }
            $nombre = trim($_POST['nombre'] ?? '');
            $horas = trim($_POST['horas'] ?? '');
            try {
                $this->validar($nombre,$horas);
                $curso = new Curso(
                    null,
                    $nombre,
                    (int)$horas,
                    date('Y-m-d H:i:s')
                );
                $this->repositorio->insertar($curso);
                header("Location: index.php?accion=listar");
                exit;
            } catch(Exception $e){
                $this->registrarError("GUARDAR", $e);
                $this->renderizar('cursos/crear', [
                    'error' => $e->getMessage(),
                    'antiguos' => ['nombre' => $nombre, 'horas' => $horas]
                ]);
            }
        }
        
        public function validar($nombre, $horas){
            if (strlen($nombre) < 3){
                throw new Exception("El nombre de usuario es demasiado corto");
            }
            // Si la hora esta vacia o no es tipo digito
            if ($horas === '' || !ctype_digit($horas)){
                throw new Exception("La hora debe de ser un número entero");
            }
            $horasNum = (int)$horas;
            if ($horasNum < 1 || $horasNum > 1000){
                throw new Exception("Las horas deben tener un valor entre 1 y 1000");
            }
        }

        public function renderizar($vista, $datos = []){
            extract($datos);
            $archivoVista = __DIR__ . "/../Vista/" . $vista . '.php';
            if (!file_exists($archivoVista)){
                throw new Exception("La vista " . $vista . " no ha sido encontrada");
                return;
            }
            $vistaContenido = $archivoVista;
            require_once __DIR__ . '/../Vista/layout.php';
        }

        public function registrarError($contexto, $error){
            $rutaLog = __DIR__ . "/../../storage/errores.log";
            $fecha = date('Y-m-d H:i:s');
            $linea = $fecha . " | " . $contexto . " | " . $error->getLine() . "\n";
            file_put_contents($rutaLog, $linea, FILE_APPEND);
        }
    }
?>