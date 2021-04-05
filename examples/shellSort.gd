void function shellSort(int size, int vetor[size]) {

    int i;
    int j;
    int value;

    int h = 1;
    while(h < size) {
        for(i = h; i < size; i = i + 1) {
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

    for(i = 0; i < size/ i = i + 1) {
        print("%d ", vetor[i]);
    }
  
}

int function main() {
  int qnt;
  input(qnt);
  shellSort(qnt);
  
  return 0;
}