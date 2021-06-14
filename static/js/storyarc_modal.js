console.log("I'm a Story Arc, yo")

//Modal Behavior For Create Setting On Project Page

const modalArc = document.getElementById("modalArc");

const btnArc = document.getElementById("myArcBtn");

const spanArc = document.getElementsByClassName("close-arc")[0];

btnArc.onclick = function(event) {
    modalArc.style.display = "block";
}

spanArc.onclick = function() {
    modalArc.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalArc) {
        modalArc.style.display = "none";
    }
}

