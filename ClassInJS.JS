// Parent class
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    displayInfo() {
        console.log("Name:", this.name);
        console.log("Age:", this.age);
    }

    static greet() {
        console.log("Welcome to JavaScript Classes");
    }
}

// Child class (Inheritance)
class Student extends Person {
    constructor(name, age, grade) {
        super(name, age); // calling parent constructor
        this.grade = grade;
    }

    displayStudentInfo() {
        this.displayInfo();
        console.log("Grade:", this.grade);
    }
}

// Access static method
Person.greet();

// Create object of child class
let student1 = new Student("Haider", 20, "A");

// Display properties using method
student1.displayStudentInfo();
