# Big-Data-Projet
### Moulin David - Gaildry Arthur - Bertrand Sébastien

Nous disposons de données bancaires divisées en trois parties : 

* train qui contient **1997419** opérations non frauduleuses et de **2581** opérations frauduleuses

* test qui contient **4003** opérations non frauduleuses et de **3997** opérations frauduleuses

* predict qui contient **2000** opérations dont on ne connait pas "l'état"

On souhaite créer un modèle d'apprentissage capable d'identifier des opérations frauduleuses.

Pour cela nous allons utiliser des algorithmes d'apprentissage supervisés.


Le Dossier Data-Analysis contient les notebooks des 4 méthodes utilisées : 

* Arbre de décision 
* SVM
* Réseaux de neurones
* K-neighbors

Le dossier PushToS3 contient le script qui permet de mettre les fichiers csv sur un bucket d'AWS.

Le code_export permet de transferer les fichiers de la vm hadoop depuis hdfs sur notre machine physique à l'aide de connection et de transfert ssh scp, ce qui nous permet de récuperer integralement les fichiers test,train et predict .csv en définissant au préalable le port et l'ip concerné, cela à été vérifié à l'aide de putty.
