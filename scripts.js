document.addEventListener("DOMContentLoaded", () => {
    const statusButtons = document.querySelectorAll(".status-btn");
    statusButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
            const action = e.target.value === "approved" ? "approve" : "disapprove";
            const confirmAction = confirm(`Are you sure you want to ${action} this application?`);
            if (!confirmAction) {
                e.preventDefault(); // Prevent form submission
            }
        });
    });
});
