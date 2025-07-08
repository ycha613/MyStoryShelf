// js for buttons adding / removing movies in user watched / watchlist for profile.html

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".toggle-button-profile");

  buttons.forEach(button => {
    button.addEventListener("click", async function () {
      const movieId = this.dataset.movieId;
      const listType = this.dataset.type;

      const response = await fetch(`/toggle_${listType}/${movieId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include"  // sends cookies for authentication
      });

      if (response.ok) {
        const data = await response.json();
        // delete row for that movie
        const movieRow = document.getElementById(`${listType}-${movieId}`);
        if (movieRow) {
            movieRow.remove();
        }
      } else {
        alert("Failed to update. Please try again.");
      }
    });
  });
});