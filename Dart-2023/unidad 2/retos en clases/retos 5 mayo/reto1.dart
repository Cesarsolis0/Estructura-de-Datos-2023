// Solicitar una lista de números enteros al usuario por teclado, y luego
// sumar cada elemento de la lista obtenida.
import 'dart:io';

void main() {
  List<int> lista = [];

  print('ingrese la longitud que tendra la lista:');
  int longitud = int.parse(stdin.readLineSync()!);
  
  print('ingrese los valores que tendra la lista:');
  for (int i = 0; i < longitud; i++) {
    int valores = int.parse(stdin.readLineSync()!);
    lista.add(valores);
  }
  print('la lista ingresada es: $lista');

  int suma=0;
  for (int numeros in lista){
    suma = suma + numeros;
  }
  print('la suma de la lista es: $suma');
}