var img1 = ran()
img1.src ="img1.jpg"

var img2 = ran()
img1.src ="img2.jpg"

var img3 = ran()
img1.src ="img3.jpg"

var img4 = ran()
img1.src ="img4.jpg"

var img5 = ran()
img1.src ="img5.jpg"

function ran() {
    var randomNumber = Math.floor((Math.random()*5)+1);
    document.getElementById("img").src="img"+randomNumber+".jpg";
}