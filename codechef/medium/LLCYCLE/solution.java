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