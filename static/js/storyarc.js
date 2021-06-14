console.log('Imma StoryArc, yo')

btnSubmitStoryArc = document.getElementById('mySubmitArcBtn');

function createArcData(createDataRes) {
    createDataRes.preventDefault();

    let projectName = document.querySelector("#project_name").innerHTML; 
    let name = document.getElementById('name_arc').value;
    let plot_point1 = document.getElementById('plot_point1').value;
    let plot_point1_value = document.getElementById('plot_point1_value').value;
    let plot_point2 = document.getElementById('plot_point2').value;
    let plot_point2_value = document.getElementById('plot_point2_value').value;
    let plot_point3 = document.getElementById('plot_point3').value;
    let plot_point3_value = document.getElementById('plot_point3_value').value;
    let plot_point4 = document.getElementById('plot_point4').value;
    let plot_point4_value = document.getElementById('plot_point4_value').value;
    let plot_point5 = document.getElementById('plot_point5').value;
    let plot_point5_value = document.getElementById('plot_point5_value').value;
    let plot_point6 = document.getElementById('plot_point6').value;
    let plot_point6_value = document.getElementById('plot_point6_value').value;

    formInputArc = {'projectName': projectName, 'name': name, 'plot_point1': plot_point1, 'plot_point1_value': plot_point1_value, 'plot_point2': plot_point2, 'plot_point2_value': plot_point2_value, 'plot_point3': plot_point3, 'plot_point3_value': plot_point3_value, 'plot_point4': plot_point4, 'plot_point4_value': plot_point4_value, 'plot_point5': plot_point5, 'plot_point5_value': plot_point5_value, 'plot_point6': plot_point6, 'plot_point6_value': plot_point6_value}
    console.log(formInputArc)
    url = `/api/create_storyarc`;
    console.log("what's happening...")
    $.post(url, formInputArc, arcDataResponse);
}

function arcDataResponse() {
    alert('Story Arc Created!');
}

btnSubmitStoryArc.addEventListener('click', createArcData);