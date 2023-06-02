const toggleBtn = document.querySelector('.nav-toggleBtn');
const menu = document.querySelector('.nav-menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
})