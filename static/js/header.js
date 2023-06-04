const toggleBtn = document.querySelector('.list-menu');
const menu = document.querySelector('.nav-menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
})