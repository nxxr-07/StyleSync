async function addItem() {
    const itemName = document.getElementById("item-name").value;
    
    const response = await fetch("/api/items", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: itemName })
    });

    if (response.ok) {
        document.getElementById("item-name").value = ""; // Clear input
        loadItems(); // Reload the item list
    }
}


async function loadItems() {
    const response = await fetch("/api/items");
    const items = await response.json();
    const itemList = document.getElementById("item-list");
    itemList.innerHTML = ""; // Clear the list

    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item.name;
        li.addEventListener('click', () => deleteItem(item.id)); // Add click event to delete item
        itemList.appendChild(li);
    });
}

async function deleteItem(itemId) {
    const response = await fetch(`/api/items/${itemId}`, {
        method: "DELETE",
    });

    if (response.ok) {
        loadItems(); // Reload the item list
    }
}

// Load items when the page is loaded
window.onload = loadItems;




const bar = document.getElementById('bar');
const nav= document.getElementById("navbar");
const close= document.getElementById("close");


if(bar){
    bar.addEventListener('click', ()=>{
        nav.classList.add('active');
    })
}
if (close){
    close.addEventListener('click',()=>{
        nav.classList.remove('active')
    })
}

           // Get the cart count display element
let cartValue = document.getElementById('count-bag');

// Read the saved cart count from localStorage
let cartCount = localStorage.getItem('cartCount') ? parseInt(localStorage.getItem('cartCount')) : 0;

// Update the displayed cart count on page load
if(cartValue) {
  cartValue.textContent = cartCount;
}
let btn = document.querySelectorAll('.cart')
btn.forEach(link => {
  link.addEventListener("click", function(e) {
    
    cartCount++;
    if(cartValue) {
      cartValue.textContent = cartCount;
    }
    localStorage.setItem('cartCount', cartCount);

    // If you want to redirect after increment:
    // window.location.href = 'shop.html';
  });
})


// filters
const checkboxes = document.querySelectorAll('.filters-sidebar input[type="checkbox"]');
const selectedFiltersDiv = document.getElementById('selected-filters');
const products = document.querySelectorAll('.pro');
const priceSlider = document.getElementById("priceRange");
const priceValue = document.getElementById("priceValue");
const noProductsMessage = document.getElementById("no-products-message");

function updateFiltersAndProducts() {
  const selected = [];

  // Get selected filters
  checkboxes.forEach(checkbox => {
    if (checkbox.checked) {
      selected.push(checkbox.value.toLowerCase());
    }
  });

  // Get selected max price
  const maxPrice = parseInt(priceSlider.value);
  priceValue.textContent = `$${maxPrice}`;

  // Display selected filters
  selectedFiltersDiv.textContent = selected.length
    ? "Selected filters: " + selected.join(', ')
    : "No filters selected";

  let anyVisible = false;

  // Filter products
  products.forEach(product => {
    const categoryData = product.dataset.category || "";
    const productPrice = parseInt(product.dataset.price || "0");
    const categories = categoryData.toLowerCase().split(" ");

    const matchesCategory = selected.length === 0 || selected.every(filter => categories.includes(filter));
    const matchesPrice = productPrice <= maxPrice;

    const isMatch = matchesCategory && matchesPrice;
    product.style.display = isMatch ? "block" : "none";

    if (isMatch) anyVisible = true;
  });

  // Show/hide "No products found" message
  noProductsMessage.style.display = anyVisible ? "none" : "block";
}

// Event listeners
checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', updateFiltersAndProducts);
});
priceSlider.addEventListener('input', updateFiltersAndProducts);

// Initial call
updateFiltersAndProducts();