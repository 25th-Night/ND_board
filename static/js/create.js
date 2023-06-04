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
    const uploadButton = document.querySelector('.input-upload');

    uploadButton.addEventListener('click', () => {
        const fileInput = document.getElementById('input_screenshot');
        fileInput.click();
    });

    const fileInput = document.getElementById('input_screenshot');
    const filenameContainer = document.querySelector('.upload-filename');
    const fileRemove = document.querySelector('.file-remove');

    fileInput.addEventListener('change', () => {
        const selectedFile = fileInput.files[0];

        const allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;

        if (!allowedExtensions.test(selectedFile.name)) {
            alert('jpg, jpeg, png, gif 파일만 업로드 가능합니다.');
            fileInput.value = '';
        } else if (selectedFile) {
            filenameContainer.textContent = selectedFile.name;
            filenameContainer.style.color = "#00F";
            filenameContainer.style.margin = "0 10px"
            filenameContainer.style.display = "flex";
            filenameContainer.style.justifyContent = "center";
            filenameContainer.style.alignItems = "center";
            fileRemove.style.display = 'block';
            fileRemove.style.height = "25px";
            fileRemove.style.padding = "0 10px"
            fileRemove.style.display = "flex";
            fileRemove.style.justifyContent = "center";
            fileRemove.style.alignItems = "center";
            fileRemove.style.border = "0.5px solid lightgray";
            fileRemove.style.borderRadius = "4px";
            fileRemove.style.cursor = "pointer";
        } else {
            filenameContainer.textContent = '';
        }
    });

    fileRemove.addEventListener('click', () => {
        fileInput.value = null;
        filenameContainer.textContent = '';
        fileRemove.style.display = 'none';
    });

    const submitBtn = document.querySelector('.btn-submit');

    submitBtn.addEventListener('click', (event) => {
        const form = document.querySelector('.question-form');

        var titleInput = document.getElementById('input_title');
        var contentInput = document.getElementById('input_content');
                
        if (titleInput.value && contentInput.value) {
            form.submit();
        } else {
            alert('제목과 내용은 필수 입력 항목입니다.')
        }
    })

    const questionListBtn = document.querySelector('.btn-question-list');

    questionListBtn.addEventListener("click", () => {
        window.location.href = "/question/"
    })
}
