$('.navbar-toggle').on('click', function(){
    if ($('#nav-mobile').hasClass('mobile-down')) {
        $('#nav-mobile').animate({
            top: -370
        }).removeClass('mobile-down')                
    } else {
        $('#nav-mobile').animate({
            top: 59
        }).addClass('mobile-down')                                
    }
})