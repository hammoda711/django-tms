document.addEventListener("DOMContentLoaded", function () {
	const urlParams = new URLSearchParams(window.location.search);
	const courseId = urlParams.get("id");

	if (!courseId) {
		alert("Invalid course ID.");
		window.location.href = "index.html";
		return;
	}

	// Fetch existing course data
	fetch(`http://localhost:8000/api/courses/${courseId}/detail/`, {
		headers: {
			"Authorization": "Bearer " + localStorage.getItem("token")
		}
	})
		.then(response => response.json())
		.then(course => {
			document.getElementById("title").value = course.title || "";
			document.getElementById("description").value = course.description || "";
			document.getElementById("date").value = course.date ? course.date.slice(0, 16) : "";
		})
		.catch(error => console.error("Error fetching course details:", error));

	// Handle form submission
	document.getElementById("updateForm").addEventListener("submit", function (event) {
		event.preventDefault();

		const updatedCourse = {
			title: document.getElementById("title").value,
			description: document.getElementById("description").value,
			date: new Date(document.getElementById("date").value).toISOString()
		};

		fetch(`http://localhost:8000/api/courses/${courseId}/`, {
			method: "PATCH",
			headers: {
				 "Content-Type": "application/json",
				"Authorization": "Bearer " + localStorage.getItem("token"),
			},
			body: JSON.stringify(updatedCourse)
		})
			.then(response => {
				if (response.ok) {
					alert("Course updated successfully!");
					window.location.href = "courses.html";
				} else {
					alert("Failed to update the course.");
				}
			})
			.catch(error => console.error("Error updating course:", error));
	});
});