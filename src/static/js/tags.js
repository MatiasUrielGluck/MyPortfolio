const tags = document.querySelectorAll('.tag');
for (const tag of tags) {
    tag.addEventListener('click', () => {
        tag.classList.toggle('active');
    });
}