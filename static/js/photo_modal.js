console.log("I'm a Setting, yo")

//Modal Behavior For Create Setting On Project Page

const modalPhoto = document.getElementById("modalSearch");

const btnPhoto = document.getElementById("mySearchBtn");

const spanPhoto = document.getElementsByClassName("close-photo")[0];

btnPhoto.onclick = function(event) {
    modalPhoto.style.display = "block";
}

spanPhoto.onclick = function() {
    modalPhoto.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalPhoto) {
        modalPhoto.style.display = "none";
    }
}

