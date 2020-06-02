
var html5webPiano = {};

html5webPiano.isMSIE = /*@cc_on!@*/false;
html5webPiano.START_NOTE_NUMBER = 48;
html5webPiano.END_NOTE_NUMBER = 90;
html5webPiano.OFFSET = [0, 40, 60, 105, 120, 180, 220, 240, 282, 300, 345, 360];

window.onload = function () {
    var i;
    var pianoArea = document.getElementById('pianoArea');

    //准备声音文件
    if (html5webPiano.isMSIE) {
        //如果是IE浏览器则使用mp3格式
        html5webPiano.sound = html5webPiano.mp3Sound;
    } else {
        html5webPiano.sound = html5webPiano.oggSound;
    }

    //设定钢琴键的事件
    if (document.addEventListener) {
        for (i = html5webPiano.START_NOTE_NUMBER; i <= html5webPiano.END_NOTE_NUMBER; i++) {
            setKeyEventListener(i);
        }
    } else if (document.attachEvent) {
        for (i = html5webPiano.START_NOTE_NUMBER; i <= html5webPiano.END_NOTE_NUMBER; i++) {
            setKeyAttachEvent(i);
        }
    }
}

//设置声音文件
function loadSoundFile(noteNumber, fileType) {
    var soundId = 'sound' + noteNumber;

    if (html5webPiano.sound) {
        html5webPiano.sound[soundId] = new Audio('sound/' + noteNumber + '.' + fileType);
    }
}

//设定钢琴键的点击事件(EventListener版)
function setKeyEventListener(noteNumber) {
    var keyId = '' + noteNumber;
    var bkeyID = 'b' + noteNumber;
    var key = document.getElementById(keyId);
    var bkey = document.getElementById(bkeyID);
    if (key) {
        key.addEventListener('mousedown', keyClick, false);
        key.addEventListener('mouseover', overKeyClick, false);
        // key.addEventListener('mouseleave', leaveKeyClick, false);
    }
    if (bkey) {
        bkey.addEventListener('mousedown', keyClick, false);
        bkey.addEventListener('mouseover', overKeyClick, false);
        // bkey.addEventListener('mouseleave', leaveKeyClick, false);
    }
}

//设定钢琴键的点击事件(AttachEvent版)
function setKeyAttachEvent(noteNumber) {
    var keyId = '' + noteNumber;
    var bkeyID = 'b' + noteNumber;
    var key = document.getElementById(keyId);
    var bkey = document.getElementById(bkeyID);
    if (key) {
        key.attachEvent('onmousedown', keyClick);
        key.attachEvent('onmouseover', overKeyClick);
        // key.attachEvent('onmouseout', leaveKeyClick);
    }
    if (bkey) {
        bkey.attachEvent('onmousedown', keyClick);
        bkey.attachEvent('onmouseover', overKeyClick);
        // bkey.attachEvent('onmouseout', leaveKeyClick);
    }
}

var isDown = false;
// var isOver = [];
var clickNum;
//按下钢琴键时
function keyClick() {
    var that = this;
    var noteNumber = that.id.replace('', '');
    playSound(noteNumber);
    console.log(noteNumber);
    isDown = true;
    clickNum = noteNumber;
}

function overKeyClick() {
    var that = this;
    var noteNumber = that.id.replace('', '');
    if (isDown == true && clickNum != noteNumber) {
        playSound(noteNumber);
        clickNum = noteNumber;
        // if (noteNumber.indexOf('b') == -1) {
        // 	if (isOver[parseInt(noteNumber)] != true) {
        // 		isOver[parseInt(noteNumber)] = true;
        // 		key = document.getElementById(noteNumber);
        // 		if (key) {
        // 			key.className = "piano-key wkey-active wkey key-hover";
        // 		}
        // 	}
        // }
        // else {
        // 	if (isOver[parseInt(noteNumber.substr(1)) + 100] != true) {
        // 		isOver[parseInt(noteNumber.substr(1)) + 100] = true;
        // 		bkey = document.getElementById(noteNumber);
        // 		if (bkey) {
        // 			bkey.className = "piano-key bkey-active bkey key-hover ";
        // 		}
        // 	}
        // }
    }
}

// function leaveKeyClick() {
// 	var that = this;
// 	var noteNumber = that.id.replace('', '');
// 	if (noteNumber.indexOf('b') == -1) {
// 		isOver[parseInt(noteNumber)] = false;
// 		key = document.getElementById(noteNumber);
// 		key.className = "piano-key  wkey key-hover";
// 	}
// 	else {
// 		isOver[parseInt(noteNumber.substr(1)) + 100] = false;
// 		bkey = document.getElementById(noteNumber);
// 		bkey.className = "piano-key bkey key-hover ";
// 	}
// }


document.onmouseup = function (e) {
    isDown = false;//清除此次状态
    clickNum = undefined;//鼠标滑动时不重复弹奏

}

//指定发出的声音
function playSound(noteNumber) {
    var soundId = 'sound' + noteNumber;
    var audio = null;

    if (html5webPiano.sound) {
        if (html5webPiano.sound[soundId]) {
            audio = new Audio(html5webPiano.sound[soundId]);
            audio.play();
        }
    }

}

isKeyDown = [];

document.onkeydown = function (e) {
    var pressEvent = e || window.event;
    var keyCode = '';
    if (pressEvent.keyCode) {
        keyCode = pressEvent.keyCode;
    } else if (pressEvent.charCode) {
        keyCode = pressEvent.charCode;
    } else if (pressEvent.which) {
        keyCode = pressEvent.which;
    }
    if (e.shiftKey) {
        if (isKeyDown[e.keyCode + 100] != true) {
            playSound('b' + e.keyCode);
            isKeyDown[e.keyCode + 100] = true;
        }
        bkey = document.getElementById('b' + e.keyCode);
        if (bkey) {
            bkey.className = "piano-key bkey-active bkey key-hover ";
        }
    } else if (!e.ctrlKey && !e.altKey) {
        if (isKeyDown[e.keyCode] != true) {
            playSound(e.keyCode);
            isKeyDown[e.keyCode] = true;
        }
        key = document.getElementById(e.keyCode);
        if (key) {
            key.className = "piano-key wkey-active wkey key-hover";
        }
    }

};

document.onkeyup = function (e) {
    var pressEvent = e || window.event;
    var keyCode = '';
    if (pressEvent.keyCode) {
        keyCode = pressEvent.keyCode;
    } else if (pressEvent.charCode) {
        keyCode = pressEvent.charCode;
    } else if (pressEvent.which) {
        keyCode = pressEvent.which;
    }
    isKeyDown = false;
    if (e.shiftKey) {
        isKeyDown[e.keyCode + 100] = false;
        bkey = document.getElementById('b' + e.keyCode);
        if (bkey) {
            bkey.className = "piano-key bkey key-hover";
        }
    } else if (!e.ctrlKey && !e.altKey) {
        isKeyDown[e.keyCode] != false;
        key = document.getElementById(e.keyCode);
        if (key) {
            key.className = "piano-key wkey key-hover";
        }
    }

};
