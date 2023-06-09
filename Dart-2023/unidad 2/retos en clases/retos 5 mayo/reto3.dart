// Crear una lista de números enteros en la cual se debe ingresar el
// tamaño y sus elementos por teclado. Se solicita ordenar
// ascendentemente y descendentemente. Además solo se deben
// ingresar números enteros positivos.
// Se solicita obtener el valor máximo y mínimo de la lista
import 'dart:io';

void main(){

  List <int> lista = [];
  print('ingrese el longitud que tendra la lista:');
  int longitud = int.parse(stdin.readLineSync()!);

  print('ingrese los elementos de la lista:');
  for(int i = 0; i < longitud; i++){
    int valor;
    do{
      valor = int.parse(stdin.readLineSync()!);
      if (valor <=0) {
        print('ingrese un valor positivo');
      }
      }while(valor <=0);
      lista.add(valor);
    }

  print("el arreglo creado es:\n $lista");

  lista.sort();
  print("el arreglo ordenado ascendentemente es:\n $lista");

  lista.sort((a, b) => b - a);
  print("el arreglo ordenado descendentemente es:\n $lista");

  int max = lista[0];
  for(int i = 0; i < lista.length; i++){
    if(lista[i] > max){
      max = lista[i];
      }
  }
  print('el valor maximo es:$max');

  int min = lista[0];
  for(int i = 0; i < lista.length; i++){
    if(lista[i] < min){
      min = lista[i];
      }
  }
  print('el valor minimo es:$min');
}