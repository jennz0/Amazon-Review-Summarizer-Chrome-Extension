// Exchange data with Flask
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        let page_url = request.url;
        
        fetch("http://127.0.0.1:5000/get_url", {
            method : 'POST',
            mode : 'cors',
            body: JSON.stringify({
                'page_url': page_url
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => res.json())
        .then(function (response) {
            let review_tags = response.tags
           
            chrome.storage.sync.set({ tags: review_tags },
                function() {
                    console.log(`[INFO][background.js] tags for this web page now set to ${review_tags}`);
            });
            console.log('Success:', response.success, response.status)
        }) 
        .catch(error => console.error('Error:', error));

        sendResponse({status: "Got url in the backend"});
    }
);