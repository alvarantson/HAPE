function loader() {
	$(".loader").fadeIn(500);
};
function pop_up(pop_up_name){
	$("#"+pop_up_name).toggleClass("hidden");
};



$( document ).ready(function() {
	$(".loader").fadeOut(600);
});
if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
	$(".navbar-desktop").toggleClass("hidden");
	$(".desktop-spacer").toggleClass("hidden");
} else {
	$(".navbar-phone").toggleClass("hidden");
	$(".phone-spacer").toggleClass("hidden");
};

$('#shopping_cart_desktop').on("click", function(){
	$('.shopping_cart-dropdown').toggleClass("hidden");
});

$('#navbar_phone').on("click", function(){
	$('.navbar-phone-selector').toggleClass("hidden");
	$('#shopping_cart_phone').toggleClass("hidden");
	$('#navbar_phone').toggleClass("clicked");
});

$('#shopping_cart_phone').on("click", function(){
	$('.shopping_cart-phone').toggleClass("hidden");
	$('#navbar_phone').toggleClass("hidden");
	$('#shopping_cart_phone').toggleClass("clicked");
});



var a = $(".navbar").offset().top;

function scrollListener(){
	if($(document).scrollTop() > a && !window.location.pathname.includes("artists"))
	{   
		$('.navbar').css({"background-color":"rgba(0,0,0,.5)"});
	} else {
		$('.navbar').css({"background-color":"rgba(0,0,0,0)"});
	}
};

$(document).scroll(scrollListener);

scrollListener();