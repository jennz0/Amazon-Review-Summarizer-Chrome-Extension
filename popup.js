var tags_container = document.getElementById("tags");

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

    chrome.runtime.sendMessage({url:tabs[0].url}, function(response) {
        console.log(response.status);
    });
});

chrome.storage.onChanged.addListener( function(data, namespaces) {

    const tags = data.tags.newValue;
    console.log(`[INFO][popup.js] changing tags in popup: ${tags}`);

    var row_container = document.createElement("li");
    const row_container_class = "list-group-item d-inline-flex p-1 border-0";
    row_container.className = row_container_class;
    var count = 0;
    for (let i = 0; i < tags.length; i++) {
        var tag_button = document.createElement("button");
        tag_button.type = "button";
        tag_button.className = "btn btn-outline-secondary btn-sm mx-1 disabled";
        tag_button.innerHTML = tags[i];
        row_container.appendChild(tag_button);
        count += 1;
        if (count == 3) {
            tags_container.appendChild(row_container);
            row_container = document.createElement("li");
            row_container.className = row_container_class;
            count = 0
        }
    }
    if (count != 0) {
        tags_container.appendChild(row_container);
    } 
});

