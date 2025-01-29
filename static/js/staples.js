const editButtons = document.getElementsByClassName("edit-btn");
const stapleForm = document.getElementById("comment_form");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("delete-btn");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let stapleId = e.target.getAttribute("staple_id");

        // Get list item details
        let stapleContent = document.getElementById(`staple${stapleId}`).innerText;

        // Match name from form
        let match = stapleContent.match(/^(.*)\s(\d+(\.\d+)?)\s(\w+)$/);

        // Extract item details
        if (match) {
            let name = match[1];
            let quantity = match[2];
            let measurementUnit = match[4];
        
            // Populate form fields
            document.getElementById("id_name").value = name;
            document.getElementById("id_quantity").value = quantity;
            document.getElementById("id_measurement_unit").value = measurementUnit;

            submitButton.innerText = "Update Item";
        } else {
            console.error("Could not parse staple content:", stapleContent);
        }
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let stapleId = e.target.getAttribute("staple_id");

        if (confirm("Are you sure you want to delete this item?")) {
            fetch(`/staples/delete/${stapleId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                }
            }).then(response => {
                if (response.ok) {
                    window.location.reload();
                } else {
                    alert("Error deleting item.");
                }
            });
        }
    });
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}