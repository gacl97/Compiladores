int [] function shellSort(int size, int vetor[size]) {
    int i;
    int j;
    int value;
    int h = 1;
    while(h < size) {
        for i = (h,  size, 1) {
            value = vetor[i];
            j = i;
            while(j > h - 1 && value <= vetor[j - h]) {
                vetor[j] = vetor [j - h];
                j = j - h;
            }
            vetor[j] = value;
        }
        h = h / 3;
    }
    return vetor;
}

int function main() {
  int size = 1000;
  int vetor[size];
  input(vetor);
  vetor = shellSort(size, vetor);
  for i = (0, size - 1, 1) {
      print("%d ", vetor[i]);
  }
  print("%d", vetor[size - 1]);
  return 0;
}