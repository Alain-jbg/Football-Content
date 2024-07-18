// Slider 1
var imgs1 = document.querySelectorAll('#slider-1 .slider img');
var dots1 = document.querySelectorAll('#slider-1 .dot');
var currentImg1 = 0;
const interval1 = 3000;

function changeSlide1(n) {
    for (var i = 0; i < imgs1.length; i++) {
        imgs1[i].style.opacity = 0;
        dots1[i].className = dots1[i].className.replace(' active', '');
    }
  
    if (n != undefined) {
        clearInterval(timer1);
        timer1 = setInterval(changeSlide1, interval1);
        currentImg1 = n;
    } else {
        currentImg1 = (currentImg1 + 1) % imgs1.length;
    }
  
    imgs1[currentImg1].style.opacity = 1;
    dots1[currentImg1].className += ' active';
}

var timer1 = setInterval(changeSlide1, interval1);

// Slider 2
var imgs2 = document.querySelectorAll('#slider-2 .slider img');
var dots2 = document.querySelectorAll('#slider-2 .dot');
var currentImg2 = 0;
const interval2 = 3000;

function changeSlide2(n) {
    for (var i = 0; i < imgs2.length; i++) {
        imgs2[i].style.opacity = 0;
        dots2[i].className = dots2[i].className.replace(' active', '');
    }
  
    if (n != undefined) {
        clearInterval(timer2);
        timer2 = setInterval(changeSlide2, interval2);
        currentImg2 = n;
    } else {
        currentImg2 = (currentImg2 + 1) % imgs2.length;
    }
  
    imgs2[currentImg2].style.opacity = 1;
    dots2[currentImg2].className += ' active';
}

var timer2 = setInterval(changeSlide2, interval2);