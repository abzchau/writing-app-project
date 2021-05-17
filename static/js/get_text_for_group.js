console.log('Belsize Park');

//Gets User Name And Display User Text

let form = document.querySelector('#get-writer');

function handleResponse(res) {
  document.querySelector('#text').innerHTML = res;
}

function getText(txt) {
  let name = document.getElementById('writer-id').value;
  const groupName = document.querySelector('#group_name').innerHTML 
  url = `/api/${groupName}/${name}`;
  console.log(url)
  $.get(url, handleResponse);
}



//For Feedback

function handleFeedbackResponse(res_feedback) {
  document.querySelector('#feedback').innerHTML = res_feedback;
}

function getFeedback(feedback_txt) {
  let name = document.getElementById('writer-id').value;
  const groupName = document.querySelector('#group_name').innerHTML 
  url = `/api/${groupName}/${name}/feedback`;
  console.log(url)
  $.get(url, handleFeedbackResponse);
}


form.addEventListener('click', getFeedback);
form.addEventListener('click', getText);


//Gets Project Feedback and Display Feedback Wanted By The Project Owner

