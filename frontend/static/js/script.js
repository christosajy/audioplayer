
// TIME-DASED-GREETING 
let greeting = document.querySelector(".greeting")
let timeNow = new Date().getHours();

console.log(timeNow)

let subject = timeNow >= 3 && timeNow < 12
    ? "Good Morning"
    : timeNow >= 12 && timeNow < 16
        ? "Good Afternoon"
        : timeNow >= 16 && timeNow < 19
            ? "Good Evening"
            : "Good Night"

console.log(subject)

greeting.innerHTML = `<p>${subject}</p>`;


// HISTORY-BASED-FORWARD-BACKWARD
function goBack() {
    window.history.back();
}

function goNext() {
    window.history.forward();
}

// BUTTON-ACTIVE-CHANGE

document.getElementById("grp-btn1").addEventListener("click", function () {
    document.getElementById("grp-btn1").classList.add("active");
    document.getElementById("grp-btn2").classList.remove("active");
})

document.getElementById("grp-btn2").addEventListener("click", function () {
    document.getElementById("grp-btn2").classList.add("active");
    document.getElementById("grp-btn1").classList.remove("active");
})
