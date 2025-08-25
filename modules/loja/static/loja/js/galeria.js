// Arquivo: modules/loja/static/loja/js/galeria.js

document.addEventListener('DOMContentLoaded', () => {
    const galeria = document.getElementById('galeriaEspelho');
    const fotos = document.querySelectorAll('.galeria-foto');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    let fotoAtual = 0;
    const totalFotos = fotos.length;

    // Função para mostrar a foto correta
    function mostrarFoto(index) {
        if (index >= totalFotos) {
            fotoAtual = 0;
        } else if (index < 0) {
            fotoAtual = totalFotos - 1;
        } else {
            fotoAtual = index;
        }
        const offset = -fotoAtual * 100;
        galeria.style.transform = `translateX(${offset}%)`;
    }

    // Eventos de clique para os botões
    prevBtn.addEventListener('click', () => {
        mostrarFoto(fotoAtual - 1);
    });

    nextBtn.addEventListener('click', () => {
        mostrarFoto(fotoAtual + 1);
    });
});