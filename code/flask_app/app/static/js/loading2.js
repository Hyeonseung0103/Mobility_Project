function startProcess() {
    var imageButton = document.getElementById('imageButton');
    var videoButton = document.getElementById('videoButton');
    var loadingLogo = document.getElementById('loadingLogo');
    
    let fileInput = document.querySelector('#fileButton').files[0];

    // 버튼 비활성화
    imageButton.disabled = true;
    videoButton.disabled = true;
  
    // 로딩 로고 표시
    loadingLogo.classList.remove('hidden');

    console.log(fileInput)

    let data = new FormData();
    data.append('file', fileInput);

    $.ajax({
        type: "POST",
        url: '/main/test',
        data: data,
        processData: false,
        contentType: false,
        success: function(){
            // 프로세스 완료 후 로딩 로고 숨김
            loadingLogo.classList.add('hidden');

            // 버튼 활성화
            imageButton.disabled = false;
            videoButton.disabled = false;
            console.log('success')
        }
    });
  }