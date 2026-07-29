// Get Form
const form = document.getElementById("musicLinksForm");

// Get Preview Container
const preview = document.getElementById("previewCards");

// Form Submit
form.addEventListener("submit", function (event) {

    event.preventDefault();

    // Get Input Values
    const spotify = document.getElementById("spotify").value;
    const youtube = document.getElementById("youtube").value;
    const apple = document.getElementById("apple").value;

    // Clear Previous Cards
    preview.innerHTML = "";

    // Create Cards
    createCard(
        "Spotify",
        spotify,
        "bi bi-spotify",
        "spotify"
    );

    createCard(
        "YouTube Music",
        youtube,
        "bi bi-youtube",
        "youtube"
    );

    createCard(
        "Apple Music",
        apple,
        "bi bi-apple",
        "apple"
    );

    // Clear Form
    form.reset();

});


// Function to Create Card
function createCard(platform, url, icon, colorClass) {

    // Extract Username / Handle
    let username = url.substring(url.lastIndexOf("/") + 1);

    // Card HTML
    preview.innerHTML += `

    <div class="col-md-4 mb-4">

        <div class="preview-card ${colorClass}">

            <i class="${icon}"></i>

            <h5>${platform}</h5>

            <p>${username}</p>

            <a href="${url}"
                target="_blank"
                class="btn btn-light">

                Visit

            </a>

        </div>

    </div>

    `;

}