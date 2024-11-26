// Fonction pour parser le CSV
function parseCSV(csv, delimiter = ';') {
    const lines = csv.split('\n'); // Diviser le CSV en lignes
    const headers = lines[0].split(delimiter);

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

function loadCSV() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0]; // Obtenir le fichier sélectionné

    if (!file) {
        alert('Veuillez sélectionner un fichier CSV.');
        return;
    }

    const reader = new FileReader();

    // Lire le fichier en tant que texte
    reader.onload = function (event) {
        const csvText = event.target.result;
        const data = parseCSV(csvText); // Parser le CSV en objets

        // Effacer les anciennes lignes ou marqueurs (si nécessaire)
        map.eachLayer(layer => {
            if (layer instanceof L.Polyline || layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

        // Créer une enveloppe pour ajuster les limites de la carte
        const bounds = L.latLngBounds();

        // Fonction pour déterminer la couleur en fonction de l'indice
        function getColor(indice) {
            if (indice <= 0.2) return 'red';
            if (indice <= 0.4) return 'orange';
            if (indice <= 0.6) return 'yellow';
            if (indice <= 0.8) return '#2ea822';
            return '#007c01';
        }

        // Parcourir chaque ligne du fichier et tracer un trajet
        data.forEach(row => {
            const latA = parseFloat(row['Lat_A']);
            const longA = parseFloat(row['Long_A']);
            const latB = parseFloat(row['Lat_B']);
            const longB = parseFloat(row['Long_B']);
            const indiceTroncon = parseFloat(row['Indice_troncon_AB']); // Indice du tronçon

            if (!isNaN(latA) && !isNaN(longA) && !isNaN(latB) && !isNaN(longB) && !isNaN(indiceTroncon)) {
                // Déterminer la couleur du chemin en fonction de l'indice
                const color = getColor(indiceTroncon);

                // Ajouter les points aux limites
                bounds.extend([latA, longA]);
                bounds.extend([latB, longB]);

                // Créer une polyligne entre les deux points
                const polyline = L.polyline(
                    [
                        [latA, longA],
                        [latB, longB],
                    ],
                    {
                        color: color,
                        weight: 10,
                        opacity: 1,
                        lineJoin: 'round',
                    }
                ).addTo(map);

                // Ajouter des marqueurs pour chaque gare avec leurs infos
                const iconA = L.divIcon({
                    className: 'icon-a',
                    html: `<b style="color: blue;">O</b>`,
                    iconSize: [20, 20],
                });
                const iconB = L.divIcon({
                    className: 'icon-b',
                    html: `<b style="color: red;"></b>`,
                    iconSize: [0, 0],
                });

                L.marker([latA, longA], { icon: iconA })
                    .addTo(map)
                    .bindPopup(`Gare A : ${row['Gare_A']}<br>Indice : ${row['Indice_gare_A']}`);

                L.marker([latB, longB], { icon: iconB })
                    .addTo(map)
                    .bindPopup(`Gare B : ${row['Gare_B']}<br>Indice : ${row['Indice_gare_B']}`);
            }
        });

        // Centrer la carte pour inclure toutes les lignes tracées
        map.fitBounds(bounds);
    };

    reader.readAsText(file);
}
