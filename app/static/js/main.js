// Main JS

(function() {

	//FlexSlider: Default Settings
	$.flexslider.defaults = {
		//Integer: Set the speed of the slideshow cycling, in milliseconds
	    slideshowSpeed: 9200
	}           
	
	$("#business_nav").on('click', function(e){
		$.get('services').html(data);
	});

	// var $tabsNav    = $('.tabs-nav'),
	// 	$tabsNavLis = $tabsNav.children('li'),
	// 	$tabContent = $('.tab-content');

	// $tabsNav.each(function() {
	// 	var $this = $(this);

	// 	$this.next().children('.tab-content').stop(true,true).hide().first().show();

	// 	$this.children('li').first().addClass('active').stop(true,true).show();
	// });

	// $tabsNavLis.on('click', function(e) {
	// 	var $this = $(this);

	// 	$this.siblings().removeClass('active').end().addClass('active');
		
	// 	$this.parent().next().children('.tab-content').stop(true,true).hide().siblings( $this.find('a').attr('href') ).fade
	// 	e.preventDefault();
	// });

})();
	