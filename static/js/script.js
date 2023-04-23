setTimeout(function () {
        let messages = $('#msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }

    , 3000);

$(document).ready(function () {
    $('.summernote').summernote({
        height: 500,
    });
});