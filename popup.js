// Dynamically populate the frontend of the chrome extension.
// Get the tags container.
var tags_container = document.getElementById("tags");

chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    // Send response status
    chrome.runtime.sendMessage({ url: tabs[0].url }, function(response) {
        console.log(response.status);
    });
});

chrome.storage.onChanged.addListener(function(data, namespaces) {

    const tags = data.tags.newValue;
    console.log(`[INFO][popup.js] changing tags in popup: ${tags}`);

    // Get the row container.
    var row_container = document.createElement("li");
    // Row styling constant.
    const row_container_class = "list-group-item d-inline-flex p-1 border-0";
    row_container.className = row_container_class;
    var count = 0;
    // Iterate through all the tags.
    for (let i = 0; i < tags.length; i++) {
        // Create tag button
        var tag_button = document.createElement("button");
        tag_button.type = "button";
        // Set the button styling
        tag_button.className = "btn btn-outline-secondary btn-sm mx-1 disabled";
        tag_button.innerHTML = tags[i];
        // Append the button to the row container
        row_container.appendChild(tag_button);
        count += 1;
        if (count == 3) {
            // Change to another row if there are three tags in the row.
            tags_container.appendChild(row_container);
            row_container = document.createElement("li");
            row_container.className = row_container_class;
            count = 0
        }
    }
    // Append the last row.
    if (count != 0) {
        tags_container.appendChild(row_container);
    }
});