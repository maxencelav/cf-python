# Exercice 1

L'encodage Base 64 : Utilisé notamment pour encoder le URLs

Egalement utilisé pour joindre des fichiers aux emails.

Encodage standard de l'information est le code ASCII (7 ou bits)

Le code Base 64 n'utilise que 64 caractères alors que l'ASCII utilise une table
de 128 caractères (ASCII 7 Bits) ou 256 caractères (ASCII 8 bits)

Etapes détaillées :

Chaque étape fera l'objet de la création d'une fonction (Documentée et commentée).

On part d'une chaine de caractères (par exemple) : 'ABCDE'

1) Transformer la chaine de caractères en liste

['A','B','C','D','E']

2) Transformer chaque élément de la liste dans son code ASCII

[65,66,67,68,69]

3) Transformer chaque élément de la liste dans sa représentation binaire

['1000001','1000010','1000011','1000100','1000101']

4) Cadrer tous les éléments de la liste à droite sur 8 positions (ajouter les
zéros à gauche)

['01000001','01000010','01000011','01000100','01000101']

5) Créer une chaine de caractère à partir de la liste

'0100000101000010010000110100010001000101'

6) Découper la chaine en blocs de 6 caractères et en faire une nouvelle liste

['010000','010100','001001','000011','010001','000100','0101']

7) Cadrer le dernier bloc sur 6 caractères (ajouter des zéros à droite)

['010000','010100','001001','000011','010001','000100','010100']

8) Transormer chaque élément en représentation décimale

[16,20,9,3,17,4,20]

9) Transformer chaque élément dans son caractère dans la table Base 64

['Q','U','J','D','R','E','U']

10 ) Transformer la liste en chaine de caractères

'QUJDREU'

11) La chaine de caractères doit avoir un longeur multiple de 4. Ajouter
éventuellemnt des signes '=' à droite pour obtenir une longeur multiple
de 4

'QUJDREU='

Exercice: Ecrire le script avec chaque étape dans une fonction.

Demander à l'utilisateur du script d'entrer une chaine quelconque et
afficher le résultat de l'encodage.

Interdiction d'utiliser: 'import base64'

Ecrire la partie script permettant de décoder le Base 64 vers l'ASCII
En réutilisant une partie des fonctions déjà implémentées.