var currentUrl = window.location.href;

if (currentUrl.split("/")[3] == "attendance") {
    let dateInput = document.getElementById('input_date');

    dateInput.addEventListener('change', function () {
        var selectedDate = new Date(this.value);
        var today = new Date();
        console.log(selectedDate);
        console.log(today);

        if (selectedDate > today) {
            alert('오늘 이후의 일자는 선택이 불가능합니다.');
            this.value = null;
        }
    })

    const submitBtn = document.querySelector('.btn-submit');

    submitBtn.addEventListener('click', (event) => {
        const form = document.querySelector('.attendance-form');

        var nameInput = document.getElementById('input_name');
        var dateInput = document.getElementById('input_date');
        var statusRadios = document.getElementsByName('status');
        const textArea = document.getElementById('input_reason');

        let hasSelectedRadio = false;

        for (let i = 0; i < statusRadios.length; i++) {
            if (statusRadios[i].checked) {
                hasSelectedRadio = true;
                break;
            }
        }
                
        if (dateInput.value && nameInput.value && hasSelectedRadio) {
            let selectedStatus;
            for (let i = 0; i < statusRadios.length; i++) {
                if (statusRadios[i].checked) {
                    selectedStatus = statusRadios[i].value;
                    break;
                }
            }

            if (selectedStatus > 1 && !textArea.value) {
                alert('"결석" 및 "일부 불참"의 경우, 사유를 반드시 작성해주세요.')
            } else {
                form.submit();
            }
        } else {
            alert('폼 작성이 완료되지 않았습니다.')
        }
    })

    const attendanceListBtn = document.querySelector('.btn-attendance-list');

    attendanceListBtn.addEventListener("click", () => {
        window.location.href = "/attendance/"
    })
} else if (currentUrl.split("/")[3] == "question") {
    // 여기에 작성
}


