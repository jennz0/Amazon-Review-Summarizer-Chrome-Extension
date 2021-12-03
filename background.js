// TODO: This is just a placeholder. Do the preprocessing of the reviews here.
let review_tags = ["placeholder", "tags", "placeholder", "tags", "placeholder", "tags", "placeholder", "tags", "placeholder"];

chrome.runtime.onInstalled.addListener(() => {
    chrome.storage.sync.set({ tags: review_tags },
        function() {
            console.log(`[INFO][background.js] tags for this web page now set to ${review_tags}`);
        });
});

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        let url = request.url;
        console.log(url);
        sendResponse({status: "Got url in the backend"});
    }
);