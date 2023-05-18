document.addEventListener('click', function(e) {
    if(e.target.classList.contains('btn')) {
        const likes = e.target.closest('.top-row').querySelector('.likes')
        likes.innerText = parseInt(likes.innerText) + 1
    }
    // console.log(e.target)
    // console.log('function 1 running')
})
