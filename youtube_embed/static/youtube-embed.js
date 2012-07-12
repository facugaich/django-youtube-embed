
function parseYoutubeURL(url) {

}

function parseURLOnKeyUp() {
    console.log('pepe');
}

function parseURLOnChange() {
    console.log('pepe');
}

$(document).ready(function() {
    var $c = $('.youtube-embed-container');
    $c.children('input[type="text"]').change(parseURLOnChange);
    $c.children('input[type="text"]').keyup(parseURLOnKeyUp);
});
