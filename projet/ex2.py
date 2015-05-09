#!/usr/bin/env python
 
### POUR EXECUTER LE FICHIER DANS NOTEPAD++ : 	        C:\Python34\python.exe ex2.py
### POUR EXECUTER EN LIGNES DE COMMANDES : 		python ex2.py
 
import re
import operator

# Ajout
from ex1 import tokenize
 
# Le chemin vers le dossier contenant les fichiers de la Cranfield collection.
#data_path = "./cran"
data_path = "./ex2"
 
def read_docs():
    with open(data_path + "/cran.all.1400") as f:
        docs = re.findall(r"^\.I ([0-9]+)\n((?:.(?!\n\.I [0-9]+\n))*.)",\
                          f.read(), flags = re.M | re.S)
        id_body_pairs = map(lambda p: (int(p[0]), re.sub(r"^\.[TABW]\n", "\n",\
                                                         p[1],\
                                                         flags = re.M | re.S)),\
                            docs)
        return dict(id_body_pairs)
 
# Un dictionnaire qui donne pour un docID son contenu.
docs = read_docs()
 
def read_queries():
    with open(data_path + "/cran.qry") as f:
        queries = re.findall(r"^\.I [0-9]+\n.W\n((?:.(?!\n\.I [0-9]+\n))*.)",\
                             f.read(), flags = re.M | re.S)
        id_query_pairs = enumerate(queries, start = 1)
        return dict(id_query_pairs)
 
# Un dictionnaire qui relie les queryIDs et leurs contenus.
queries = read_queries()
 
def read_relevance():
    with open(data_path + "/cranqrel") as f:
        qd_pairs = map(lambda l: (int(l.split()[0]), int(l.split()[1])),\
                       f.readlines())
        return set(qd_pairs)
 
# Un ensemble des pairs (q,d) ou q est le queryID d'une question pour
# laquelle d est un docID d'un document qui lui est pertinent.
relevance = read_relevance()

# FONCTION 1
# frequencies(["ab","bc","ab"]) --> { "ab" : 2, "bc" : 1 }
def frequencies(toks):
    freqs = {}
    for tok in toks:
        if tok in freqs:
            freqs[tok] += 1
        else:
            freqs[tok] = 1
    #for tok in freqs:
    #        freqs[tok] = (1,freqs[tok])
    return freqs

# FONCTION 2
# build_index(docs) --> { "slipstream": [(1,6), (16,3), ...], "configuration": [(1,1), ...], ... }
def build_index(docs):
    """VOTRE CODE ICI

       A partir de la collection des documents, construisez une structure
       des donnees qui vous permettra d'identifier des documents pertinents
       pour une question (e.g., l'index inversee qu'on a vu en classe).
    """
    index = {}

    for docID in docs:
        freqs = frequencies(tokenize(docs[docID]))
        for tok in freqs: ###
            if tok in index.keys():
                index[tok].append((docID, freqs[tok]));
            else:
            	index[tok] = []
            
        print(freqs) ###
        # ID DU DOCUMENT ACTUEL
        print(docID) ###
        # POUR EVITER DE BLOQUER LE PROCESSUS, METTRE UNE VALEUR FAIBLE (EXEMPLE : 'if docID > 10:')
        if docID > 4: ###
            break ###
    # ...
    print(index)
  
    return index
 
# FONCTION 3
# rank_docs(...) --> {367,45,1352,27,1149,897,12,1400} or [367,45,1352,27,1149,897,12,1400] ??
# Add comment sign at the beginning of the line where there is "DEBUG PRINTING" comment to avoid useless printing
def rank_docs(index, query):
    rank = {}
	
    """VOTRE CODE ICI

       Retournez la serie des docIDs ordonnes par leur pertinence vis-a-vis
       la question 'query'.
    """
	
    for i in range(1, 1401):
        rank[i] = 0

    for mot in tokenize(query):
        
        if mot in index.keys():
            for item in index[mot]:
                rank[item[0]] = item[1]

    print("Beginning of Rank")      ### DEBUG PRINTING
    print(rank)
    print("End of Rank")            ### DEBUG PRINTING
    sort = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
    print("Beginning of Sort")      ### DEBUG PRINTING
    print(sort)
    print("End of Sorted")          ### DEBUG PRINTING
    dico = dict(sort)
    print("Beginning of Dico")      ### DEBUG PRINTING
    print(dico)
    print("End of Dico")            ### DEBUG PRINTING
    liste = list(dico.keys())
    print("Beginning of Liste")     ### DEBUG PRINTING
    print(liste)
    print("End of Liste")           ### DEBUG PRINTING
    print(type(liste))
    
    return liste
 
def average_precision(qid, ranking):
    print("QUERY ID (qid) : " + str(qid))           ### DEBUG PRINTING
    relevant = 0
    total = 0
    precisions = []
    
    for did in ranking:
        print("DOCUMENT ID (did) : " + str(did))    ### DEBUG PRINTING
        total += 1
        if (qid, did) in relevance:
            relevant += 1
            precisions.append(relevant / total)
 
    return sum(precisions) / len(precisions)

def mean_average_precision():
    index = build_index(docs)
 
    aps = []
    for qid in queries:
        ranking = rank_docs(index, queries[qid])
        assert len(set(ranking)) == len(ranking), "Duplicates in document ranking."
        assert len(ranking) == len(docs), "Not enough (or too many) documents in ranking."
        aps.append(average_precision(qid, ranking))
        break
    return sum(aps) / len(aps)
 
# Imprime le MAP de l'approche implemente
print("Mean average precision: " + str(mean_average_precision()))

# SCORE INITIAL :   Mean average precision: 0.011772548860990937
# SCORE ACTUEL :    Mean average precision: 0.12316653495319264

