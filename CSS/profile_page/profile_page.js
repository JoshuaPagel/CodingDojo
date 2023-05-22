

var requestSpan = document.querySelector("#card-button");
var connectionSpan = document.querySelector("#connections");
var username = document.querySelector(".blue-button");

function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
    connectionSpan.innerText++;
}

function ignore(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
}

function edit() {
    username.innerText = "Marisa G";
}