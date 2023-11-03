
// Extract the desired_username from the URL
const url = window.location.pathname;
const parts = url.split('/');
const desired_username = parts[parts.length - 1];  // The last part of the URL

// Make a GET request to the API with the extracted username
fetch(`/api/users-tasks/${desired_username}`)
    .then(response => response.json())
    .then(data => {
        displayuserstasks(data);
    })
    .catch(error => console.error('Error: ', error));
    
function displayuserstasks(data){
    const taskList = document.getElementById("tasklist");
    data.forEach(task => {
        const taskElement = document.createElement("div");
        taskElement.className = "task"
        taskElement.innerHTML=`<p class="ownername">Owner: ${task.owner.username}</p><p class="taskname">Task Name: ${task.name}</p><p class=category>Category: ${task.category}</p>`;
        taskList.appendChild(taskElement);
        
    });
}
