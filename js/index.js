window.addEventListener('load', function() {
    div1.style.display = 'none'
    div2.style.display = 'none'
    div3.style.display = 'none'
    div4.style.display = 'none'
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