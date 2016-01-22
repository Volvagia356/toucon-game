function generateMaps() {
    for (var map_id in questions) {
        var map = questions[map_id]
        var map_elmt = $('<div/>', {
            'id': map_id,
            'class': 'map',
        });
        map_elmt.css('background-image', "url(img/" + map_id + ".png)");

        for (var node_id in map) {
            var node = map[node_id];
            var node_elmt = $('<div/>', {
                'class': 'node',
                'data-map': map_id,
                'data-node': node_id,
            });
            node_elmt.css('left', node.x + "px");
            node_elmt.css('top', node.y + "px");
            node_elmt.click(showModal);
            map_elmt.append(node_elmt);
        }

        $('body').append(map_elmt);
    }
}

function fillMapList() {
    for (var i in map_order) {
        var map_id = map_order[i];
        var list_elmt = $('<li/>', {
            'data-map': map_id,
        });
        list_elmt.text(map_id);
        list_elmt.click(function() {
            showMap($(this).data('map'));
        });
        $('#map-list').append(list_elmt);
    }
}

function showModal() {
    var elem = $(this)
    var map_id = elem.data('map');
    var node_id = elem.data('node');
    var question = questions[map_id][node_id];
    $('#question').text(question.question);
    $('#answer').text(question.answer);
    $('#modal').fadeIn();
}

function hideModal() {
    $('#modal').fadeOut(400 ,function() {
        $('#answer').hide();
    });
}

function toggleAnswer() {
    $('#answer').toggle();
}

function showMap(map_id) {
    $('.map').hide();
    $('#' + map_id).show();
}


$(function() {
    generateMaps();
    fillMapList();
    $('#close-button').click(hideModal)
    $('#show-answer').click(toggleAnswer);
    showMap(map_order[0]);
});
