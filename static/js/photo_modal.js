console.log("I'm a Modal, yo")

//Modal Behavior

const modal = document.getElementById("modalSearch");

const btn = document.getElementById("mySearchBtn");

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

