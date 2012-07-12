
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
    var api_pre, api_suf, id, $this;
    $this = $(this);
    id = $this.val();
    api_pre = 'https://gdata.youtube.com/feeds/api/videos/';
    api_suf = '?v=2&alt=jsonc&callback=showVideoInfoOnRetrieve';

    // HACK: Since the callback function doesn't have an extra state
    // we "tag" the elements that must receive the video data with a class
    $('#title_' + $this.attr('id')).addClass('title' + id);
    $('#img_' + $this.attr('id')).addClass('img' + id);
    $('#desc_' + $this.attr('id')).addClass('desc' + id);

    $.getScript(api_pre + encodeURIComponent(id) + api_suf);
}

function showVideoInfoOnRetrieve(response) {
    id = response.data.id;
    $('.title' + id).text(response.data.title)
                    .removeClass('title' + id);
    $('.img' + id).attr('src', response.data.thumbnail.sqDefault)
                  .removeClass('img' + id);
    $('.desc' + id).text(response.data.description)
                   .removeClass('title' + id);
}

$(document).ready(function() {
    var $c = $('.youtube-embed-container');
    $c.children('input[type="text"]').change(parseURLOnKeyUpChange);
    $c.children('input[type="text"]').keyup(parseURLOnKeyUpChange);
    $c.children('input[type="hidden"]').change(retrieveVideoOnChange);
});
