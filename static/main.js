const toggler = document.getElementById('toggle-check');
const toggler2 = document.getElementById('toggle-mode');
const toggler3 = document.getElementById('alpha');
const heading = document.getElementById('inputHead');
const heading2 = document.getElementById('inputHead2');
const heading3 = document.getElementById('beta');

const textSearch = document.getElementById('textSearch');
const imgSearch = document.getElementById('imgSearch');

toggler3.addEventListener("click", ()=>{
    if(toggler3.checked == true){
        heading3.innerHTML = "Hindi";
    }else{
        heading3.innerHTML = "English";
    }

});

toggler.addEventListener("click", ()=>{
    if(toggler.checked == true){
        heading.innerHTML = "Image Input";
        heading3.innerHTML = "Hindi";
        textSearch.style.display = "none";
        imgSearch.style.display = "block";
    }else{
        heading.innerHTML = "Text Input";
        heading3.innerHTML = "English";
        textSearch.style.display = "block";
        imgSearch.style.display = "none";
    }

});

toggler2.addEventListener("click", ()=>{
    if(toggler2.checked == true){
        heading2.innerHTML = "Legal Mode";
    }else{
        heading2.innerHTML = "Summary Mode";
    }

});

