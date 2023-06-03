const createBtn = document.querySelector(".attendance-create-btn");

createBtn.addEventListener("click", () => {
    window.location.href = "/attendance/create/"
})

let currentUrl = window.location.href;
console.log(currentUrl);
var arr = currentUrl.split('page=')
var pageValue;
if (currentUrl.includes('page')) {
    pageValue = arr[arr.length -1]
} else {
    pageValue = 1
}

let page_nums = document.querySelectorAll('.page-link');
for (let i = 0; i < page_nums.length; i++) {
    if (page_nums[i].innerText == pageValue) {
        page_nums[i].style.backgroundColor = "#009879";
        page_nums[i].style.color = "white";
        break;
    }
}