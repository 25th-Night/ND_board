const createBtn = document.querySelector(".attendance-create-btn");

createBtn.addEventListener("click", () => {
    window.location.href = "/attendance/create/"
})

let currentUrl = window.location.href;
let searchParams = new URLSearchParams(currentUrl);
let pageValue = searchParams.get("page", 1);
let page_nums = document.querySelectorAll('.page-link');
for (let i = 0; i < page_nums.length; i++) {
    if (page_nums[i].innertext == pageValue) {
        page_nums[i].style.backgroundColor = "#009879";
        page_nums[i].style.color = "white";
        break;
    }
}