let items = document.querySelectorAll('.carousel .carousel-item')

items.forEach((el) => {
    if (window.matchMedia("(min-width: 768px)").matches)
    {
        const minPerSlide = 3
        let next = el.nextElementSibling
        for (var i=1; i<minPerSlide; i++) {
            if (!next) {
                // wrap carousel by using first child
                next = items[0]
            }
            let cloneChild = next.cloneNode(true)
            el.appendChild(cloneChild.children[0])
            next = next.nextElementSibling
        }
    }
})
