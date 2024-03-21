let greeting = document.querySelector(".greeting");

let timeNow = new Date().getHours();
console.log(timeNow)

let subject = timeNow >= 3 && timeNow < 12
    ? "Good Morning"
    : timeNow >= 12 && timeNow < 16
        ? "Good Afternoon"
        : timeNow >= 186 && timeNow < 18
            ? "Good Evening"
            : "Good Night"
console.log(subject)

greeting.innerHTML = `<p>${subject}</p>`;