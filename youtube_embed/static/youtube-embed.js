
function parseYoutubeURL(text) {
    var videoid, m, ret;
    if (/^https?\:\/\/.+/i.test(text)) {
        m = /[\?\&]v=([^\?\&]+)/.exec(text);
        if (m) {
            videoid = m[1];
        } else {
            videoid = '';
        }
    } else {
        videoid = text;
    }

    if (/^[A-Za-z0-9_\-]{11}$/.test(videoid) === false) {
        videoid = '';
    }

    return videoid;
}

//$.getScript( 'http://gdata.youtube.com/feeds/api/videos/' + encodeURIComponent( videoid ) + '?v=2&alt=json-in-script&callback=youtubeFetchDataCallback' );

function parseURLOnKeyUpChange() {
    var $this, url, id;
    $this = $(this);
    url = $this.val();
    id = parseYoutubeURL(url);

    $hid = $this.siblings('input[type="hidden"]');
    if ($hid.val() !== id) {
        $hid.val(id);
        $hid.trigger('change');
    }
}

function retrieveVideoOnChange() {
    console.log($(this).val());
}

$(document).ready(function() {
    var $c = $('.youtube-embed-container');
    $c.children('input[type="text"]').change(parseURLOnKeyUpChange);
    $c.children('input[type="text"]').keyup(parseURLOnKeyUpChange);
    $c.children('input[type="hidden"]').change(retrieveVideoOnChange);
});
