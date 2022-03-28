class Animal {
	// set name and food as atrributes
	// let's say default initial energy amount is 50
	protected String name = "";
	protected float food = 50;

	// contructor
	public Animal(String name) {
		this.name = name;
	}

	// calls hidden method digest()
	public boolean eat(float food) {
		System.out.println("eat food");
		return digest(food);
	}

	// calls hidden method consume_food()
	// default food efficiency is 1 unit food per 1 unit distance
	public boolean walk(int distance) {
		System.out.println("walk");
		return consume_food(distance);
	}

	// return name
	public String get_name() {
		System.out.println("My name is "+this.name);
		return this.name;
	}

	// add food
	// maximum food is 100
	// food absorption rate is 1
	protected boolean digest(float food) {
		if (this.food+food > 100) {
			System.out.println("I'm full");
			return false;
		}

		this.food += food;
		System.out.println("food +"+food);

		return true;
	}

	// use food
	protected boolean consume_food(float food) {
		if (this.food - food < 0) {
			System.out.println("I'm hungry");
			return false;
		}

		this.food -= food;
		System.out.println("food -"+food);

		return true;
	}
}

// Dog inherits from Animal
class Dog extends Animal {

	//calls animal's contructor
	public Dog(String name) {
		super(name);
	}

	// new method
	// uses 5 food per each call
	public boolean woof() {
		if (!consume_food(5))
			return false;

		System.out.println("woof woof");
		return true;
	}

	// overwrite digest()
	// Dog's food absorption rate is 0.7
	@Override
	protected boolean digest(float food) {
		food *= 0.7;
		if (this.food + food > 100) {
			System.out.println("I'm full");
			return false;
		}

		this.food += food;
		System.out.println("food +"+food);

		return true;
	}
}

// Cat inherits from Animal
class Cat extends Animal {

	//calls animal's contructor
	public Cat (String name) {
		super(name); 
	}

	// new method
	// uses 3 food per each call
	public boolean meow() {
		if (!consume_food(3))
			return false;

		System.out.println("meow meow");
		return true;
	}

	// overwrite walk()
	// Cat's food efficiency is 0.5 unit food per 1 unit distance
	@Override
	public boolean walk(int distance) {
		System.out.println("walk");
		distance *= 0.5;
		return consume_food(distance);
	}

}

class Main {
	public static void main(String[] args) {
		// subtyping
		Animal[] animal = new Animal[2];
		animal[0] = new Dog("Buddy");
		animal[1] = new Cat("Kitty");

		animal[0].get_name(); // prints "My name is Buddy"
		animal[1].get_name(); // prints "My name is Kitty"

		// these does not run
		// Dog dog_but_cat = new Cat("Kitty");
		// Cat cat_but_dog = new Dog("Buddy"); 
		
		// overloading
		print_sum(1, 2); // 3
		print_sum(1, 2, 3); // 6
		print_sum("1", "2"); // 3
	}

	public static void print_sum(int a, int b) {
  	System.out.println(a + b);
	}

	public static void print_sum(int a, int b, int c) {
  	System.out.println(a + b + c);
	}

	public static void print_sum(String a, String b){
		int a_int = Integer.parseInt(a);
  	int b_int = Integer.parseInt(b);
		System.out.println(a_int+b_int);
	}
}