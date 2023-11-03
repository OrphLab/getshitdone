// frontend_script.js

// Extract the desired_username from the URL
const url = window.location.pathname;
const parts = url.split('/');
const desired_username = parts[parts.length - 1];  // The last part of the URL

// Make a GET request to the API with the extracted username
fetch(`/api/users-tasks/${desired_username}`)
    .then(response => response.json())
    .then(data => {
        displayUserTasks(data);
    })
    .catch(error => console.error('Error: ', error));

function displayUserTasks(data) {
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = ''; // Clear any existing tasks

    data.forEach(task => {
        const taskElement = document.createElement("div");
        taskElement.className = 'task';
        taskElement.innerHTML = `<p>Owner: ${task.owner.username}</p><p>Name: ${task.name}</p><p>Category: ${task.category}</p>`;
        taskList.appendChild(taskElement);
    });
}M