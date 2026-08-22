# ABSTRACTION

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com vinaymiryalkar miryalkarvinay12@gmail.com

A vehicle management system contains a base class `Vehicle` with a method `startEngine()`.

The classes `Car` and `Motorcycle` inherit from `Vehicle`. Each subclass must provide its own implementation of `startEngine()` by overriding the method from the parent class.

### Task

Complete only the `Car` and `Motorcycle` classes.

- In Car, override startEngine() to print:

```
Car engine starting with a roar...

```

- In Motorcycle, override startEngine() to print:

```
Motorcycle engine starting with a vroom...

```

The `Vehicle` class and the `main()` method are already provided and must not be modified.

The driver code reads the vehicle type, creates the corresponding object, stores it in a `Vehicle` reference, and calls `startEngine()`. This demonstrates  **method overriding and runtime polymorphism**.

### Output Format

Print the engine-starting message for the specified vehicle type.

For `Vehicle`:

```
Vehicle engine starting...

```

For `Car`:

```
Car engine starting with a roar...

```

For `Motorcycle`:

```
Motorcycle engine starting with a vroom...

```

### Sample 1:
Input
Output

```
Car
```

```
 Car engine starting with a roar...
```

### Sample 2:
Input
Output

```
Motorcycle

```

```
Motorcycle engine starting with a vroom...

```

## Solution

**Language:** Java  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T12:57:29.161Z  

```java
import java.util.*;

class Vehicle
{
    public void startEngine()
    {
        System.out.println("Vehicle engine starting...");
    }
}

class Car extends Vehicle
{
    // Complete this class
    @Override
    public void startEngine(){
        System.out.println("Car engine starting with a roar...");
    }
}

class Motorcycle extends Vehicle
{
    // Complete this class
    @Override
    public void startEngine(){
    System.out.println("Motorcycle engine starting with a vroom...");
    }
}

class Codechef
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        String type = sc.nextLine();

        Vehicle vehicle;
        if (type.equals("Car"))
        {
            vehicle = new Car();
        }
        else if (type.equals("Motorcycle"))
        {
            vehicle = new Motorcycle();
        }
        else
        {
            vehicle = new Vehicle();
        }
        vehicle.startEngine();
    }
}
```

---

[View on CodeChef](https://www.codechef.com/problems/ABSTRACTION)