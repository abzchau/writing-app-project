console.log('Belsize Park');

//Gets User Name And Display User Text

let form = document.querySelector('#writer-id');

function handleResponse(res) {
  document.querySelector('#get-text').innerHTML = res;
}

function alertFunction(txt) {
  let name = document.getElementById('writer-id').value;
  const groupName = document.querySelector('#group_name').innerHTML 
  url = `/api/${groupName}/${name}`;
  console.log(url)
  $.get(url, handleResponse);
}

form.addEventListener('click', alertFunction);

