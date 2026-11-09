# Cartographie des acteurs — Poulainville

Référentiel documenté du projet de reconversion de l'ancienne usine **Ÿnsect / ŸnFarm** de Poulainville (Somme), destiné à un possible data center / gigacalculateur. **Arrêté initial : 5 novembre 2026. Actualisation : 9 novembre 2026.**

## Interfaces — modèle partagé

- `apps/cards/` : **vue cartes acteurs**, avec exactement la même grille, filtres, encadrés, modal et typologie de couleurs que les cartographies Escaudain et Dunkerque. Cinq onglets : Cartographie / Synthèse / Points de vigilance & sources / Chronologie / Évolution des acteurs.
- `apps/network/` : **nuage de points**, reprenant le même modèle graphique (fond quadrillé, simulation physique, nœuds circulaires, liens courbes, filtres latéraux, zoom, glissement, panneau latéral et sources cliquables).
- `index.html` : accueil avec accès aux deux vues.
- `data/` et `config/taxonomy.json` : référentiel JSON commun à toutes les vues.

## Faits vérifiés et prudence d'interprétation

- RTE a annoncé le 31 juillet 2026 une **pré-réservation de 700 MW** pour neuf mois, prorogeable trois mois sous condition. Cela ne correspond **ni à une puissance IT installée, ni à un raccordement physique livré, ni à un contrat final accepté**.
- Le **porteur définitif** de la reconversion n'est pas confirmé par le corpus au 5 novembre 2026.
- **Mistral AI** est cité par *Le Courrier Picard* en mai 2026 comme piste ; **Eclairion** apparaît dans une offre d'emploi localisée à Poulainville. Aucune de ces pièces ne démontre la reprise du site par l'entreprise citée.
- Frédéric Fauvet évoque **100 à 200 emplois en premières tranches** et **300 à 400 à terme** (conseil du 24 septembre, compte rendu du 6 octobre). Ces nombres sont des projections politiques, non des emplois réalisés.
- Les critiques du financement, de la fermeture et des conditions sociales d'**Ÿnsect** ne sont **pas assimilées à une opposition au futur projet de data center**.
- Un groupe politique régional, **Les Écologistes Hauts-de-France**, a publié le 6 novembre 2026 une critique des méga-data centers en citant Poulainville et en soutenant un moratoire. Aucun collectif ou recours **spécifiquement local à Poulainville** n'est néanmoins documenté. C'est une limite de la recherche, **pas une preuve de consensus**.

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

Le dépôt GitHub est opérationnel : les mises à jour du 9 novembre 2026 ont été poussées sur la branche `main`. La cartographie est une base documentaire ouverte à de nouvelles sources et à des mises à jour différentielles.


## Onglet Évolution des acteurs (9 novembre 2026)

Le modèle Montereau/Escaudain propose **Nouveaux**, **Cumulés** et **Par position**, la dernière variante distinguant favorables, opposés, prudents et positions non établies. Deux périmètres empêchent les confusions : **Projet Poulainville** (acteurs directement liés au dossier) et **Avec contexte régional** (acteurs de l'ancienne Ÿnsect, du cadre national ou des débats sur les data centers).

**26 acteurs disposent d'une fiche affichée ; 25 d'entre eux peuvent être placés dans le temps ; Eclairion reste sans date et sans contractualisation démontrée.** Parmi les acteurs datés, 15 sont associés directement à la reconversion, 10 au contexte général. Le groupe Les Écologistes Hauts-de-France apparaît en **opposition au modèle régional** dans le périmètre élargi, pas comme collectif de riverains de Poulainville.

La synthèse compte neuf thèmes, dont une fiche sur l'opposition régionale du 6 novembre 2026, avec preuves déroulables. La chronologie compte dix jalons et sept repères techniques. Les anciennes positions et relations ont été conservées : seuls l'acteur régional, sa position et une relation « mention contextuelle » sont ajoutés.

**Attention :** la pré-réservation de **700 MW** par RTE (31 juillet 2026) ne garantit ni opérateur sélectionné, ni contrat de raccordement accepté, ni puissance informatique livrée. Source officielle : [RTE](https://services-rte.org/fr/actualites/validation-par-l-Etat-d-un-nouveau-site-fast-track-a-Poulainville.html). Opposition régionale : [Écologistes HDF, 6 novembre](https://lesecologisteshdf.fr/2026/11/06/mobilisation-contre-les-datacenters-du-week-end-du-7-8-novembre/).

Données : `data/timeline.json`, `data/evolution-audit-20261109.json`. Le graphique Par position exprime **la classification des fiches à la date de la veille**, non la chronologie de changements de position.
