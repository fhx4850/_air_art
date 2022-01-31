$(document).ready(function(){
	$('.category_slider').slick({
		arrows:true,
		dots:false,
		slidesToShow:4,
		autoplay:false,
		speed:400,
		autoplaySpeed:800,
		responsive:[
			{
				breakpoint: 768,
				settings: {
					slidesToShow:2
				}
			},
			{
				breakpoint: 550,
				settings: {
					slidesToShow:1
				}
			}
		]
	});
});

