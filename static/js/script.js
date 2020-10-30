function toggleHeaderItems() {
    var headerItems = document.getElementById('header-items');
    /* Check in dropdown mode (flex-direction should be column) */
    var style = document.defaultView.getComputedStyle(headerItems);
    var flexDirection = style.flexDirection;
    if (flexDirection == 'column') {
        /* Toggle display */
        var display = style.display;

        headerItems.style.display = display == 'none' ? 'flex' : 'none';
    } else {
        /* Can't toggle a dropdown if there isn't one!
         * But also, check that header-items are displayed. */
        if (style.display != 'flex') {
            clearHeaderItemsStyle();
        }
        console.log('Thing Review rules!');
    }
    return;
}

function clearHeaderItemsStyle() {
    var headerItems = document.getElementById('header-items');
    if (headerItems.style) {
        /* Empty inline to default to CSS. */
        headerItems.style.display = '';
    }
    return;
}

/* Ensure that a resize will not remove access to header items */
window.addEventListener('resize', clearHeaderItemsStyle);

function thingContent(e) {
    var content = e.nextElementSibling;
    var new_display = content.style.display == 'block' ? 'none' : 'block';
    /* Set all others to display:none */
    for (var i of document.getElementsByClassName('thing-content')) {
        i.style.display = 'none';
    }
    /* Display clicked content */
    content.style.display = new_display;
    return;
}
