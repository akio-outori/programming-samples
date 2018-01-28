import java.util.*;

public class Kata1 {
  
  public Kata1() {
 
  }
  
  public static int sum(ArrayList<Integer> numbers) {
    int max = numbers.get(0);
    int min = numbers.get(0);
    int sum = 0;

    /* int primitives cannot be nil/null.  they must be assigned a value
       http://stackoverflow.com/questions/2254435/can-an-int-be-null-in-java
       also, .length() is for strings while .size() is for arrays/ArrayLists
    */ 
    for (int number=0; number < numbers.size(); number++) {
      if (numbers.get(number) > numbers.get(max)) {
        max = number;
      } else if (numbers.get(number) < numbers.get(min)) {
        min = number;
      }
    }
    
    // Remove a value from an array (by value, not position)
    // http://stackoverflow.com/questions/14231688/how-to-remove-element-from-arraylist-by-checking-its-value
    numbers.remove(max);
    numbers.remove(min);

    // Add all values in a numeric ArrayList
    for(Integer number : numbers) {
      sum += number;
    }

    return sum;
  }
  
  public static void main(String[] args) {
    Kata1 numArray = new Kata1();
    numArray.sum(new ArrayList<Integer>(Arrays.asList(5, 10, 15, 20, 25, 30, 51, 3, 6, 61)));
  }
  
}
