#include "stdio.h"
#include "stdlib.h"
#include "string.h"

// first elem is an int. points to an int
int *sorted(int *unsorted_arr, int arr_len) {
  int arr_size = sizeof(unsorted_arr[0]) * arr_len;
  int *sorted_arr = malloc(arr_size);
  memcpy(sorted_arr, unsorted_arr, arr_size);

  int swap_count;
  do {
    swap_count = 0;
    for (int b = 1; b < arr_len; b++) {
      int a = b - 1;
      if (sorted_arr[b] < sorted_arr[a]) {
        int storage_variable = sorted_arr[b];
        sorted_arr[b] = sorted_arr[a];
        sorted_arr[a] = storage_variable;
        swap_count++;
      }
    }
  } while (swap_count > 0);

  return sorted_arr;
}

void printa(int *array, int arr_len) {
  printf("[");
  for (int i = 0; i < arr_len; i++) {
    printf("%d", array[i]);
    if (i != arr_len - 1) {
      printf(", ");
    }
  }
  printf("]\n");
}

int main() {
  int nums[] = {
      893, 573, 266, 55,  229, 797, 678, 723, 248, 156, 755, 337, 490, 400, 827,
      250, 283, 784, 448, 727, 634, 918, 752, 420, 884, 890, 861, 385, 371, 879,
      911, 380, 973, 914, 472, 18,  995, 131, 773, 831, 259, 785, 428, 685, 522,
      69,  48,  188, 597, 282, 473, 100, 792, 156, 639, 886, 190, 463, 507, 620,
      809, 164, 38,  786, 583, 312, 843, 630, 880, 361, 473, 369, 479, 914, 639,
      778, 86,  281, 221, 329, 860, 790, 638, 312, 999, 952, 2,   447, 119, 433,
      409, 854, 750, 699, 611, 494, 812, 870, 199, 327,
  };
  int nums_len = 100;

  printf("unsorted:\n");
  printa(nums, nums_len);
  printf("sorted:\n");
  printa(sorted(nums, nums_len), nums_len);

  return 0;
}
