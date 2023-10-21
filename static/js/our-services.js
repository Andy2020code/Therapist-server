window.addEventListener('load', function() {
    div1.style.display = 'none'
    div2.style.display = 'none'
    div3.style.display = 'none'
    div4.style.display = 'none'
    div5.style.display = 'none'
    div6.style.display = 'none'
    div7.style.display = 'none'
    div8.style.display = 'none'
    div9.style.display = 'none'
    div10.style.display = 'none'
    div11.style.display = 'none'
    div12.style.display = 'none'
    div13.style.display = 'none'
    div14.style.display = 'none'
    div15.style.display = 'none'
})


let currentlyVisible = null;

        function hideShow(elementId) {
            const div = document.getElementById(elementId);
            
            if (currentlyVisible) {
                currentlyVisible.style.display = 'none';
            }
            
            if (div !== currentlyVisible) {
                div.style.display = 'block';
                currentlyVisible = div;
            } else {
                currentlyVisible = null;
            }
        }