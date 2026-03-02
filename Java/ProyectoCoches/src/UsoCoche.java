import java.util.Scanner;
public class UsoCoche {
	public static void main(String[] args) {
		Coche miCoche = new Coche("1234ABC","TOYOTA","YARIS");
		miCoche.acelerar(75);
		miCoche.frenar(19);
		System.out.println(miCoche.toString());
		Scanner lector = new Scanner (System.in);
		String opcion = "";
		do {
			System.out.println("1. Acelerar");
			System.out.println("2. Frenar");
			System.out.println("3. Ver estado del coche");
			System.out.println("4. Salir");
			System.out.println("---------------------");
			System.out.println("¿Qué opción eliges?");
			opcion = lector.nextLine();
		} while(!opcion.equals("4")); {
			lector.close();
		}
	}
}
