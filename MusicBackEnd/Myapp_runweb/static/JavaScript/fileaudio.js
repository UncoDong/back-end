function playFile() {
    console.log("调用")
    var fileDom = document.getElementById('file');
    var fileName = fileDom.value;
    var audioDom = document.getElementById('audio');
    audioDom.setAttribute('src', fileName);
    audioDom.className = 'audio audio-after'
}
var setIntervalFun = null;

function getFileName() {
    console.log(123)
    var fileName = document.getElementById('file').value;
    if (fn != fna) {
        console.log(fn, fna)
        clearInterval(setIntervalFun);
        fn = fna;
    }
    fna = fileName;
    document.getElementById('fname').innerHTML = fileName.split('\\').pop();
}

var fn = "";
var fna = "";


document.getElementById('filebtn').addEventListener("click", function () {
    document.getElementById('file').click();
    setIntervalFun = setInterval(getFileName, 1000);

})