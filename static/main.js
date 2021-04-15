const toggler = document.getElementById('toggle-check');
const toggler2 = document.getElementById('toggle-mode');
const heading = document.getElementById('inputHead');
const heading2 = document.getElementById('inputHead2');

const textSearch = document.getElementById('textSearch');
const imgSearch = document.getElementById('imgSearch');

toggler.addEventListener("click", ()=>{
    if(toggler.checked == true){
        heading.innerHTML = "Image Input";
        textSearch.style.display = "none";
        imgSearch.style.display = "block";
    }else{
        heading.innerHTML = "Text Input";
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
