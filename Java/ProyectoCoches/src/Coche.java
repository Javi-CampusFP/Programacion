public class Coche { 
	
	private String matricula;
	private String marca;
	private String modelo;
	private int velocidad;
	
	
	
	public Coche(String matricula, String marca, String modelo) {
		super();
		this.matricula = matricula;
		this.marca = marca;
		this.modelo = modelo;
		this.velocidad = 0;
	}

	public String getMatricula() {
		return matricula;
	}
	
	public void setMatricula(String matricula) {
		this.matricula = matricula;
	}
	
	public String getMarca() {
		return marca;
	}
	
	public void setMarca(String marca) {
		this.marca = marca;
	}
	
	public String getModelo() {
		return modelo;
	}
	
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	
	public int getVelocidad() {
		return velocidad;
	}
	
	public void acelerar (int cuanto) {
		this.velocidad = this.velocidad + cuanto;
	}
	
	public void frenar (int cuanto) {
		this.velocidad = this.velocidad + cuanto; 
	}
	
	@Override
	public String toString() {
		return "Coche [matricula=" + matricula + ", marca=" + marca + ", modelo=" + modelo + ", velocidad=" + velocidad + "]";
	}
}
