const notes = [];

function ajouterNote() {
  const texte = prompt("Écris ta note :");

  if (texte && texte.trim() !== "") {
    notes.push({
      texte: texte.trim(),
      date: new Date().toLocaleString()
    });

    alert("Note enregistrée dans NEXUS !");
    console.log(notes);
  }
}

function rechercherNote() {
  const recherche = prompt("Que veux-tu retrouver ?");

  if (!recherche) return;

  const resultats = notes.filter(note =>
    note.texte.toLowerCase().includes(recherche.toLowerCase())
  );

  if (resultats.length === 0) {
    alert("NEXUS n'a trouvé aucune note.");
  } else {
    alert(
      resultats
        .map(note => `${note.texte}\n${note.date}`)
        .join("\n\n")
    );
  }
}