# Cartographie des acteurs — Poulainville

Référentiel documenté du projet de reconversion de l'ancienne usine **Ÿnsect / ŸnFarm** de Poulainville (Somme), destiné à un possible data center / gigacalculateur. **Arrêté : 5 novembre 2026.**

## Interfaces — modèle partagé

- `apps/cards/` : **vue cartes acteurs**, avec exactement la même grille, filtres, encadrés, modal et typologie de couleurs que les cartographies Escaudain et Dunkerque. Onglets Cartographie / Synthèse / Points de vigilance & sources / Chronologie.
- `apps/network/` : **nuage de points**, reprenant le même modèle graphique (fond quadrillé, simulation physique, nœuds circulaires, liens courbes, filtres latéraux, zoom, glissement, panneau latéral et sources cliquables).
- `index.html` : accueil avec accès aux deux vues.
- `data/` et `config/taxonomy.json` : référentiel JSON commun à toutes les vues.

## Faits vérifiés et prudence d'interprétation

- RTE a annoncé le 31 juillet 2026 une **pré-réservation de 700 MW** pour neuf mois, prorogeable trois mois sous condition. Cela ne correspond **ni à une puissance IT installée, ni à un raccordement physique livré, ni à un contrat final accepté**.
- Le **porteur définitif** de la reconversion n'est pas confirmé par le corpus au 5 novembre 2026.
- **Mistral AI** est cité par *Le Courrier Picard* en mai 2026 comme piste ; **Eclairion** apparaît dans une offre d'emploi localisée à Poulainville. Aucune de ces pièces ne démontre la reprise du site par l'entreprise citée.
- Frédéric Fauvet évoque **100 à 200 emplois en premières tranches** et **300 à 400 à terme** (conseil du 24 septembre, compte rendu du 6 octobre). Ces nombres sont des projections politiques, non des emplois réalisés.
- Les critiques du financement, de la fermeture et des conditions sociales d'**Ÿnsect** ne sont **pas assimilées à une opposition au futur projet de data center**.
- Aucun collectif local d'opposition au projet de data center n'a été identifié dans les sources retenues. C'est une limite de la recherche, **pas une preuve de consensus**.

## Sources principales

- RTE : https://services-rte.org/fr/actualites/validation-par-l-Etat-d-un-nouveau-site-fast-track-a-Poulainville.html
- Amiens Métropole : https://www.amiens.fr/Actualites/Le-point-sur-Y-nsect-et-Tiamat
- Gazette France : https://www.lagazettefrance.fr/article/amiens-nord-une-piste-de-reconversion-de-la-friche-ynsect-tres-electrique
- France 3 Régions : https://france3-regions.franceinfo.fr/hauts-de-france/somme/amiens/reconversion-de-l-ancien-site-d-ynsect-une-activite-a-forte-consommation-d-energie-pourrait-bientot-s-y-installer-3398347.html
- Ici Picardie : https://www.ici.fr/hauts-de-france/somme-80/poulainville/raccordement-electrique-jusqu-a-700-mw-l-ancien-site-ynsect-a-amiens-accueillera-t-il-un-data-center-4421566

Chaque position et relation porte une ou plusieurs preuves reliées à une source URL, avec un champ de traçabilité indiquant si la ressource a été consultée directement ou fournie sous forme d'extrait dans **Poulainville.xlsx**.

## Tester localement

```bash
python3 validate.py
python3 -m http.server 8000
```

Ouvrir `http://localhost:8000/` dans un navigateur. Les fichiers JSON sont chargés par JavaScript via HTTP (et non `file://`).

## Publication GitHub Pages

1. Créer un dépôt public vide `cartographies_poulainville` dans le compte `Zoruohorse` (si non existant).
2. Copier **le contenu** du dossier racine du dépôt, avec `index.html` directement à la racine.
3. Dans Settings → Pages, déployer depuis `main`, dossier `/ (root)`.
4. URL attendue après déploiement : `https://zoruohorse.github.io/cartographies_poulainville/`.

Cette URL est **prévisionnelle** tant que le dépôt et Pages ne sont pas activés. La cartographie est une base documentaire ouverte à de nouvelles sources et à des mises à jour différentielles.
