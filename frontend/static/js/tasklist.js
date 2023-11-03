
// Make a GET request when the button is clicked
fetch("/api/tasks/")  // Replace with your actual API URL
    .then(response => response.json())
    .then(data => {
        // Handle the response data
        displayTasks(data);
    })
    .catch(error => console.error("Error:", error));


    function displayTasks(data) {
        const taskList = document.getElementById("taskList");
        // Iterate over the tasks and format them
        data.forEach(task => {
            const taskElement = document.createElement("div");
            taskElement.className = "task";
            taskElement.innerHTML = `<p>Owner: ${task.owner.username}</p><p>Name: ${task.name}</p><p>Category: ${task.category}</p>`;
            taskList.appendChild(taskElement);
    });
}