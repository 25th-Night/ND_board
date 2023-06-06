var currentUrl = window.location.href;

if (currentUrl.includes("attendance")) {
    const attendanceCreateBtn = document.querySelector(".attendance-create-btn");

    attendanceCreateBtn.addEventListener("click", () => {
        window.location.href = attendanceCreateUrl;
    })
} else if (currentUrl.includes("question")) {
    const questionCreateBtn = document.querySelector(".question-create-btn");
    
    questionCreateBtn.addEventListener("click", () => {
        window.location.href = questionCreateUrl;
    })

    const questions = document.querySelector('.table-row-wrap');
    questions.addEventListener("click", (event) => {
        const clickedRow = event.target.closest('.table-row');
        if (clickedRow) {
            const questionId = clickedRow.dataset.id;
            if (questionId) {
                window.location.href = questionId + '/';
            }
        }
    })
}


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