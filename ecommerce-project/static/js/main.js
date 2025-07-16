const slider = document.querySelector('.single-slider');

const slides = [
    {
        image: '/static/images/showcase/fruits.webp',
        title: 'Fresh Fruits Delivered',
        text: 'Order a variety of fresh fruits online and get them delivered to your doorstep.'
    },
    {
        image: '/static/images/showcase/packaged-food.png',
        title: 'Packaged Foods & Essentials',
        text: 'Shop for quality packaged foods and daily essentials at the best prices.'
    },
    {
        image: '/static/images/showcase/laptop.jpg',
        title: 'Shop Groceries Online',
        text: 'Experience the convenience of online grocery shopping from your home.'
    },
    {
        image: '/static/images/showcase/vegetables.jpg',
        title: 'Farm-Fresh Vegetables',
        text: 'Get fresh, organic vegetables picked and delivered the same day.'
    }
];

let index = 0;

function changeSlide(slideIndex = index) {
    const { image, title, text } = slides[slideIndex];

    // Add fade/slide class
    slider.classList.remove('slider-fade');
    void slider.offsetWidth; // force reflow to restart animation
    slider.classList.add('slider-fade');

    slider.style.backgroundImage = `url(${image})`;
    slider.querySelector('.main-title').textContent = title;
    slider.querySelector('p').textContent = text;

    index = (slideIndex + 1) % slides.length;
}

// Initial load
changeSlide();

// Auto slide every 4 seconds
setInterval(() => changeSlide(), 4000);

// Manual navigation
const navLinks = document.querySelectorAll('.slider-nav a');
navLinks.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const slideIndex = parseInt(link.getAttribute('data-index'));
        changeSlide(slideIndex);
        index = slideIndex + 1;
    });
});
// Highlight button when clicked
document.addEventListener("DOMContentLoaded", () => {
  const productButtons = document.querySelectorAll(".product-card .btn");

  productButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.classList.add("clicked");
      setTimeout(() => btn.classList.remove("clicked"), 200);
    });
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const browseBtn = document.querySelector(".cta .btn-secondary");

  if (browseBtn) {
    browseBtn.addEventListener("click", (e) => {
      if (browseBtn.getAttribute("href").startsWith("#")) {
        e.preventDefault();
        const targetId = browseBtn.getAttribute("href");
        document.querySelector(targetId).scrollIntoView({
          behavior: "smooth",
        });
      }
    });
  }
});
