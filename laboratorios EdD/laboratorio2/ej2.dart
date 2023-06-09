// a. La primera lista debe tener los siguientes 5 elementos: [14,2,5,3,9]
// b. La segunda se debe ingresar por teclado (Debe tener 5 elementos
// enteros)
// c. La tercera lista igual debe contener 5 elementos, pero deben ser
// generados de forma aleatoria. (Solo números aleatorios negativos del
// -15 al -25)
// d. Restar la primera y segunda lista. La lista obtenida se suma con la
// tercera lista. Imprimir el resultado obtenido.
// e. Insertar en la primera y segunda posición de la lista que se obtuvo de la suma, los
// elementos 17 y 24.
// f. Por último ordenar de forma descendente la lista.
import "dart:io";
void main(){
  List <int> numeros = [14,2,5,3,9];
  // lista ingresada por el usuario
  List <int> numeros2 = [];
  print('ingrese el longitud que tendra la lista:');
  int longitud = int.parse(stdin.readLineSync()!);
  print('ingrese los elementos de la lista:');
  for(int i = 0; i < longitud; i++){
    numeros2.add(int.parse(stdin.readLineSync()!));
  }
  // lista de numeros aleatorios
  List <int> numeros3=[];
  final = random()
  print('ingrese el longitud que tendra la lista:');
  int longitud2 = int.parse(stdin.readLineSync()!);
  for(int i = 0; i<longitud;i++){                             
    numeros3.add(nextind.random(-15,-25));
  }

  print("la primera lista es:\n$numeros");
  print("la segunda lista es:\n$numeros2");  
  print("la tercera lista es:\n$numeros3");
}