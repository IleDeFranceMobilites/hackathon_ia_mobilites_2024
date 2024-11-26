// Exemple : Mettre à jour le niveau de dangerosité d'une gare
const gares = [
    { name: "RER A", danger: "Élevé" },
    { name: "RER B", danger: "Moyen" },
    { name: "RER C", danger: "Bas" },
  ];
  
  const container = document.querySelector(".gares-container");
  
  gares.forEach((gare) => {
    const gareElement = document.createElement("div");
    gareElement.classList.add("gare");
    gareElement.innerHTML = `
      <span class="gare-icon">🚇</span>
      <span class="gare-name">${gare.name}</span>
      <span class="gare-danger">⚠️ Niveau : ${gare.danger}</span>
    `;
    container.appendChild(gareElement);
  });