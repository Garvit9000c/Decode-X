//Loader Scripting
$(document).ready(function(){
    $(this).scrollTop(0);
});

$(window).on("load",function(){
    $(".loader").slideUp("slow");
    $("html").css("overflow-y", "scroll");
    typeWriter();
    setTimeout(disBtn, (speed * txt.length)+100 );
});

//TypeWrite Animation script
var i = 0;
var txt = 'Get Your Documents Summaries for better Understanding.'; /* The text */
var speed = 30; /* The speed/duration of the effect in milliseconds */

//function to give typing animation
function typeWriter() {
  if (i < txt.length) {
    document.getElementById("typedTxt").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
//function to wait for typeWriter function to end
function disBtn(){
  $('.buttons').addClass("ocupEffect");
  $('.pCon1').addClass("ocupEffect");
  $('.aCon1').addClass("ocupEffect");
  $('form').addClass("ocupEffect");
}

//Icon Animation
$('.aCon1').hover( () =>{
    $(".workI").addClass("iconA");
}, () => {
    $(".workI").removeClass("iconA");
});
$('.buttons').hover( () =>{
    $(".tryI").addClass("iconA1");
}, () => {
    $(".tryI").removeClass("iconA1");
});
