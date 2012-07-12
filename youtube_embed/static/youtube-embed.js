
function parseYoutubeURL(text) {
    var videoid, m, ret;
    if (text.indexOf('/') !== -1) {
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

function parseURLOnKeyUpChange() {
    var $this, url, id;
    $this = $(this);
    url = $this.val();
    id = parseYoutubeURL(url);

    $hid = $this.siblings('input[type="hidden"]');
    if ($hid.val() !== id) {
        $hid.val(id);
        if (id !== '') {
            $hid.trigger('change');
        }
    }
}

function retrieveVideoOnChange() {
    var api_pre, api_suf;
    api_pre = 'https://gdata.youtube.com/feeds/api/videos/';
    api_suf = '?v=2&alt=jsonc&callback=showVideoInfoOnRetrieve';
    $.getScript(api_pre + encodeURIComponent($(this).val()) + api_suf);
}

function showVideoInfoOnRetrieve(response) {
    $('#youtube-embed-title').text(response.data.title);
    $('#youtube-embed-img').attr('src', response.data.thumbnail.sqDefault);
    $('#youtube-embed-desc').text(response.data.description);
}

$(document).ready(function() {
    var $c = $('.youtube-embed-container');
    $c.children('input[type="text"]').change(parseURLOnKeyUpChange);
    $c.children('input[type="text"]').keyup(parseURLOnKeyUpChange);
    $c.children('input[type="hidden"]').change(retrieveVideoOnChange);
});
