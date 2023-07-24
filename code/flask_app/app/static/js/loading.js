function startProcess() {
    var imageButton = document.getElementById('imageButton');
    let fileInput = document.querySelector('#fileButton').files[0];
    var buttonName = imageButton.value; // 버튼의 ID 가져오기

    // 버튼 비활성화
    imageButton.disabled = true;
  
    // 로딩 로고 표시
    loadingLogo.classList.remove('hidden');

    console.log(fileInput)

    let data = new FormData();
    data.append('file', fileInput);
    data.append('button', buttonName); // 버튼의 ID 추가

    $.ajax({
        type: "POST",
        url: '/main/detect',
        data: data,
        datatype: html,
        processData: false,
        contentType: false,
        success: function(){
            // 프로세스 완료 후 로딩 로고 숨김
            loadingLogo.classList.add('hidden');

            // 버튼 활성화
            imageButton.disabled = false;
            console.log('success')
        }
    });
  }