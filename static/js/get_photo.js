console.log('doo')

btnSubmitPhoto = document.getElementById('mySubmitPhotoBtn')

function getData(getDataRes) {
    getDataRes.preventDefault();
    let photo = window.selected.slice(40);
    const photoReplaced = photo.replaceAll('&', 'replace')
    const photoReplacedFinal = photoReplaced.replaceAll('?', 'question')
    let photoNum = window.selected.slice(33, 40);
    let name = document.getElementById('name_photo').value; 
    let desc = document.getElementById('desc_photo').value;
    const projectName = document.querySelector("h1").innerHTML; 
    const imageCall = window.selected
    console.log(photoReplacedFinal)
    url = `/api/${name}/${desc}/${photoNum}/${photoReplacedFinal}/${projectName}`;
    $.get(url, dataResponse);
}

function dataResponse() {
        alert('created');
    
}


btnSubmitPhoto.addEventListener('click', getData);




// Creates div elements with search term image results
const container = document.querySelector(".container");
let cardTag = '';
window.selected = '' ;

function getPhotos(images) {
    container.innerHTML = ''
    let num = 1
    images.map(image => {
        cardTag = `<div class="card">
                <img src=${image.src.tiny} id="myimage${num}" />
                </div>`;
        num += 1
        container.innerHTML += cardTag;
    });
    let imagesElements = document.querySelectorAll(".card img");

    for (let image of imagesElements) {
        image.onclick = function() {
            window.selected = image.src;
        }
    }
}



//Makes the Get request for the search term

function handleSearchResult(res) {
    console.log(res)
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
    let search = document.getElementById('search').value;

    handleSearchResult(search);

}

btnSearch.addEventListener('click', getResult);

