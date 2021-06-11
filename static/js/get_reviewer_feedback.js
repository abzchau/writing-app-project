console.log("shadwell")

//Gets Reviewer Name And Display Reviewer Feedback

let formFeedback = document.querySelector('#reviewer-id');

function handleReviewerResponse(resReviewerFeedback) {
    document.querySelector('#review').innerHTML = resReviewerFeedback;
}

function getReviewer(txtReviewer) {
    let name = document.getElementById('reviewer-id').value;
    const projectName = document.querySelector('#project_name').innerHTML
    url = `/api/project/${projectName}/${name}`;
    console.log(url)
    $.get(url, handleReviewerResponse)
}


formFeedback.addEventListener('click', getReviewer);



//This closes the modal

let submitProject = document.getElementById('submit_project');

function closeModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none";
}

submitProject.addEventListener('submit', closeModal)