// Match poster sliding effect
var dots = document.querySelectorAll('.dot');
var matches = document.querySelectorAll('.slider .match');
var currentMatch = 0; // index of the first match 
const interval = 3000; // duration (speed) of the slide

// Change slide based on the dot clicked
dots.forEach(dot => {
    dot.addEventListener('click', function () {
        clearInterval(timer); // Stop automatic sliding
        currentMatch = Array.from(dots).indexOf(dot); // Find the index of the clicked dot
        changeSlide(currentMatch); // Show corresponding slide
        timer = setInterval(() => changeSlide(), interval); // Restart the timer
    });
});

function changeSlide(n) {
    if (n !== undefined) {
        currentMatch = n; // Use the provided index
    } else {
        currentMatch = (currentMatch + 1) % matches.length; // Move to the next slide in the loop
    }

    var slides = document.querySelector('.slides');
    slides.style.transform = `translateX(-${currentMatch * 100}%)`; // Shift slides horizontally

    // Update active dot
    dots.forEach(dot => dot.classList.remove('active'));
    dots[currentMatch].classList.add('active'); // Highlight the active dot
}

// Start automatic sliding
var timer = setInterval(() => changeSlide(), interval);