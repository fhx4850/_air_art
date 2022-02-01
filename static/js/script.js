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
	document.getElementById('view_all_categories_btn').onclick = function(){
		let alert = document.getElementById('home_alert_place');
		showElement(alert);
		disableScrolling();
	}
	document.getElementById('close_alert').onclick = function(){
		let alert = document.getElementById('home_alert_place');
		hideElement(alert);
		enableScrolling();
	}
	document.getElementById('home-alert-bg').onclick = function(){
		let alert = document.getElementById('home_alert_place');
		hideElement(alert);
		enableScrolling();
	}

	if(document.getElementsByClassName('like_btn')){
		let q = document.getElementsByClassName('like_btn');
		for(let i = 0; i < q.length; i++){
			q[i].onclick = function(){
				like(q[i]);
			}
		}
	}
});

function disableScrolling(){
	let scroll_y=window.scrollY;
	let scroll_x=window.scrollX;
	window.onscroll=function(){
		window.scrollTo(scroll_x, scroll_y);
	};
}

function enableScrolling(){
	window.onscroll=function(){};
}

function showElement(elem){
	elem.style.opacity = '1';
	elem.style.visibility = 'visible';
}

function hideElement(elem){
	elem.style.opacity = '0';
	elem.style.visibility = 'hidden';
}

function like(elem){
	elem.classList.toggle('btn_red');
	// elem.style.fill = '#000';
}