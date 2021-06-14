// $(document).ready(function(){
//     $('#title').focus();
//       $('#text').autosize();
//   });

//Sends Card Info To the Backend And Gets Back Info To Manipulate the Card Elements On the Project Page
let cardSelector = document.querySelector("#selector_card");

function handleCardResponse(resCardResponse) {
    console.log(resCardResponse);
    if (resCardResponse.card_type === "index") {
        document.querySelector('#card_name').innerHTML = resCardResponse.card_name;
        document.getElementById("card_image").src = resCardResponse.image_url;
        document.getElementById("card_desc").innerHTML = resCardResponse.desc;
    } else if (resCardResponse.card_type === "character") {
        document.querySelector('#card_name').innerHTML = resCardResponse.card_name;
        document.querySelector('#card_desc').innerHTML = resCardResponse.desc;
        document.querySelector('#card_role').innerHTML = resCardResponse.role;
    } else {
        document.querySelector('#card_name').innerHTML = resCardResponse.card_name;
    }
}

function addCardInfo(cardRes) {
    console.log('is this happening...')
    let cardName = document.querySelector("#selector_card").value;
    let projectName = document.querySelector('#project_name').innerHTML;

    if (selector_card.options[selector_card.selectedIndex].id === "index") {
        let card_type = "index";
        url = `/api/project/card/${projectName}/${card_type}/${cardName}`;
        $.get(url, handleCardResponse);
    } else if (selector_card.options[selector_card.selectedIndex].id === "character") {
        let card_type = "character";
        url = `/api/project/card/${projectName}/${card_type}/${cardName}`;
        console.log(url);
        $.get(url, handleCardResponse);
    } else {
        let card_type = "storyarc";
        url = `/api/project/card/${projectName}/${card_type}/${cardName}`;
        console.log(url);
        $.get(url, handleCardResponse);
    }
}

    cardSelector.addEventListener('click', addCardInfo);

//Chart.js Playground

