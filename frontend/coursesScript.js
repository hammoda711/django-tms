document.addEventListener("DOMContentLoaded", function () {
    fetchCourses();
});

function fetchCourses() {
    fetch("http://localhost:8000/api/courses/", {
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token")
        }
    })
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("coursesTableBody");
            tableBody.innerHTML = ""; // Clear existing data

            data.forEach(course => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${course.title || "N/A"}</td>
                    <td>${course.description || "N/A"}</td>
                      <td>
                                <button class="details-btn" onclick="updateCourse(${course.id})">Update Course</button>
                                <button class="details-btn" onclick="showCourse(${course.id})">Show Details</button>
                                <button class="delete-btn" onclick="deleteCourse(${course.id})">Delete</button>
                            </td>
                `;

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error("Error fetching courses:", error));
}

function deleteCourse(courseId) {
    if (!confirm("Are you sure you want to delete this course?")) return;

    fetch(`http://localhost:8000/api/courses/${courseId}/`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token")
        }
    })
        .then(response => {
            if (response.ok) {
                alert("Course deleted successfully!");
                fetchCourses(); // Refresh the list
            } else {
                alert("Failed to delete the course.");
            }
        })
        .catch(error => console.error("Error deleting course:", error));
}

function updateCourse(courseId) {
    window.location.href = `update-course.html?id=${courseId}`;
}
function showCourse(courseId) {
    window.location.href = `course-details.html?id=${courseId}`;
}