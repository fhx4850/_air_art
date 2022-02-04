$(document).ready(function () {
	if(document.getElementsByClassName('category_slider')){
		$('.category_slider').slick({
			arrows: true,
			dots: false,
			slidesToShow: 4,
			autoplay: false,
			speed: 400,
			autoplaySpeed: 800,
			responsive: [
				{
					breakpoint: 768,
					settings: {
						slidesToShow: 2
					}
				},
				{
					breakpoint: 550,
					settings: {
						slidesToShow: 1
					}
				}
			]
		});
	}
	if(document.getElementById('view_all_categories_btn')){
		document.getElementById('view_all_categories_btn').onclick = function () {
			let alert = document.getElementById('home_alert_place');
			showElement(alert);
			disableScrolling();
		}
	}
	if(document.getElementById('close_alert')){
		document.getElementById('close_alert').onclick = function () {
			let alert = document.getElementById('home_alert_place');
			hideElement(alert);
			enableScrolling();
		}
	}
	if(document.getElementById('home-alert-bg')){
		document.getElementById('home-alert-bg').onclick = function () {
			let alert = document.getElementById('home_alert_place');
			hideElement(alert);
			enableScrolling();
		}
	}
	if (document.getElementsByClassName('like_btn')) {
		let q = document.getElementsByClassName('like_btn');
		for (let i = 0; i < q.length; i++) {
			q[i].onclick = function () {
				like(q[i]);
			}
		}
	}
	if (document.getElementsByClassName("small_resolution_accordion")) {
		let button = document.getElementsByClassName("small_resolution_accordion");
		for (let i = 0; i < button.length; i++) {
			button[i].addEventListener("click", function () {
				this.classList.toggle("active");
				let panel = document.getElementById('prof_statistics_small');
				let arrow = document.getElementById('small_resolution_accordion_icon');
				if (panel.style.maxHeight) {
					panel.style.maxHeight = null;
					arrow.style.transform = 'rotateZ(0deg)';
					button[i].style.cssText = 'background-size: 0% 1px;';
				} else {
					button[i].style.cssText = 'background-size: 100% 1px;';
					arrow.style.transform = 'rotateZ(90deg)';
					arrow.style.transform = 'rotateZ(90deg)';
					panel.style.maxHeight = "110px";
				}
			});
		}
	}
	if(document.getElementById('small_resolution_folder_btn')){
		document.getElementById('small_resolution_folder_btn').onclick = function(){
			let alert = document.getElementById('home_alert_place');
			showElement(alert);
			disableScrolling();
		}
	}
	if(document.getElementById('all_folders_btn')){
		document.getElementById('all_folders_btn').onclick = function(){
			let alert = document.getElementById('home_alert_place');
			showElement(alert);
			disableScrolling();
		}
	}
});

function disableScrolling() {
	let scroll_y = window.scrollY;
	let scroll_x = window.scrollX;
	window.onscroll = function () {
		window.scrollTo(scroll_x, scroll_y);
	};
}

function enableScrolling() {
	window.onscroll = function () { };
}

function showElement(elem) {
	elem.style.opacity = '1';
	elem.style.visibility = 'visible';
}

function hideElement(elem) {
	elem.style.opacity = '0';
	elem.style.visibility = 'hidden';
}

function like(elem) {
	elem.classList.toggle('btn_red');
	// elem.style.fill = '#000';
}