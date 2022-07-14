const expandTaskBtns = document.querySelectorAll(".expand-task-btn");
const tasksName = document.querySelectorAll(".task-name");
const tasksDesc = document.querySelectorAll(".task-desc");

for (let i = 0; i < expandTaskBtns.length; i++) {
    expandTaskBtns[i].addEventListener("click", () => {
        tasksName[i].classList.toggle("expanded")
        tasksDesc[i].classList.toggle("desc-inactive");
    });
}