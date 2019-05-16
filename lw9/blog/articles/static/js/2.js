
var clsheaders = document.getElementsByClassName("one-post");
for (var i = 0; i<clsheaders.length; i++)
{ 
	clsheaders[i].addEventListener("click", function(e) { 
	if (e.target.parentElement.className == "one-post folded"){
		e.target.parentElement.className = "one-post";
	}
	else{
		e.target.parentElement.className = "one-post folded";
	}
});
}