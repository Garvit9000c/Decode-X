var i = 0;
var txt = 'Get Your Documents Summaries for better Understanding.'; /* The text */
var speed = 30; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("typedTxt").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

function disBtn(){
  $('.buttons').addClass("ocupEffect");
  $('.pCon1').addClass("ocupEffect");
  $('.aCon1').addClass("ocupEffect");
}

typeWriter();
setTimeout(disBtn, (speed * txt.length)+100 );
