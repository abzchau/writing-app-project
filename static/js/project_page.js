// $(document).ready(function(){
//     $('#title').focus();
//       $('#text').autosize();
//   });

const cardSelector = document.querySelector("#selector_card");

function handleCardResponse(resCardResponse) {
    document.getElementsById('#card_name').innerHTML = resCardResponse.name
}


function addCardInfo() {
    const cardName = document.querySelector("#selector_card").value;
    const projectName = document.querySelector('#project_name').innerHTML  
    url = `/api/project/${projectName}/${cardName}`  
    console.log(url)
    $.get(url, handleCardResponse)
}


cardSelector.addEventListener('click', addCardInfo)