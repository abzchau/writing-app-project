// $(document).ready(function(){
//     $('#title').focus();
//       $('#text').autosize();
//   });

//Sends Card Info To the Backend And Gets Back Info To Manipulate the Card Elements On the Project Page
let cardSelector = document.querySelector("#selector_card");

function handleCardResponse(resCardResponse) {
    console.log(resCardResponse);
    if (resCardResponse.card_type === "index") {
        document.querySelector('#card_name').innerHTML = "Name:" + " " + resCardResponse.card_name;
        document.getElementById("card_image").src = resCardResponse.image_url;
        document.getElementById("card_desc").innerHTML = "Description:" + " " + resCardResponse.desc;
    } else if (resCardResponse.card_type === "character") {
        document.querySelector('#card_name').innerHTML = "Name:" + " " +  resCardResponse.card_name;
        document.querySelector('#card_desc').innerHTML = "Description:" + " " + resCardResponse.desc;
        document.querySelector('#card_role').innerHTML = "Role:" + " " + resCardResponse.role;
    } else if (resCardResponse.card_type === "storyarc") {
        // document.querySelector('#card_name').innerHTML = resCardResponse.card_name;
        $('.card__details').append('<canvas id="myChartCard"></canvas>');
        myChart(resCardResponse)
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

function clearData() {
    document.getElementById('card_image').src = '';
    document.getElementById('card_desc').innerHTML = '';
    document.getElementById('card_name').innerHTML = '';
    document.getElementById('card_role').innerHTML = '';
    $('#myChartCard').remove();
    addCardInfo()
}

cardSelector.addEventListener('click', clearData);

//Chart.js Playground

function myChart(resCardResponse) {
    let ctx = document.getElementById('myChartCard');

    let myChartCard = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [resCardResponse.plot_point1, resCardResponse.plot_point2, resCardResponse.plot_point3, resCardResponse.plot_point4, resCardResponse.plot_point5, resCardResponse.plot_point6],
            datasets: [{
                label: 'Story Arc',
                data: [resCardResponse.plot_point1_value, resCardResponse.plot_point2_value, resCardResponse.plot_point3_value, resCardResponse.plot_point4_value, resCardResponse.plot_point5_value, resCardResponse.plot_point6_value],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


