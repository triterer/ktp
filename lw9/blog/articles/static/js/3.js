$(document).ready(function(){    
	$('.one-post').hover(function(event){        
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.5'}, 300);    
	}, function(event){
	 $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
	})
});

$(document).ready(function(){    
	$('.image').hover(function(event){        
		$(event.currentTarget).animate({width:'520'},300);    
		$(this).attr('src','static/pic2.png'); 
	}, function(event){
	 $(event.currentTarget).animate({width:'430'},300);
	 $(this).attr('src','static/pic1.png');
	})
});

/*
$(function(){
  $(".image").on({
   mouseenter: function(){
    $(this).attr('src','static/pic2.png');
  },
  mouseleave: function(){
    $(this).attr('src','static/pic1.png');
  }
  });
  
});
*/