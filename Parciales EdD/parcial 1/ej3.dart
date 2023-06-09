// 3. Crear tres listas:
// a. La primera y segunda lista debe ser generada de forma aleatoria y tener
// 10 elementos. (Elementos entre el rango de 10 al 20)
// b. La tercera matriz se debe ingresar por teclado (Debe tener 5 elementos
// enteros)
// c. Concatenar todas las listas anteriores
// d. Obtener el promedio de la lista obtenida.
// e. Por último ordenar de forma ascendente la lista.
import "dart:math";
import "dart:io";

void main(){
  List <int> lista1=[];
  List <int> lista2=[];
  List <int> lista3=[];
  List <int> lista4=[];

  final random=Random();
  int longitud = 10;
  for (int i = 0; i < longitud; i++) {
    lista1.add(random.nextInt(21));
    lista2.add(random.nextInt(21));
  }
  int longitud2=5;
  print("ingrese las elementos de la lista 3:");
  for (int i = 0; i < longitud2; i++) {
    lista3.add(int.parse(stdin.readLineSync()!));
  }
  print("la primera lista es:\n$lista1");
  print("la segunda lista es:\n$lista2");
  print("la tercera lista es:\n$lista3");

  lista4.addAll(lista1);
  lista4.addAll(lista2);
  lista4.addAll(lista3);

  print("la lista es:\n$lista4");

  int suma=0;
  for (int i = 0; i < lista4.length; i++) {
    suma = suma + lista4[i];
  }
  print(suma);
  double promedio = suma/lista4.length;
  print("el promedio de la lista concatenada es:\n $promedio");

  lista4.sort();
  print("la lista ordenada ascendentemente es:\n$lista4");
}
