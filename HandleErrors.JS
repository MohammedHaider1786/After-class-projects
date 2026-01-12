try {
    // Intentionally creating an error
    let age = 15;

    if (age < 18) {
        throw new Error("Access denied: Age must be 18 or above.");
    }

    console.log("Access granted.");

} catch (error) {
    // Catching and displaying the error message
    console.log("Error occurred:");
    console.log(error.message);
}
