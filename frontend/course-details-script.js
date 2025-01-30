document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const courseId = urlParams.get("id");

    if (courseId) {
        fetch(`http://localhost:8000/api/courses/${courseId}/detail/`,{
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("token")
            } 
        })
            .then(response => response.json())
            .then(course => {
                document.getElementById("detailTitle").textContent = course.title || "N/A";
                document.getElementById("detailDescription").textContent = course.description || "N/A";
                document.getElementById("detailDate").textContent = new Date(course.date).toLocaleDateString();
            })
            .catch(error => console.error("Error fetching course details:", error));
    } else {
        document.getElementById("detailsContainer").innerHTML = "<p>Invalid course ID.</p>";
    }
});