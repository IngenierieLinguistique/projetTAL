
Date de rendu TP1 : 12/04
Date de rendu TP2 : 10/05
Date de rendu TP3 : 24/05

Lien vers les dépôts Arche : 

---
TD 2 :
- faire build_index
- faire rank_docs (et avoir un score mieux que 0.01)
---

________________________________________________________

EVALUATION DU COURS
________________________________________________________

---
Votre note dans ce cours sera basé uniquement sur votre travail sur les projets lancés au sein des TDs.
---

TD1

Deadline: Avant les vacances d'avril.

Exigences: Avoir un tokéniseur qui prend en compte quelque cas intéressants (e.g. des acronymes, des mots avec des tirets dedans, des numéros avec les points et les points virgules dedans). Il y a plusieurs façon d'attaquer ça. Pour donner quelque stratégie valables:
- un tokéniseur détaillé avec des règles spécifiques mais qui reste toujours lisible (astuce: utiliser r"""(?x)...""" en Python)
- un tokéniseur efficace avec un petit nombre des règles sous forme générale
- une procédure écrit toute à la main, qui ne se base pas sur les expressions régulières

TD2

Deadline: Deux semaines après le fin des vacances d'avril (vous pouvez travailler jusqu'à la deadline de TD3 sur les extensions).

Exigences: Finir les fonctions build_index et rank_docs (trier les documents selon les scores tf-idf). Implémenter une des extensions proposés en dessous.
- Expérimentez avec les différents mesures de pertinence (e.g., cosine similarity, les variantes sur le diapo intitulé "tf-idf weighting has many variants").
- Utilisez un stop list (fourni dans NLTK) pour filtrer des termes (e.g., au niveau du construction de l'index).
- Utilisez un stemmer, un lemmatiser (tous les deux sont déjà dans NLTK) ou votre propre fonction pour normaliser les termes.
- Branchez votre propre tokéniseur surpuissant du TD1.
- Observez et notez l'effet des différents optimalisations et variantes proposés dessus sur votre score.
- Ajoutez un simple interface (pour le terminal ou même graphique) qui permet au utilisateur de saisir une question et qui lui rend une liste des (titres et IDs des) 10 documents les plus pertinents.

TD3

Deadline: Quatre semaines après le fin des vacances d'avril.

Exigences: Finir les fonctions train_model (calcul des paramètres de HMM) et tag_sentence (algorithme de Viterbi). Pour que ça marche pour de vrai, il faudrait implémenter aussi du smoothing, ça veut dire que dans les formules pour calculer des paramètres à partir des fréquences, vous ajoutez une valeur petite (e.g. 1) à chaque fréquence utilisé dans le formule pour que aucune probabilité n'est ni 0 et ni x / 0.

---
Modifié le: mercredi 8 avril 2015, 11:43
---

________________________________________________________

ASTUCES
________________________________________________________

TD3

Fonctions conseillées à utiliser:
- pour train_model: frequencies (de TD2), nltk.bigrams

---
Modifié le: mercredi 8 avril 2015, 09:35
---
