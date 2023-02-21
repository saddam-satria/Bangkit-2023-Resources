
const navbar = document.querySelector(".header-content .nav-list")
const hamburgerBtn = document.querySelector(".header-content .header-title .humberger-menu")

const modalScreen = document.querySelector('.modal-screen')
const profileImage = document.querySelector(".main-content .profile-article .profile-image")

const socialModal = document.querySelector(".main-content .profile-article .profile-social-content .profile-social-modal");

hamburgerBtn.addEventListener('click', () => {
    navbar.classList.toggle('active')
})

profileImage.addEventListener("click", () => {
    modalScreen.classList.add("modal-active")
})


modalScreen.addEventListener("click", () => {
    modalScreen.classList.remove("modal-active")
})


socialModal.addEventListener("mouseenter", () => {
    socialModal.style.width = "80px"
})
socialModal.addEventListener("mouseleave", () => {
    socialModal.style.width = "auto"
})