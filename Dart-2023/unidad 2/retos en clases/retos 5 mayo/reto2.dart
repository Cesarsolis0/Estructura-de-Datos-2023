// Crear un arreglo de tamaño aleatorio (entre 10 a 30 elementos). Los
// elementos también deben ser aleatorios (de 0 a 10). Además se
// solicita ordenarlo de forma ascendente.
// Luego ordenar ese mismo arreglo de forma aleatoria
import 'dart:math';

void main(){

  final random = Random();  

  List <int> arreglo = [];
  for (int i = 0; i < random.nextInt(21)+10; i++) {
    arreglo.add(random.nextInt(11));
  }
  print('el arreglo es: \n$arreglo');

  arreglo.sort();
  print('el arreglo ordenado de forma ascendente es:\n $arreglo');

  arreglo.shuffle();
  print('el arreglo ordenado de forma aleatoria es:\n $arreglo');
}
