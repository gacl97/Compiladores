void function fibonacci(int num) {
  if(num == 0) {
    return;
  } elif(num == 1) {
    print("0");
    return;
  } elif(num == 2) {
    print("0, 1, 1");
    return;
  }

  int prev2number = 1;
  int prev1number = 1;
  int numberToPrint = prev2number + prev1number;

  while(numberToPrint < num) {
    print(", %d", numberToPrint);
    prev2number = prev1number;
    prev1number = numberToPrint;
    numberToPrint = prev1number + prev2number;
  }
}

int function main() {
  int num;
  input(num);
  fibonacci(num);
  return 0;
}