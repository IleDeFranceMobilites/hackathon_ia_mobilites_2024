// Fonction pour parser le CSV
function parseCSV(csv, delimiter = ';') {
    const lines = csv.split('\n'); // Diviser le CSV en lignes
    const headers = lines[0].split(delimiter); // Extraire l'en-tête

    // Créer des objets pour chaque ligne
    return lines.slice(1).map(line => {
        const values = line.split(delimiter);
        const obj = {};
        headers.forEach((header, index) => {
            obj[header.trim()] = values[index]?.trim();
        });
        return obj;
    });
}

// Initialiser la carte
const map = L.map('map').setView([48.8566, 2.3522], 13);

// Ajouter une couche de tuiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Fonction pour charger et parser le fichier CSV
function loadCSV() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0]; // Obtenir le fichier sélectionné

    if (!file) {
        alert('Veuillez sélectionner un fichier CSV.');
        return;
    }

    const reader = new FileReader();

    // Lire le fichier en tant que texte
    reader.onload = function(event) {
        const csvText = event.target.result;
        const data = parseCSV(csvText); // Parser le CSV en objets

        // Effacer les anciens marqueurs (si nécessaire)
        map.eachLayer(layer => {
            if (layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

        console.log(data);
        // Ajouter des marqueurs en fonction des données du CSV
        data.forEach(row => {
            const latitude = row['Lat_A'];
            const longitude = row['Long_A'];
            const securite = parseFloat(row['Indice_gare_A']);
            const nom = row['Gare_A'];
            console.log(latitude,longitude);
            console.log(securite);
            if (!isNaN(securite)) {
                const [lat, lng] = [latitude,longitude];

                // Déterminer l'icône et sa classe en fonction de l'indice de sécurité
                if (securite >= 0 && securite < 0.2) {
                    iconPath =  'ressources/visage_effrayé.png';
                    iconClass = 'red-smiley';
                } else if (securite >= 0.2 && securite < 0.4) {
                    iconPath = 'ressources/visage_inquiet.png';
                    iconClass = 'yellow-smiley';
                } else if (securite >= 0.4 && securite <= 0.6) {
                    iconPath = 'ressources/visage_neutre.png';
                    iconClass = 'yellow-smiley';
                }else if (securite >= 0.6 && securite <= 0.8) {
                    iconPath = 'ressources/visage_sourire.png';
                    iconClass = 'green-smiley';
                }else if (securite >= 0.8 && securite <= 1) {
                    iconPath = 'ressources/visage_rieur.png';
                    iconClass = 'green-smiley';
                }

                // Créer une icône personnalisée
                const customIcon = L.icon({
                    className: iconClass,
                    iconUrl: iconPath,
                    iconSize: [25, 25],
                    iconAnchor: [16, 16],
                    popupAnchor: [0, -16],
                });

                // Ajouter un marqueur à la carte
                L.marker([lat, lng], { icon: customIcon })
                    .addTo(map)
                    .bindPopup(`Gare : ${nom}<br>Indice de sécurité : ${securite}`);
                
            }
        });
    };

    reader.readAsText(file); // Lire le fichier CSV comme texte
}
