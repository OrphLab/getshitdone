var today = new Date();
var current_time = today.toLocaleTimeString();

var colors = ['red','green', 'blue'];
var changecon = changeContent(colors);
console.log(changecon)


var firstDiv = document.getElementById("here");
firstDiv.textContent = current_time;

var secondDiv = document.getElementById('heretoo');
secondDiv.textContent  = changecon;

function changeContent(colors){
    return colors[0];
    }