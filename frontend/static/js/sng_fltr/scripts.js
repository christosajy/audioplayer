
let progress = document.getElementById("progress");
let song = document.getElementById("song");
let ctrlIcn = document.getElementById("ctrlIcn");
let vol = document.getElementById("vol");
let sbmt = document.getElementById("sbmtIcn");

song.onloadedmetadata = function () {
    progress.max = song.duration;
    progress.value = song.currentTime;
    song.pause();
    song.currentTime= 0
}

function playPause() {
    if (ctrlIcn.classList.contains("fa-pause")) {
        song.pause();
        ctrlIcn.classList.remove("fa-pause");
        ctrlIcn.classList.add("fa-play");
    }
    else {
        song.play();
        ctrlIcn.classList.remove("fa-play");
        ctrlIcn.classList.add("fa-pause");
    }
}

if (song.play()) {
    setInterval(() => {
        progress.value = song.currentTime;
    }, 500);
}

progress.onchange = function () {
    song.play();
    song.currentTime = progress.value;
    ctrlIcn.classList.add("fa-pause");
    ctrlIcn.classList.remove("fa-play");
}

function volCtrl() {
    var sound = document.getElementById("song");
    var slider = 0 + "." + document.getElementById("vol").value;
    sound.volume = slider;
}

function fastFwd(seconds) {
    song.currentTime += seconds;
}

function fastBkwd(seconds) {
    song.currentTime -= seconds;
}

function audioStop() {
    song.pause();
    song.currentTime= 0;
    ctrlIcn.classList.add("fa-play");
    ctrlIcn.classList.remove("fa-pause");
}

function audioMute() {
    if (volIcn.classList.contains("fa-volume-high")) {
        song.muted = !song.muted;
        volIcn.classList.add("fa-volume-xmark");
        volIcn.classList.remove("fa-volume-high");
    }
    else {
        song.muted = false;
        volIcn.classList.add("fa-volume-high");
        volIcn.classList.remove("fa-volume-xmark");
    }
}

function icnSbmt () {
    sbmt.click();
}