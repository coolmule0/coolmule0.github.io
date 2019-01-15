function toggleVis() {
	//Nav element to show/hide
	var x = document.getElementById("nav");
	x.classList.toggle("minimized");
}

function animateBars() {
	var x = document.getElementById("hamburger");
	x.classList.toggle("change");
}

function setMobileProperties(){
	if(document.getElementById("hamburger").classList.contains("change")){
		toggleVis();
		animateBars();

	}
	else{
	}
}
function screenResize(){
	//make sure mobile screen settings are present
	if(window.innerWidth < 720){
		setMobileProperties();
	}
	else{
		if(document.getElementById("nav").classList.contains("minimized")){
			toggleVis();
			animateBars();
		}
	}
}

window.onload = function(){
	var x = document.getElementById("hamburger");
	x.addEventListener("click", animateBars);
	x.addEventListener("click", toggleVis);
	window.addEventListener("resize", screenResize);
	screenResize();
}

window.onresize = function(){
	
}
