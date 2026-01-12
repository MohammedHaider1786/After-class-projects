// Original array
let numbers = [5, 2, 9, 1, 7];

// Map the array (multiply each element by 2)
let mappedArray = numbers.map(num => num * 2);

console.log("Mapped Array:", mappedArray);

// Sort in ascending order
let ascendingOrder = [...mappedArray].sort((a, b) => a - b);
console.log("Ascending Order:", ascendingOrder);

// Sort in descending order
let descendingOrder = [...mappedArray].sort((a, b) => b - a);
console.log("Descending Order:", descendingOrder);
