void function fibonacci(int qnt) {

  if(qnt == 1) {
    print("0");
  } elif(qnt >= 2) {
    print("0, 1");
  }

  int i = 2;
  int numberToPrint;
  int prev2number = 0;
  int prev1number = 1;

  while(i < qnt) {
    numberToPrint = prev1number + prev2number;
    prev2number = prev1number;
    prev1number = numberToPrint;
    print(", %d", numberToPrint);
    i = i + 1;
  }
}

int main() {
  int qnt;
  input(qnt);
  fibonacci(qnt);
}