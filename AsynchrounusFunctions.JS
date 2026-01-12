function fetchUserData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const user = {
                name: "Haider",
                age: 20
            };
            resolve(user); 
        }, 2000);
    });
}

async function displayUserData() {
    try {
        const userData = await fetchUserData();
        console.log("User Name:", userData.name);
        console.log("User Age:", userData.age);
    } catch (error) {
        console.log("Error fetching user data");
    }
}

displayUserData();
