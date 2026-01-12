// Object creation
let student = {
    name: "Haider",
    age: 20,
    course: "JavaScript"
};

// Display object values using keys
console.log("Student Name:", student.name);
console.log("Student Age:", student.age);
console.log("Student Course:", student.course);

// Array creation
let subjects = ["Math", "Science", "English", "Computer"];

// Display array using index
console.log("First Subject:", subjects[0]);
console.log("Second Subject:", subjects[1]);

// Join array elements
let joinedSubjects = subjects.join(", ");
console.log("Joined Array:", joinedSubjects);

// Remove last element using pop()
subjects.pop();

// Display whole array after pop
console.log("Array after pop:", subjects);
