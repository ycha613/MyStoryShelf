// js for buttons adding / removing movies in user watched / watchlist for movie.html

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".toggle-button-movie");

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
        if (data.in_list) {
          this.textContent = `Remove from ${capitalize(listType)}`;
        } else {
          this.textContent = `Add to ${capitalize(listType)}`;
        }
      } else {
        alert("Failed to update. Please try again.");
      }
    });
  });

  function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1);
  }
});