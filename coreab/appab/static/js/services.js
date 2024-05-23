//openN = document.getElementsByClassName("card__btn")
//for (i in openN){
//    openN[i].addEventListener("click", function(){
//        document.getElementById("component").style.display='block'
//    })
//    spanN = document.getElementById("test2")
//    spanN.addEventListener("click", function(){
//        document.getElementById("component").style.display='none'
//    })
//}

//openN = document.getElementsByClassName("card__btn")
//for (i in openN){
//    openN[i].addEventListener("click", function(){
//    location.href = 'http://127.0.0.1:8000/test/'
//    })
//    spanN = document.getElementsByClassName("card__btn")
//    spanN.addEventListener("click", function(){
//        location.href = 'http://127.0.0.1:8000/test/'
//    })
//}
open = document.getElementById("modal")
let span = document.getElementById("test")

open.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='block'
})

span.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='none'
})
function record() {
location.href = "http://127.0.0.1:8000/service-appointment/";
}

let isBlurred = false;

function blurBackground() {
  document.getElementById("background").style.filter = "blur(5px)";
  isBlurred = true;
}

function unblurBackground() {
  document.getElementById("background").style.filter = "none";
  isBlurred = false;
}



