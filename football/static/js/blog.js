function adjustBackgroundPosition() {
    const hero = document.getElementById('hero');
    const heroHeight = hero.offsetHeight;
    const windowHeight = window.innerHeight;

    if (heroHeight < windowHeight) {
        hero.style.backgroundPosition = 'center top';
    } else {
        hero.style.backgroundPosition = 'center center';
    }
}

window.addEventListener('resize', adjustBackgroundPosition);
document.addEventListener('DOMContentLoaded', adjustBackgroundPosition);