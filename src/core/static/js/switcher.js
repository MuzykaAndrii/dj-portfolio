// Wait for the document to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the <html> element
    const htmlElement = document.querySelector("html");
  
    // Get the theme toggle checkbox
    const themeToggleCheckbox = document.getElementById("theme-switcher");
  
    // Check the current theme on page load (Optional)
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme) {
      htmlElement.setAttribute("data-bs-theme", currentTheme);
      themeToggleCheckbox.checked = currentTheme === "light";
    }
  
    // Function to toggle the theme
    function toggleTheme() {
      const newTheme = themeToggleCheckbox.checked ? "light" : "dark";
      htmlElement.setAttribute("data-bs-theme", newTheme);
  
      // Save the new theme preference to local storage (Optional)
      localStorage.setItem("theme", newTheme);
    }
  
    // Attach an event listener to the theme toggle checkbox
    themeToggleCheckbox.addEventListener("change", toggleTheme);
  });
  