// functions.js

// JavaScript code
let activeTags = [];

// Toggle a tag when a button is clicked
function toggleTag(tag) {
    const tagIndex = activeTags.indexOf(tag);

    if (tagIndex === -1) {
        activeTags.push(tag); // Add tag to active tags if not already active
    } else {
        activeTags.splice(tagIndex, 1); // Remove tag if it's already active
    }

    updateActiveTags(); // Update the active tags display
    filterDisplayBoxes(); // Filter display boxes based on active tags
}

// Update the active tags display
function updateActiveTags() {
    const activeTagsList = document.getElementById('active-tags-list');
    activeTagsList.innerHTML = ''; // Clear the current active tags list

    activeTags.forEach(tag => {
        const tagElement = document.createElement('span');
        tagElement.textContent = tag;
        activeTagsList.appendChild(tagElement);
    });
}

// Filter the display boxes based on active tags
function filterDisplayBoxes() {
    const displayBoxes = document.querySelectorAll('.display-box');

    displayBoxes.forEach(box => {
        const boxTags = box.getAttribute('data-tag').split(' ');
        let isVisible = true;

        // Check if all active tags are present in the display box's tags
        for (let tag of activeTags) {
            if (!boxTags.includes(tag)) {
                isVisible = false;
                break;
            }
        }

        // Show or hide the display box based on whether it matches the active tags
        box.style.display = isVisible ? 'block' : 'none';
    });
}

// Clear all filters
function clearFilters() {
    activeTags = [];
    updateActiveTags();
    filterDisplayBoxes(); // Show all display boxes
}
