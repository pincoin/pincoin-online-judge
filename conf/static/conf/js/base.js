$(document).ready(function () {
    $('.dropdown-trigger').dropdown();

    $('.sidenav').sidenav();

    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true,
    });

    setInterval(function () {
        $('.carousel.carousel-slider').carousel('next');
    }, 3000);
});