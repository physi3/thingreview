function thingContent(e) {
    var content = e.nextElementSibling;
    var new_display = content.style.display == 'block' ? 'none' : 'block';
    // Set all others to display:none
    for (var i of document.getElementsByClassName('thing-content')) {
        i.style.display = 'none';
    }
    // Display clicked content
    content.style.display = new_display;
    return;
}
