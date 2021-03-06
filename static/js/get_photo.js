console.log('doo')

//Gets the form data from the modal, posts the pogo to the api url, which then calls the create_index function to create a index in the Index database

btnSubmitPhoto = document.getElementById('mySubmitPhotoBtn')

function getData(getDataRes) {
    getDataRes.preventDefault();

    let name = document.getElementById('name_photo').value; 
    let desc = document.getElementById('desc_photo').value;
    const projectName = document.querySelector("#project_name").innerHTML; 

    formInput = {'name': name, 'desc': desc, 'photoReplacedFinal': window.selected, 'projectName': projectName}
    url = `/api/create_index`;
    $.post(url, formInput, dataResponse);
}

function dataResponse() {
        alert('Index Card created!');
    
}

btnSubmitPhoto.addEventListener('click', getData);


// Creates div elements with search term image results
const container = document.querySelector(".container-image");
let cardTag = '';
window.selected = '' ;

function getPhotos(images) {
    container.innerHTML = ''
    let num = 1
    images.map(image => {
        cardTag = `<div class="card">
                <img class="img-fluid" src=${image.src.tiny} id="myimage${num}" />
                </div>`;
        num += 1
        container.innerHTML += cardTag;
    });
    let imagesElements = document.querySelectorAll(".card img");

    $('img').click(function(){
        $('.selected').removeClass('selected'); // removes the previous selected class
        $(this).addClass('selected'); // adds the class to the clicked image
     });

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

