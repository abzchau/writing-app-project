console.log("shadwell")

//Gets Reviewer Name And Display Reviewer Feedback

let formFeedback = document.querySelector('#reviewer-id');

function handleReviewerResponse(res_reviewerFeedback) {
    document.querySelector('#review').innerHTML = res_reviewerFeedback;
}

function getReviewer(txtReviewer) {
    let name = document.getElementById('reviewer-id').value;
    const projectName = document.querySelector('#project_name').innerHTML
    url = `/api/project/${projectName}/${name}`;
    console.log(url)
    $.get(url, handleReviewerResponse)
}


formFeedback.addEventListener('click', getReviewer);