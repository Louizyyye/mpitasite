document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("site-header").innerHTML = `
    <header class="bg-blue-600 text-white p-4">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="font-bold text-xl">Mpita Medical</h1>
        <nav class="space-x-4">
          <a href="index.html" class="hover:underline">Home</a>
          <a href="about.html" class="hover:underline">About</a>
          <a href="services.html" class="hover:underline">Services</a>
          <a href="marketplace.html" class="hover:underline">Marketplace</a>
          <a href="contact.html" class="hover:underline">Contact</a>
        </nav>
      </div>
    </header>
  `;
});
