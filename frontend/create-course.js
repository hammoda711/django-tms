document.getElementById("courseForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value + ":00Z"; // Convert to UTC format

    const courseData = {
        title: title,
        description: description,
        date: date
    };

    fetch("http://localhost:8000/api/courses/create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("token")
        },
        body: JSON.stringify(courseData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = "Course created successfully!";
        document.getElementById("courseForm").reset();
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("message").innerText = "Failed to create course.";
    });
});