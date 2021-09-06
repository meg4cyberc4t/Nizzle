import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'package:collection/collection.dart'; // To compare arrays

List<List<int>> getOriginalMatrix() => <List<int>>[
      <int>[1, 2, 3],
      <int>[4, 5, 6],
      <int>[7, 8, 9]
    ].toList();
// .toList() is used to create a new array!
// If this is not done, all arrays will refer to the same memory

void showMatrix(List<List<int>> matrix) {
  print('  4 5 6');
  for (var row = 0; row < 3; row++) {
    print('${row + 1} ${matrix[row][0]}|${matrix[row][1]}|${matrix[row][2]}');
  } // Matrix output
}

List<List<int>> randomizeMatrix(List<List<int>> matrix) {
  // This function deals with the randomization of the array
  var returnMatrix = <List<int>>[[], [], []];
  var oneMatrix = <int>[];
  matrix.forEach((inArray) {
    oneMatrix.addAll(inArray);
  });
  for (var i = 0; i < 3; i++) {
    for (var l = 0; l < 3; l++) {
      var position = Random().nextInt(oneMatrix.length);
      returnMatrix[i].add(oneMatrix[position]);
      oneMatrix.removeAt(position);
    }
  }
  return returnMatrix;
}

void showBanner() {
  var banner = '''
    ███╗░░██╗██╗███████╗███████╗██╗░░░░░███████╗
    ████╗░██║██║╚════██║╚════██║██║░░░░░██╔════╝
    ██╔██╗██║██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░
    ██║╚████║██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░
    ██║░╚███║██║███████╗███████╗███████╗███████╗
    ╚═╝░░╚══╝╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
    ''';
  print(banner);
}

void moveMatrix(List matrix, int move) {
  // Movement of a column or row in the array:
  // the source array and the rotation number are passed
  late int buffer;
  if (move > 0) {
    if (move <= 3) {
      move -= 1;
      buffer = matrix[move][2];
      matrix[move][2] = matrix[move][1];
      matrix[move][1] = matrix[move][0];
      matrix[move][0] = buffer;
    } else {
      move -= 3;
      move -= 1;
      buffer = matrix[2][move];
      matrix[2][move] = matrix[1][move];
      matrix[1][move] = matrix[0][move];
      matrix[0][move] = buffer;
    }
  } else {
    // In the opposite direction
    move = -move;
    if (move <= 3) {
      move -= 1;
      buffer = matrix[move][0];
      matrix[move][0] = matrix[move][1];
      matrix[move][1] = matrix[move][2];
      matrix[move][2] = buffer;
    } else {
      move -= 1;
      move -= 3;
      buffer = matrix[0][move];
      matrix[0][move] = matrix[1][move];
      matrix[1][move] = matrix[2][move];
      matrix[2][move] = buffer;
    }
  }
}

void clearTerminal() {
  for (var i = 0; i < stdout.terminalLines; i++) {
    stdout.writeln();
  }
}

String input() => stdin.readLineSync(encoding: Encoding.getByName('utf-8')!)!;
// The dart doesn't have its own input()

void main() {
  showBanner();
  print(
      'Welcome to Nizzle. Your task is to return the matrix to its original position:');
  showMatrix(getOriginalMatrix());
  print(
      'You can do this by moving one column or row. To do this, use the numbers from 1 to 6. If you use negative numbers from 1 to 6, then the movement will be in the opposite direction.');
  print("Let's start? (If not, press ctrl + c)");
  input();
  // Training
  var gameMatrix = randomizeMatrix(getOriginalMatrix());
  var startTime = Stopwatch()..start(); // Start timer
  var errorMessage = '';
  var originalMatrix = getOriginalMatrix();
  while (!const DeepCollectionEquality().equals(gameMatrix, originalMatrix)) {
    // As long as the arrays are not equal, run next
    clearTerminal();
    showMatrix(gameMatrix);
    if (errorMessage.isNotEmpty) {
      print(errorMessage);
      errorMessage = '';
    }
    var thisInput;
    try {
      print('Make a move:');
      thisInput = int.parse(input());
      if (thisInput == 0 || thisInput > 6 || thisInput < -6) {
        // Checking for correct input
        throw FormatException();
      }
      moveMatrix(gameMatrix, thisInput);
    } on FormatException {
      errorMessage = 'Incorrect input. Use numbers from 1 to 6, -1 to -6!';
      continue;
    }
  }
  // final :)
  clearTerminal();
  showMatrix(gameMatrix);
  print('Congratulations. You passed the game for ${startTime.elapsed}');
  print('Come again! :)');
  print('The author of the project: https://github.com/meg4cyberc4t');
}
