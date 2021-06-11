// $(document).ready(function(){
//     $('#title').focus();
//       $('#text').autosize();
//   });

let cardSelector = document.querySelector("#selector_card");

function handleCardResponse(resCardResponse) {
    console.log(resCardResponse);
    document.querySelector('#card_name').innerHTML = resCardResponse.card_name;
    document.getElementById("card_image").src = resCardResponse.image_url;
    document.getElementById("card_desc").innerHTML = resCardResponse.desc;
}


function addCardInfo(cardRes) {
    console.log('is this happening...')
    let cardName = document.querySelector("#selector_card").value;
    let projectName = document.querySelector('#project_name').innerHTML;  
    url = `/api/project/card/${projectName}/${cardName}`;  
    console.log(url);
    $.get(url, handleCardResponse);
}


cardSelector.addEventListener('click', addCardInfo);