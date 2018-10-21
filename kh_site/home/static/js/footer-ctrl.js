$('#consult').on('click', () => {
    $('#mailing-list-overlay').show()
    $('body').addClass("noscroll")
})

let closeEverything = () => {
    console.log('working')
    $('#mailing-list-overlay').hide()
    $('body').removeClass("noscroll")
}

$('#mailing-list-bypass').on('click', closeEverything)
$('#mc-embedded-subscribe-form').on('submit', closeEverything)
$('.close-overlay').on('click', closeEverything)
