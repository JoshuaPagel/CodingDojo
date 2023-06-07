document.addEventListener('DOMContentLoaded', changeBannerImage);

function changeBannerImage() {
    const bannerImg = document.getElementById('bannerImg');
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');
    
    const images = ['stonepunk.png', 'pixel-ninjas-2.png', 'cafe-neko.png'];
    let currentIndex = 0;

    function updateImage() {
        bannerImg.src = images[currentIndex];
    }
    
    leftArrow.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateImage();
    });

    rightArrow.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % images.length;
        updateImage();
    })
}

function updateCartCount() {
    const cartCount = document.getElementById('cartCount');
    let count = parseInt(cartCount.innerText);
    count++;
    cartCount.innerText = count;
}

const buyBtn = document.getElementsByClassName('buyBtn');
for (let i = 0; i < buyBtn.length; i++) {
    buyBtn[i].addEventListener('click',updateCartCount);
}
