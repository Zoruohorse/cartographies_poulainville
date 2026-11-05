# Poulainville — Rapport de création de la cartographie initiale

**Date d’arrêté : 5 novembre 2026**  
**Base documentaire : six ressources de `Poulainville.xlsx` et vérifications complémentaires.**  
**Politique de preuve :** citation URL par preuve ; toute relation conservée a au moins un rattachement à une preuve ; les citations secondaires et les extraits de presse ne sont pas présentés comme des actes officiels.

## 1. Le projet

L’ancienne usine Ÿnsect/ŸnFarm de Poulainville a cessé son activité après la liquidation judiciaire du 1er décembre 2025. En janvier 2026, la reconversion en data center n’était qu’une hypothèse parmi plusieurs options. Le 31 juillet 2026, l’État a demandé à RTE de pré-réserver 700 MW sur le site, selon une procédure Fast Track validée par la CRE. En août 2026, la préfecture et les partenaires publics ont présenté la friche comme un foncier stratégique en préparation d’une activité électro-intensive. Le 6 octobre 2026, Amiens Métropole évoque un projet de gigacalculateur, sans publication dans les ressources sélectionnées d’un nom d’exploitant final confirmé.

**RTE :** https://services-rte.org/fr/actualites/validation-par-l-Etat-d-un-nouveau-site-fast-track-a-Poulainville.html

**Amiens Métropole :** https://www.amiens.fr/Actualites/Le-point-sur-Y-nsect-et-Tiamat

## 2. Acteurs et prises de position

| Acteur | Position sur la reconversion | Qualification |
|---|---|---|
| Préfecture de la Somme / Rollon Mouchel-Blaisot | Soutien à la reconversion industrielle | Citation préfectorale rapportée par La Gazette France, 7 août 2026 |
| Amiens Métropole / Frédéric Fauvet | Soutien à la perspective de gigacalculateur | Déclarations lors du conseil du 24 septembre, publiées le 6 octobre 2026 |
| Léon Deffontaines | Favorable, avec exigence de souveraineté technologique | Interview ici Picardie, 7 août 2026 |
| Rémi Cardon | Prudent ; aurait préféré une industrie plus structurante | Interview ici Picardie, 7 août 2026 |
| Hadrien Godard | Adaptation technique jugée plausible ; alerte environnementale et sociale | France 3 et Courrier Picard ; ne constitue pas opposition formelle |
| Jean-Pierre Pardoux | Maire de Poulainville ; **position sur le data center non établie** | Amiens Métropole, mai 2026 |
| Banque des Territoires | Accompagnement de la sécurisation du foncier | Action agricole Picarde, 7 août 2026 |
| RTE | Pré-réservation technique de 700 MW, pas soutien industriel à un porteur | Source primaire, 31 juillet 2026 |
| Mistral AI | Aucun soutien ou contrat démontré | Hypothèse journalistique mai 2026 uniquement |
| Eclairion | Aucun contrat local démontré | Signal de recrutement à Poulainville sans mention d’Ÿnsect |

## 3. Points de vigilance et signaux faibles

- **Capacité :** ne pas présenter 700 MW de pré-réservation comme une puissance informatique souscrite ou livrée. Neuf mois à compter du 31 juillet 2026 et prorogation conditionnelle de trois mois.
- **Porteur :** hypothèse Mistral AI (Courrier Picard mai 2026) à confirmer ; offre Eclairion (localisation Poulainville) signal faible d’emploi, **pas** preuve de contrat.
- **Fonciers et financeurs :** SCI Vertycal et sa participation attribuée à la Caisse des Dépôts ont été rapportées par la presse à partir de témoignages, sans documentation patrimoniale primaire.
- **Emplois :** 100–200 en premières tranches, 300–400 à terme sont des projections énoncées par Frédéric Fauvet, sans preuve d’embauches réalisées.
- **Anciens salariés :** le Gouvernement rapporte au 15 septembre 2026 l’avancement du reclassement des salariés d’Ÿnsect et la poursuite de la procédure sociale ; ces sujets ne sont pas assimilés à une opposition au futur data center.
- **Environnement :** inquiétudes hydriques et électriques formulées par Hadrien Godard ; ni étude hydrique propre au futur opérateur ni permis de data center établi dans le corpus.
- **Oppositions :** aucune organisation citoyenne nommément opposée au nouveau projet n’a pu être attribuée sur preuve dans cette recherche ; l’absence d’acteurs identifiés ne préjuge pas des positions futures.

## 4. Méthode, données et qualité

Les fichiers `actors.json`, `claims.json`, `evidence.json`, `sources.json`, `relations.json`, `synthesis.json`, `content.json`, `meta.json` et `taxonomy.json` sont communs aux cartes et au réseau. Les identifiants `project_poulainville`, `actor_0001...`, `claim_0001...` etc. sont stables et servent aux futures mises à jour différentielles.

L'interface graphique reprend les dimensions, couleurs et interactions du modèle de référence Escaudain/Dunkerque : cartes avec filtres et fenêtre modale, trois onglets de synthèse, un quatrième pour la chronologie, ainsi qu’un nuage SVG à liens courbes et simulation physique.

Validation par `python3 validate.py` : cardinalités, unicité des identifiants, références croisées, taxonomie, présence de sources URLs, justification des positions et relations. Tests navigateur : ouverture des vues et interactions basiques sous Chromium local.

## 5. Réserves techniques et éditoriales

La qualification `direct` indique une page consultée en ligne dans le cadre de cette analyse ; `xlsx_excerpt` un contenu déjà fourni dans le classeur. Les textes de presse réservés aux abonnés ne sont pas recopiés intégralement dans le dépôt.

Les attestations officielles retenues ne démontrent ni contrats finaux, ni travaux réels de raccordement, ni bilan d’emplois à ce jour. L’archive est prête pour GitHub Pages ; sa publication est conditionnée à l’existence d’un nouveau dépôt accessible à l’outil de connexion GitHub.
