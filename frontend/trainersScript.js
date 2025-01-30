document.addEventListener("DOMContentLoaded", function () {
	localStorage.setItem(
		'token',
		'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4ODQ2NTcxLCJpYXQiOjE3MzgyNDE3NzEsImp0aSI6ImJlOGJmMGY0MDI1YzRiYWJiYTY3ZTA1NTczMzhjN2Q5IiwidXNlcl9pZCI6MX0.vHGk1KZ4ni4uFNSxh6pYVLyUKcFEstXj2kgDDmAMvZM'
	)
	fetchTrainers();
});

function fetchTrainers() {
	fetch("http://localhost:8000/api/trainers/",{
		headers:{
			"Authorization": "Bearer " + localStorage.getItem("token")
		}})
		.then(response => response.json())
		.then(data => {
			const tableBody = document.getElementById("trainersTableBody");
			tableBody.innerHTML = ""; // Clear existing data

			data.forEach(trainer => {
				const row = document.createElement("tr");

				row.innerHTML = `
					<td>${trainer.full_name || "N/A"}</td>
					<td>${trainer.specialization || "N/A"}</td>
					<td>${trainer.total_sessions}</td>
				`;

				tableBody.appendChild(row);
			});
		})
		.catch(error => console.error("Error fetching trainers:", error));
}