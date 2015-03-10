$(function () {
    $(document).ready(function () {

        function initPevNext() {
            if ($('.owl-pagination').children().length > 1) {
                $('.js-prev, .js-next').show();
            }
            else {
                $('.js-prev, .js-next').hide();
            }
        }

        var owl = $("#slideshow-owl");
        owl.owlCarousel({
            items: 4,
            itemsDesktop: [1500, 3],
            itemsTablet: [768, 2],
            itemsMobile: false
        });

        // Custom Navigation Events
        $(".js-next").click(function () {
            owl.trigger('owl.next');
        })
        $(".js-prev").click(function () {
            owl.trigger('owl.prev');
        })


        initPevNext();
        $(window).resize(function(){
           setTimeout(function(){
               initPevNext();
           }, 200);
        })

    });
});




