function checkStatsForToday(input){
    beforeLimit = 7;
    afterLimit = 8.5
    for (let i=0; i<input.length-1;i++){
        let before = input[i];
        let after = input[i+1];

        if ((before > beforeLimit) || (after > afterLimit)){
            exceedThresholdTeleMsg(before, after);
            break
        } else if ((before > beforeLimit - 0.5) || (after > afterLimit - 0.5)){
            approachingThresholdTeleMsg(before, after);
            break            
        }
    }
}

function approachingThresholdTeleMsg(after){
    let message = "Your glucose level is approaching the threshold limit. You might want to cut down on whatever food you have just eaten. Your current glucose level is at " + after
    axios.post(telegramURL + teleToken + '/sendMessage?chat_id=' + chatID +'&text='+ message)
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });
}

function exceedThresholdTeleMsg(before, after){
    let message = "There a sudden high spike in your glucose level today! Your previous glucose level was " + before + 
    " and your current level is at " + after + ". You might want to check what you have just eaten"
    axios.post(telegramURL + teleToken + '/sendMessage?chat_id=' + chatID +'&text='+ message)
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });
}

function subtractHours(date, hours) {
    date.setHours(date.getHours() - hours);

    return date;
}

// Upload File Function
function uploadFile(file) {
    let that = this;
    let formData = new FormData()
    formData.append('image', file)
    fetch("{% url 'CBG:read_CBG' %}", { 
        method: 'POST',
        body: formData 
    })
    .then (response => response.json())
    .then (data => {
        $('#reading').val(data.reading);
        $("#measurement").prop('selectedIndex') == 'mgdl' ? 0 : 1;
        // FileReader()
        const fileReader = new FileReader();
        // File Type 
        const fileType = file.type;
        // File Size 
        const fileSize = file.size;
        // If File Is Passed from the (File Validation) Function
        if (fileValidate(fileType, fileSize)) {
            // Add Class (drop-zoon--Uploaded) on (drop-zoon)
            dropZoon.classList.add('drop-zoon--Uploaded');
            // Show Loading-text
            loadingText.style.display = "block";
            // Hide Preview Image
            previewImage.style.display = 'none';
            // Remove Class (uploaded-file--open) From (uploadedFile)
            uploadedFile.classList.remove('uploaded-file--open');
            // Remove Class (uploaded-file__info--active) from (uploadedFileInfo)
            uploadedFileInfo.classList.remove('uploaded-file__info--active');
            // After File Reader Loaded 
            fileReader.addEventListener('load', function () {
            // After Half Second 
                setTimeout(function () {
                        // Add Class (upload-area--open) On (uploadArea)
                        uploadArea.classList.add('upload-area--open');
                        // Hide Loading-text (please-wait) Element
                        loadingText.style.display = "none";
                        // Show Preview Image
                        previewImage.style.display = 'block';
                        // Add Class (file-details--open) On (fileDetails)
                        fileDetails.classList.add('file-details--open');
                        // Add Class (uploaded-file--open) On (uploadedFile)
                        uploadedFile.classList.add('uploaded-file--open');
                        // Add Class (uploaded-file__info--active) On (uploadedFileInfo)
                        uploadedFileInfo.classList.add('uploaded-file__info--active');
                    }, 500) // 0.5s
                    // Add The (fileReader) Result Inside (previewImage) Source
                    previewImage.setAttribute('src', fileReader.result);
                    // Add File Name Inside Uploaded File Name
                    uploadedFileName.innerHTML = file.name;
                    // Call Function progressMove();
                    progressMove();
                })
                // Read (file) As Data Url 
                fileReader.readAsDataURL(file);
            } else { // Else
                this; // (this) Represent The fileValidate(fileType, fileSize) Function
            }            
    })
    .catch(error => {
        alert("Unable to get reading from your BEFORE MEAL picture, please try another image thank you!")
    })
}
function uploadFile2(file) {
    // FileReader()
    const fileReader = new FileReader();
    // File Type 
    const fileType = file.type;
    // File Size 
    const fileSize = file.size;
    // If File Is Passed from the (File Validation) Function
    if (fileValidate(fileType, fileSize)) {
        // Add Class (drop-zoon--Uploaded) on (drop-zoon)
        dropZoon2.classList.add('drop-zoon--Uploaded');
        // Show Loading-text
        loadingText2.style.display = "block";
        // Hide Preview Image
        previewImage2.style.display = 'none';
        // Remove Class (uploaded-file--open) From (uploadedFile)
        uploadedFile2.classList.remove('uploaded-file--open');
        // Remove Class (uploaded-file__info--active) from (uploadedFileInfo)
        uploadedFileInfo2.classList.remove('uploaded-file__info--active');
        // After File Reader Loaded 
        fileReader.addEventListener('load', function () {
        // After Half Second 
            setTimeout(function () {
                    // Add Class (upload-area--open) On (uploadArea)
                    uploadArea2.classList.add('upload-area--open');
                    // Hide Loading-text (please-wait) Element
                    loadingText2.style.display = "none";
                    // Show Preview Image
                    previewImage2.style.display = 'block';
                    // Add Class (file-details--open) On (fileDetails)
                    fileDetails2.classList.add('file-details--open');
                    // Add Class (uploaded-file--open) On (uploadedFile)
                    uploadedFile2.classList.add('uploaded-file--open');
                    // Add Class (uploaded-file__info--active) On (uploadedFileInfo)
                    uploadedFileInfo2.classList.add('uploaded-file__info--active');
                }, 500) // 0.5s
                // Add The (fileReader) Result Inside (previewImage) Source
                previewImage2.setAttribute('src', fileReader.result);
                // Add File Name Inside Uploaded File Name
                uploadedFileName2.innerHTML = file.name;
                // Call Function progressMove();
                progressMove2();
            })
            // Read (file) As Data Url 
            fileReader.readAsDataURL(file);
        } else { // Else
            this; // (this) Represent The fileValidate(fileType, fileSize) Function
        }
}
function uploadFile3(file) {
    let formData = new FormData()
    formData.append('image', file)
    fetch("{% url 'CBG:read_CBG' %}", { 
        method: 'POST',
        body: formData 
    })
    .then (response => response.json())
    .then (data => {
        $('#reading6').val(data.reading);
        $("#measurement").prop('selectedIndex') == 'mgdl' ? 0 : 1;
        // FileReader()
        const fileReader = new FileReader();
        // File Type 
        const fileType = file.type;
        // File Size 
        const fileSize = file.size;
        // If File Is Passed from the (File Validation) Function
        if (fileValidate(fileType, fileSize)) {
            // Add Class (drop-zoon--Uploaded) on (drop-zoon)
            dropZoon3.classList.add('drop-zoon--Uploaded');
            // Show Loading-text
            loadingText3.style.display = "block";
            // Hide Preview Image
            previewImage3.style.display = 'none';
            // Remove Class (uploaded-file--open) From (uploadedFile)
            uploadedFile3.classList.remove('uploaded-file--open');
            // Remove Class (uploaded-file__info--active) from (uploadedFileInfo)
            uploadedFileInfo3.classList.remove('uploaded-file__info--active');
            // After File Reader Loaded 
            fileReader.addEventListener('load', function () {
            // After Half Second 
                setTimeout(function () {
                        // Add Class (upload-area--open) On (uploadArea)
                        uploadArea3.classList.add('upload-area--open');
                        // Hide Loading-text (please-wait) Element
                        loadingText3.style.display = "none";
                        // Show Preview Image
                        previewImage3.style.display = 'block';
                        // Add Class (file-details--open) On (fileDetails)
                        fileDetails3.classList.add('file-details--open');
                        // Add Class (uploaded-file--open) On (uploadedFile)
                        uploadedFile3.classList.add('uploaded-file--open');
                        // Add Class (uploaded-file__info--active) On (uploadedFileInfo)
                        uploadedFileInfo3.classList.add('uploaded-file__info--active');
                    }, 500) // 0.5s
                    // Add The (fileReader) Result Inside (previewImage) Source
                    previewImage3.setAttribute('src', fileReader.result);
                    // Add File Name Inside Uploaded File Name
                    uploadedFileName3.innerHTML = file.name;
                    // Call Function progressMove();
                    progressMove3();
                })
                // Read (file) As Data Url 
                fileReader.readAsDataURL(file);
        } else { // Else
            this; // (this) Represent The fileValidate(fileType, fileSize) Function
        }
    })
    .catch(error => {
        alert("Unable to get reading from your AFTER MEAL picture, please try another image thank you!")
    })        
}

