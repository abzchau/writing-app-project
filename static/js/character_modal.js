console.log("I'm a Character, yo")

//Modal Behavior For Create Character On Project Page

const modalCharacter = document.getElementById("modalChar");

const btn = document.getElementById("myCharBtn");

const span = document.getElementsByClassName("close-char")[0];

btn.onclick = function(event) {
    modalCharacter.style.display = "block";
}

span.onclick = function() {
    modalCharacter.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalCharacter) {
        modalCharacter.style.display = "none";
    }
}

