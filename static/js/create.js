const submitBtn = document.querySelector(".btn-submit");

submitBtn.addEventListener("click", (event) => {
    const form = document.querySelector(".attendance-form");
    const formData = new FormData(form);

    fetch("/attendance/create/", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log("폼 데이터 제출 성공");
            window.location.href = "/attendance/";
        } else {
                console.log("폼 데이터 제출 실패");
        }
    })
    .catch(error => {
        console.log("폼 데이터 제출 오류");
        console.error(error);
    });

    event.preventDefault();
});