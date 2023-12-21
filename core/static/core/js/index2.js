document.addEventListener('scroll', () => {
    const navbar = document.querySelector('navbar');

    if (window.scrollY > 0) {
        Headers.classList.add('scrolled');
    } else {
        Headers.classList.remove('scrolled');
    }
})