'use strict'

/*
========================================
    Preloader
========================================
*/
$(window).on('load', function() {
    $('#preloader').delay(200).fadeOut('slow');
    $('body').delay(200).css({
        'overflow': 'visible'
    });
});

/* responsive menu  */

jQuery(document).ready(function() {
    jQuery('#mobile-menu').meanmenu({
        meanMenuContainer: ".mobile-menu",
        meanScreenWidth: "991",
        meanRevealPosition: "right",
    });
});

/* ===============================================
        AddClass menu js
   ===============================================
*/

$(window).on('scroll', function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 200) {
        $(".navigation-area").addClass("shrinkheader");
    } else {
        $(".navigation-area").removeClass("shrinkheader");
    }
});

/* 
========================================
    SearchBar
========================================
*/

$(document).ready(function() {
    $('.search-open').on('click', function() {
        $('.search-bar').addClass('active');
        $('.search-close, .close-toggle-body').addClass('open');
    });
    $('.search-close, .close-toggle-body').on('click', function() {
        $('.search-bar').removeClass('active');
        $('.search-close, .close-toggle-body').removeClass('open');
    });
});

/* 
========================================
    Date Picker
========================================
*/

$('.date-input').datepicker({
    format: 'dd/mm/yyyy',
    /* startDate: '-30d', */
});

/* 
========================================
    data paroller
========================================
*/

$("[data-paroller-factor]").paroller();

/* 
========================================
    data background
========================================
*/
$(document).ready(function() {

    $("[data-background]").each(function() {
        $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
    });

    $("[data-bg-color]").each(function() {
        $(this).css("background", $(this).attr("data-bg-color"))
    });

});


/* 
========================================
    Nice Select
========================================
*/

$(document).ready(function() {
    $('select').niceSelect();
});


/* 
========================================
    Tab
========================================
*/

$('ul.tabs li').on('click', function() {
    var tab_id = $(this).attr('data-tab');

    $('ul.tabs li').removeClass('active');
    $('.tab-content').removeClass('active');

    $(this).addClass('active');
    $("#" + tab_id).addClass('active');
});



/*
========================================
counter odometer
========================================
*/

$(".counter-count").each(function() {
    $(this).isInViewport(function(status) {
        if (status === "entered") {
            for (var i = 0; i < document.querySelectorAll(".odometer").length; i++) {
                var el = document.querySelectorAll('.odometer')[i];
                el.innerHTML = el.getAttribute("data-odometer-final");
            }
        }
    });
});


/*
========================================
accordion
========================================
*/

$('.faq-contents .faq-title').on('click', function(e) {
    var element = $(this).parent('.faq-item');
    if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('.faq-panel').removeClass('open');
        element.find('.faq-panel').slideUp(300, "swing");
    } else {
        element.addClass('open');
        element.children('.faq-panel').slideDown(300, "swing");
        element.siblings('.faq-item').children('.faq-panel').slideUp(300, "swing");
        element.siblings('.faq-item').removeClass('open');
        element.siblings('.faq-item').find('.faq-title').removeClass('open');
        element.siblings('.faq-item').find('.faq-panel').slideUp(300, "swing");
    }
});

/* 
========================================
    slick slide
========================================
*/

/* Testimonial */

$('.testimonial-slider').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    infinite: true,
    swipe: true,
    swipeToSlide: true,
    dots: false,
    arrows: false,
    nextArrow: '<i class="las la-long-arrow-alt-right"></i>',
    prevArrow: '<i class="las la-long-arrow-alt-left"></i>',
    autoplay: true,
    autoplaySpeed: 3000,
    pauseOnHover: true,
    responsive: [{
        breakpoint: 992,
        settings: {
            slidesToShow: 1,
        }
    }, ]
});

/* About Slider */

$('.about-service-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    nextArrow: '<i class="las la-angle-right"></i>',
    prevArrow: '<i class="las la-angle-left"></i>',
    dots: false,
    fade: false,
    swipeToSlide: true,
});

/* Brands */

$('.brands-slider').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    infinite: true,
    swipe: true,
    swipeToSlide: true,
    dots: false,
    arrows: false,
    nextArrow: '<i class="las la-long-arrow-alt-right"></i>',
    prevArrow: '<i class="las la-long-arrow-alt-left"></i>',
    autoplay: true,
    autoplaySpeed: 2000,
    pauseOnHover: true,
    responsive: [{
            breakpoint: 1200,
            settings: {
                slidesToShow: 4,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
    ]
});

/* 
========================================
    video
========================================
*/

$('.video-play-btn').magnificPopup({
    type: 'iframe',
});

/*
========================================
    Line ProgressBar
========================================
*/

$('.line-progress1').LineProgressbar({
    fillBackgroundColor: '#4073dd',
    backgroundColor: '#789ce6',
    radius: '30px',
    duration: 3000,
    ShowProgressCount: true,
    width: '100%',
    height: '10px',
    percentage: 75,
});

$('.line-progress2').LineProgressbar({
    fillBackgroundColor: '#4073dd',
    backgroundColor: '#789ce6',
    radius: '30px',
    duration: 3000,
    ShowProgressCount: true,
    width: '100%',
    height: '10px',
    percentage: 75,
    percentage: 85,
});
$('.line-progress3').LineProgressbar({
    fillBackgroundColor: '#4073dd',
    backgroundColor: '#789ce6',
    radius: '30px',
    duration: 3000,
    ShowProgressCount: true,
    width: '100%',
    height: '10px',
    percentage: 75,
    percentage: 65,
});
$('.line-progress4').LineProgressbar({
    fillBackgroundColor: '#4073dd',
    backgroundColor: '#789ce6',
    radius: '30px',
    duration: 3000,
    ShowProgressCount: true,
    width: '100%',
    height: '10px',
    percentage: 75,
    percentage: 95,
});

/* 
========================================
    Blog Pagination
========================================
*/

$(document).ready(function() {
    $('.blog-pagination li a').click(function() {
        $('.blog-pagination li a').removeClass("active");
        $(this).addClass("active");
    });
});

/* 
========================================
    Wow Animation
========================================
*/

// new WOW().in

/*
========================================
Scroll to top
========================================
*/

if ($('#scroll-top').length) {
    function scrollToTop() {
        var $scrollUp = $('#scroll-top'),
            $lastScrollTop = 0,
            $window = $(window);

        $window.on('scroll', function() {
            var st = $(this).scrollTop();
            if (st > $lastScrollTop) {
                $scrollUp.removeClass('show');
            } else {
                if ($window.scrollTop() > 200) {
                    $scrollUp.addClass('show');
                } else {
                    $scrollUp.removeClass('show');
                }
            }
            $lastScrollTop = st;
        });

        $scrollUp.on('click', function(evt) {
            $('html, body').animate({ scrollTop: 0 }, 600);
            evt.preventDefault();
        });
    }
    scrollToTop();
}