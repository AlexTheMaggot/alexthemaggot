$(window).on('load', function () {
    $('.window').removeClass('window_loading');
    setTimeout(function () {
        $('.main-block').removeClass('main-block_loading');
    }, 500)
    $('#main-block__submit').on('click', function () {
        $('#form-block').removeClass('form-block_none');
        $('#main-block').addClass('main-block_closed');
        setTimeout(function () {
            $('#form-block').removeClass('form-block_closed');
            $('#main-block').addClass('main-block_none');
        }, 500)
    })
});