fetch("https://api.pexels.com/v1/search?query=people", { 
	headers: { 
		Authorization: "563492ad6f917000010000016dba63fdcee443c384f3b8757a9569e6" 
	} 
})
	.then(resp => {
    	return resp.json()
	})
	.then(data => {
    	console.log(data)
	})