// Progress Counter Increase Function
function progressMove() {
    // Counter Start
    let counter = 0;
    // After 600ms 
    setTimeout(() => {
        // Every 100ms
        let counterIncrease = setInterval(() => {
        // If (counter) is equle 100 
        if (counter === 100) {
            // Stop (Counter Increase)
            clearInterval(counterIncrease);
        } else { // Else
            // plus 10 on counter
            counter = counter + 10;
            // add (counter) vlaue inisde (uploadedFileCounter)
            uploadedFileCounter.innerHTML = `${counter}%`
        }
        }, 100)
    }, 600)
}
function progressMove2() {
    let counter = 0;
    setTimeout(() => {
        let counterIncrease = setInterval(() => {
        if (counter === 100) {
            clearInterval(counterIncrease);
        } else {
            counter = counter + 10;
            uploadedFileCounter2.innerHTML = `${counter}%`
        }
        }, 100)
    }, 600)
}
function progressMove3() {
    let counter = 0;
    setTimeout(() => {
        let counterIncrease = setInterval(() => {
        if (counter === 100) {
            clearInterval(counterIncrease);
        } else {
            counter = counter + 10;
            uploadedFileCounter3.innerHTML = `${counter}%`
        }
        }, 100)
    }, 600)
}

// Simple File Validate Function
function fileValidate(fileType, fileSize) {
    // File Type Validation
    let isImage = imagesTypes.filter((type) => fileType.indexOf(`image/${type}`) !== -1);
    // If The Uploaded File Is An Image
    if (isImage.length !== 0) {
        // Check, If File Size Is 2MB or Less
        if (fileSize <= 3000000) { // 3MB :)
            return true;
        } else { // Else File Size
            return alert('Please Your File Should be 2 Megabytes or Less');
        }
    } else { // Else File Type 
        return alert('Please make sure to upload An Image File Type');
    }
}