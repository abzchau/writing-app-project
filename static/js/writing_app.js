console.log('Belsize Park');

let form = document.querySelector('#writer-id');

function handleResponse(res) {
  document.querySelector('#get-text').innerHTML = res;
}

function alertFuction(txt) {
  let name = document.getElementById('writer-id').value;
  url = `/api/writer/${name}`;
  console.log(url)
  $.get(url, handleResponse);
}

form.addEventListener('click', alertFuction);


// const form = document.querySelector('#get-writer');

// function handleResponse(res) {
//   document.querySelector('#get-text').innerHTML = res.fname;
// }

// function alertFuction(txt) {
//   txt.preventDefault();
//   let name = document.getElementById('writer-id').value;
    //  const groupName = document.querySelector('#group_name').innerHTML
//   url = `/api/writer/${groupName}/${name}`;
//   $.get(url, handleResponse);
// }

// form.addEventListener('submit', alertFuction);

// function handleResponse(res) {
//     document.querySelector('#get-text').innerHTML = 'boo'
// }

// function callHandleResponse(txt) {
//     alert('dodo')
//     // txt.preventDefault();
//     // let name = document.getElementById('writer-id').value;
//     // const groupName = document.querySelector('#group_name').innerHTML 
//     // url = `/api/writer/${groupName}/${name}`;
//     // $.get(url, handleResponse);
// }

// form.addEventListener('click', callHandleResponse);

// const groupName = document.querySelector('#group_name').innerHTML 

// const form = document.querySelector('#get-writer');

// function handleResponse(res) {
//   document.querySelector('#get-text').innerHTML = res.fname;
// }

// function alertFuction(txt) {
//   txt.preventDefault();
//   let name = document.getElementById('writer-id').value;
    //  const groupName = document.querySelector('#group_name').innerHTML
//   url = `/api/writer/${groupName}/${name}`;
//   $.get(url, handleResponse);
// }

// form.addEventListener('submit', alertFuction);