
Date de rendu TP1 : 12/04
Date de rendu TP2 : 08/05 à 17h
Date de rendu TP3 : 22/05 à 17h

Lien vers le cours et les dépôts Arche : http://arche.univ-lorraine.fr/course/view.php?id=11783

---
TD 2 :
- faire build_index
- faire rank_docs (et avoir un score mieux que 0.01, donc supérieur ?)
---

________________________________________________________

EVALUATION DU COURS
________________________________________________________

---
Votre note dans ce cours sera basé uniquement sur votre travail sur les projets lancés au sein des TDs.
---

TD1

Deadline: Avant les vacances d'avril.

Exigences: Avoir un tokéniseur qui prend en compte quelque cas intéressants (e.g. des acronymes, des mots avec des tirets dedans, des numéros avec les points et les points 
virgules dedans). Il y a plusieurs façon d'attaquer ça. Pour donner quelque stratégie valables:
- un tokéniseur détaillé avec des règles spécifiques mais qui reste toujours lisible (astuce: utiliser r"""(?x)...""" en Python)
- un tokéniseur efficace avec un petit nombre des règles sous forme générale
- une procédure écrit toute à la main, qui ne se base pas sur les expressions régulières

TD2

Deadline: vendredi, 8 mai

Exigences: Finir les fonctions build_index et rank_docs (trier les documents selon les scores tf-idf). Implémenter une des extensions proposés en dessous.
- Expérimentez avec les différents mesures de pertinence (e.g., cosine similarity, les variantes sur le diapo intitulé "tf-idf weighting has many variants").
- Utilisez un stop list (fourni dans NLTK) pour filtrer des termes (e.g., au niveau du construction de l'index).
- Utilisez un stemmer, un lemmatiser (tous les deux sont déjà dans NLTK) ou votre propre fonction pour normaliser les termes.
- Branchez votre propre tokéniseur surpuissant du TD1.
- Observez et notez l'effet des différents optimalisations et variantes proposés dessus sur votre score.
- Ajoutez un simple interface (pour le terminal ou même graphique) qui permet au utilisateur de saisir une question et qui lui rend une liste des (titres et IDs des) 10 documents 
les plus pertinents.

TD3

Deadline: vendredi, 22 mai (NB: ça c'est non-négociable parce que je dois rendre vos notes à la fac le lundi 25 mai)

Exigences: Finir les fonctions train_model (calcul des paramètres de HMM) et tag_sentence (algorithme de Viterbi). Pour que ça marche pour de vrai, il faudrait implémenter 
aussi du smoothing, ça veut dire que dans les formules pour calculer des paramètres à partir des fréquences, vous ajoutez une valeur petite (e.g. 1) à chaque fréquence utilisé 
dans le formule pour que aucune probabilité n'est ni 0 et ni x / 0.

---
Modifié le: jeudi 30 avril 2015, 01:48
---

________________________________________________________

ASTUCES
________________________________________________________

***************
***** TD2 *****
***************

--------------------
L'algorithme simple:
--------------------

J'ai mis en place une version simplifiée de modèle pour votre code source dans lequel vous pouvez importez votre code (e.g. build_index). Pour finir la fonction rank_docs, 
il vous suffit juste de finir la fonction score qui doit donner une score de pertinence à un document spécifique vis à vis d'une question posé et l'état de l'index que vous 
avez construit.

Dans votre index, vous pouvez retrouvez la fréquence f(t,d) d'un terme t dans un document d ainsi que le nombre de documents n_t qui contient tous le terme t. La première 
valeur vous indique la pertinence d'un document pour un terme et la deuxième vous donne l'importance du terme (des termes qui apparaissent dans peu de document sont plus 
utiles que ceux qui apparaissent partout). À partir de ces deux valeurs, vous pouvez calculer le score du pertinence d'un terme pour un document.

Un bon schéma pour le calculer s'appelle tf-idf. Vous pouvez trouver des informations sur comment le calculer dans les diapos ou autre part (les variantes simples et efficaces 
sont, e.g., des variantes logarithmiques (1 + log f(t,d) pour la fréquence des termes et log (N / n_t) pour la fréquence des documents (vous pouvez retrouver le nombre de 
documents N en prenant la taille de collection docs))). Pour retrouver le score de pertinence d'un document vis à vis d'une question, faites juste la somme de tous les score 
tf-idf pour chaque terme dans la question.

Il existe un algorithme plus efficace qui profite de la structure d'index qu'on a crée et donc une fois que vous avez compris le but de la tâche en essayant de mettre en place 
l'algorithme en dessus, il vaudra mieux essayer aussi celui en dessous.

NB: Vous saurez que vous avez probablement réussi quand votre score (le "mean average precision") a visiblement remonté. Pour donner une référence, après avoir mis en place 
l'algorithme en dessous (qui calcule la même chose, i.e. le tf-idf, que celui en dessus), j'ai eu un score de 0,19 et après avoir branché l'un de vos tokeniseur en place de 
la fonction split, j'ai eu 0,2.

----------------------
L'algorithme efficace:
----------------------

Cet algorithme est basé sur deux idées qu'on va voir apparaître dans le deux fonctions, build_index et rank_docs, respectivement.

Pour la première idée, on va remarquer qu'au final, on se sert des fréquences stockés dans l'index juste pour calculer les score tf-idf et on les calcule chaque fois qu'on 
utilise rank_docs de même façon. En place de stocker la fréquence f(t,d) d'un terme t dans un document d, on peut stocker directement le score tf-idf du document vis à vis 
du terme. Donc, après avoir construit l'index ou on a pour chaque terme un postings list des (docID, fréquence), on va traverser tout l'index et remplacer les fréquences par 
les scores tf-idf qu'on calcule avec la même formule comme avant, en se basant sur la fréquence du terme dans le document et le nombre des documents dans lesquels le terme 
apparaisse (i.e. la taille du postings list). En faisant ça dans build_index, on peut rendre la fonction rank_docs plus simple et plus efficace.

La deuxième idée nous donnera l'algorithme de rank_docs. On sait que tous les documents dans lesquels n'apparais aucun terme de la question ne sont pas pertinents et que leur 
score sera 0. Donc, tous les documents qui nous intéressent contient au moins un terme de la question et dans ce cas, leur docID apparais dans le postings list de ce terme. 
Pour retrouver tous les documents avec une pertinence > 0, il nous suffit de juste faire l'union de tous les postings lists appartenant aux termes de la question. On peut faire 
ça assez facilement en apportant quelques petites adaptations au algorithme de l'intersection des postings lists qu'on a vu en classe (il se trouve aussi dans les diapos). En 
plus, quand on est en train de calculer l'union des deux postings lists, pour chaque docID qui apparais dans tous les deux postings lists, on va mettre la somme des deux scores 
que le document avait dans les deux listes en tant que le nouvel score dans le nouvel liste. Comme ça, on finit avec une liste ou on a non seulement tous les pertinents docIDs, 
mais on a déjà le score de pertinence tf-idf pour chaqu'un d'eux. Maintenant, il suffit juste de trier cette collection selon les scores (les deuxièmes éléments dans les pairs) 
en ordre descendant et après extraire la séquence des docIDs (les premières éléments dans les pairs) dans cette collection triée.

NB: Comme ça, la séquence des docIDs qu'on va produire ne va pas contenir tous les docIDs dans notre collection des documents. Avec l'ancienne version du code d'évaluation, 
celui-là produira une erreur et il faudrait ajouter des docIDs manquant au fin de liste produit. Pour cette raison, j'ai modifié le code d'évaluation et j'ai mis à jour le 
ficher modèle de code source pour que vous pouvez mettre en place l'algorithme décrit en dessus sans se souciant de fait que les listes des documents ordonnés par la pertinence 
que vous produisez ne contiennent pas tous les docIDs.

***************
***** TD3 *****
***************

Fonctions conseillées à utiliser:
- pour train_model: frequencies (de TD2), nltk.bigrams

---
Modifié le: jeudi 30 avril 2015, 01:41
---
