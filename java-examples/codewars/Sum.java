public class Sum {
  
  public Sum() {
 
  }
  
  public static int sum(int[] numbers) {

    if (numbers == null || numbers.length < 2) return 0;
    int min,max;
    int sum = 0;
    min = max = numbers[0];
   
    // https://www.tutorialspoint.com/java/lang/math_min_int.htm
    for (int number : numbers) {
      max = Math.max(max, number);
      min = Math.min(min, number);
      sum += number;
    }  

    return sum - max - min;
  }
  
  public static void main(String[] args) {
    Sum numArray = new Sum();
    System.out.println(numArray.sum(new int[] { 5, 10 }));
  }
  
}
