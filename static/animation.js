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
  document.getElementById('tryBtn').classList.add("ocupEffect");
  document.getElementById('con1P').classList.add("ocupEffect");
}

typeWriter();
setTimeout(disBtn, (speed * txt.length)+100 );
