/*
This is an example script to show some of the basic functionality of java.
This should be considered example code only.
*/

// This is the start of the script

import java.util.*;

// Example class

public class Example {

  // Example constructor 
  public Example() {
    System.out.println("We're going to make a public example!");
  }

  // Example basic data types
  public void basicTypes() { 
    int integer = 4;
    String str  = "Example";
    boolean tF  = true;
    char alpha  = 'A';

    System.out.println(integer + "\n" + str + "\n" + tF + "\n" + alpha);
  }

  // Example advanced data types
  public void advancedTypes() {
    
    // pulled from http://cs.fit.edu/~ryan/java/language/java-data.html
    // Also ref https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html
    byte smallNum          = 127;
    short mediumNum        = 32000;
    long bigNum            = 1000000;
    float preciseNum       = 3.14f;
    double superPreciseNum = 3.1456d;

    System.out.println(smallNum + "\n" + mediumNum + "\n" + bigNum + "\n" + preciseNum + "\n" + superPreciseNum);
  }

  // Example Array Method
  public void arrayExample() {
    ArrayList<String> stringArray = new ArrayList<String>();
    stringArray.add("Example 1");
    stringArray.add("Example 2");
    stringArray.add("Example 3");

    // Update values in an Array
    stringArray.set(2, "Example 4");   

    // Iterate by calling each element individually using .get
    for(int i=0; i < stringArray.size(); i++) {
      System.out.println(stringArray.get(i));
    }

    // Iterate using Java's for each functionality
    for(String element : stringArray) {
      System.out.println(element);
    }
  }

  // Example Hash Method
  public void hashExample() {
    HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
    hashMap.put("Age", 31);
    hashMap.put("Weight", 190);
    hashMap.put("Height", 74);

    // Iterate through just values
    for (String key: hashMap.keySet()) {
      System.out.println("value is " + hashMap.get(key));
    }    

    // Iterate through keys + values
    for (String key: hashMap.keySet()) {
      System.out.println("The key is " + key + " and the value is " + hashMap.get(key));
    }
  }

  // Main Method
  public static void main(String[] args) {
    Example ex1 = new Example();

    if (args.length > 0) {
      switch (args[0]) {
        case "basicTypes": 
          ex1.basicTypes();
          break;
        case "advancedTypes": 
          ex1.advancedTypes();
          break;
        case "arrayExample": 
          ex1.arrayExample();
          break;
        case "hashExample": 
          ex1.hashExample();
          break;
        default: 
          System.out.println("Argument not understood!");
      } 
    }
  }
}
