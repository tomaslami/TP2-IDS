// Animacion de aparicion al hacer scroll usando Intersection Observer

document.addEventListener('DOMContentLoaded', function () {
    const elementos = document.querySelectorAll('.animar-aparecer');
    const observer = new window.IntersectionObserver((entradas) => {
        entradas.forEach(entrada => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add('aparecido');
                observer.unobserve(entrada.target);
            }
        });
    }, { threshold: 0.2 });

    elementos.forEach(el => observer.observe(el));
});
