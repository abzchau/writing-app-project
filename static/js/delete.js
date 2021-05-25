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

function handleSearchResult(res) {
    fetch(`https://api.pexels.com/v1/search?query=${res}`, {
        headers: {
            Authorization: "563492ad6f917000010000016dba63fdcee443c384f3b8757a9569e6"
        }
    })
        .then(resp => {
            return resp.json();
        })
        .then(data => {
            getPhotos(data.photos)
        })
    }

//Gets the search result

let btnSearch = document.querySelector('#mySearchBtn');

function getResult(resSearch) {
    resSearch.preventDefault();
    let search = document.getElementById('search').value
    url = `/api/deleteme/${search}`;
    $.get(url, handleSearchResult);

}

btnSearch.addEventListener('click', getResult);

