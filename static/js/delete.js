console.log('doo')

const container = document.querySelector(".container");
let cardTag = '';

function getPhotos(images) {
    images.map(image => {
        cardTag = `<div class="card">
                <img src=${image.src.tiny} />
                </div>`;
        container.innerHTML += cardTag;
    })
}

fetch("https://api.pexels.com/v1/search?query=koalas", {
    headers: {
        Authorization: "563492ad6f917000010000016dba63fdcee443c384f3b8757a9569e6"
    }
})
    .then(resp => {
        return resp.json()
    })
    .then(data => {
        getPhotos(data.photos)
    })