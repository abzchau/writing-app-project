console.log("I'm a Modal, yo")

//Modal Behavior

const modal = document.getElementById("modalChar");

const btn = document.getElementById("myCharBtn");

const span = document.getElementsByClassName("close")[0];

btn.onclick = function(event) {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

