# pam_corpus - Modification du corpus de la BFM pour le PAM.

Ce répertoire contient les scripts nécessaires pour créer le corpus du pam
à partir des fichiers xml de la BFM.

## Pré-requis

Installer __python3__ en suivant la documentation officielle sur:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Installer le gestionnaire de package python3 `pip3` de la manière la plus
adéquate selon votre OS.

Installer les dépendances suivantes avec ces packages:

```
sudo pip3 install lxml
sudo pip3 install beautifulsoup4
sudo pip3 install num2words
```

## Ou trouver les xml des textes de la BFM?

Demander les fichiers xml directement à la BFM en les contactant à cette
adresse : bfm@ens-lyon.fr

## Transformation de xml vers txt

Pour extraire le texte des vers des fichiers xml,
il faut lancer le script exécutable `xml_txt.py`.

### Exemple
```console
$> python3 xml_txt.py corpus/bestam100.xml
corpus/bestam100.txt is created.
```
## Nettoyage des chiffres romains dans les fichiers txt

Pour nettoyer les chiffres romains des fichiers txt il suffit d’exécuter le
le script `clear_numbers.py` avec les fichiers en argument.

Après le nettoyage manuel des `.I.` un fichier propre est sauvé dans le
dossier `clear_txt`  

### Exemple
```
$> python3 clear_numbers.py corpus/bestam100.txt
bestam100.txt
corpus/bestam100.txt line: 6
 Me semont d'emprendre .I. afaire.
Choose 1:un or 2:une
2
corpus/bestam100.txt line: 98
 Quar quant l'en voit painte .I. estoire
Choose 1:un or 2:une
1
corpus/bestam100.txt line: 103
 Car quant l'en ot .I. rommant lire
Choose 1:un or 2:une
1
clear_txt/bestam100.txt have been created.
```
