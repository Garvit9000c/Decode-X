const toggler = document.getElementById('toggle-check');
const heading = document.getElementById('inputHead');

const textSearch = document.getElementById('textSearch');
const imgSearch = document.getElementById('imgSearch');

toggler.addEventListener("click", ()=>{
    if(toggler.checked == true){
        heading.innerHTML = "Image Input:";
        textSearch.style.display = "none";
        imgSearch.style.display = "block";
    }else{
        heading.innerHTML = "Text Input:";
        textSearch.style.display = "block";
        imgSearch.style.display = "none";
    }
});