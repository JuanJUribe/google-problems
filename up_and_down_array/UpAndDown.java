package upanddown;

import java.util.Arrays;

class Main {
  
  public static Integer findMaxIdx(int[] array) {
    if(array.length == 0){
      return -1;
    }
    int[] sorted_array = new int[array.length];
    for(int i = 0; i<array.length; i++){
      sorted_array[i] = array[i];
    }
    Arrays.sort(sorted_array);
    int max_value = sorted_array[sorted_array.length-1];
    for(int i = 0; i<array.length; i++){
      if(max_value == array[i]){
        return i;
      }
    }
    return null;
  }
}