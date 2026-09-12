import os
import json

# FICHIER LOCAL DE TA SÉCURITÉ NEXUS
FICHIER_GRAPHE = "nexus_graphe_local.json"

def alimenter_le_graphe_local_nexus(texte_brut):
    print("🧠 L'IA locale analyse le texte...")
    mots = texte_brut.split()
    mots_inutiles = ["le", "la", "les", "de", "des", "un", "une", "pour", "avec", "dans", "sur", "par", "qui", "que", "est", "sont"]
    concepts = list(set([mot.strip(".,!?()").capitalize() for mot in mots if len(mot) > 4 and mot.lower() not in mots_inutiles]))
    
    graphe = {"flux": [], "liens": {}}
    if os.path.exists(FICHIER_GRAPHE):
        with open(FICHIER_GRAPHE, "r", encoding="utf-8") as f:
            graphe = json.load(f)
            
    id_flux = len(graphe["flux"]) + 1
    graphe["flux"].append({"id": id_flux, "contenu": texte_brut})
    
    for concept in concepts:
        if concept not in graphe["liens"]:
            graphe["liens"][concept] = []
        graphe["liens"][concept].append(id_flux)
        
    with open(FICHIER_GRAPHE, "w", encoding="utf-8") as f:
        json.dump(graphe, f, indent=4, ensure_ascii=False)
        
    print(f"✅ SUCCÈS COMPLET ! Données enregistrées localement.")

# Note d'initialisation automatique au lancement
ma_note = "Initialisation reussie de l'application NEXUS sur l'ecran d'accueil"
alimenter_le_graphe_local_nexus(ma_note)
