$(document).ready(function(){
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $parallaxElement = $('.image');
    $(window).scroll(function() { 
    	scrolled = $(window).scrollTop(); 
    	for (var i = 0; i < $parallaxElements.length; i++){ 
    		yPosition = (scrolled * 0.15*(i + 1)); 
    		$parallaxElements.eq(2-i).css({ top: yPosition }); 
    	}
    	yPosition = (scrolled * 0.25);
    	$parallaxElement.eq(0).css({ top: yPosition });
    }); 
}); 