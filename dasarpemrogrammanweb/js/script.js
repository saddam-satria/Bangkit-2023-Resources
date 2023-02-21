
const navbar = document.querySelector(".header-content .nav-list")
const hamburgerBtn = document.querySelector(".header-content .header-title .humberger-menu")

const modalScreen = document.querySelector('.modal-screen')
const profileImage = document.querySelector(".main-content .profile-article .profile-image")



hamburgerBtn.addEventListener('click', () => {
    navbar.classList.toggle('active')
})

profileImage.addEventListener("click", () => {
    modalScreen.classList.add("modal-active")
})


modalScreen.addEventListener("click", () => {
    modalScreen.classList.remove("modal-active")
})