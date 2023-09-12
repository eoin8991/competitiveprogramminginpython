'''
Problem Statement:

Retour vers le futur – Regional event 2012
Level 3

Énoncé
Plusieurs années ont passé, et hélas ! vous ne pouvez plus participer à Prologin. Heureusement, 
votre DeLorean vous permet de remonter le temps, et vous avez donc décidé que chaque année, vous 
revivriez les finales Prologin de votre choix. Une question vous taraude nonobstant : quel sera le 
plus grand nombre d'occurrences simultanées de vous-même ?

On vous donne en entrée les intervalles de temps pendant lesquels vous irez faire un tour dans le 
passé, et vous devez retourner le nombre maximum d'exemplaires de vous-même ayant assisté à la même finale.

Entrée
Sur la première ligne, le nombre N d'intervalles de temps.
Sur les N lignes suivantes, une paire d'entiers (Di, Fi) représentant l'intervalle de temps (début, fin) pendant 
lequel vous allez exister une fois de plus dans le passé.

Sortie
Le nombre maximal d'occurrences simultanées de vous-même.

Contraintes
1 <= N <= 1 000 000
0 <= Di <= Fi <= 1 000 000 000
Runtime constraints
Maximum memory usage
10000 kilobytes
Maximum execution time
1000 milliseconds

Input/output samples
Sample input
5
2006 2009
2008 2011
2011 2011
2007 2008
2010 2012

Sample output
3
'''
