console.log('camden')


//Gets Text And Returns Misspelled Words

let formSpellChecker = document.querySelector('#mySpellBtn');

function handleSpellingResponse(res_spelling) {
    document.querySelector('#spellcheck').innerHTML = res_spelling;
}

function getSpellingCorrections(spelling_txt) {
    
    const projectName = document.querySelector('#project_name').innerHTML
    url = `/api/project/${projectName}/spellcheck`;
    console.log(url)
    $.get(url, handleSpellingResponse)
}

formSpellChecker.addEventListener('click', getSpellingCorrections)