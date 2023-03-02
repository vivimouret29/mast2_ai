1. Qu'est-ce que la validation croisée (cross-validation) ? Pourquoi est-elle importante dans la 
modélisation des données ?
2. Comment traitez-vous les valeurs manquantes dans un ensemble de données ? Quelles sont les 
techniques que vous utilisez et pourquoi ?
3. Pouvez-vous expliquer la différence entre la régression linéaire et la régression logistique ? 
Dans quels cas utiliseriez-vous l'une ou l'autre méthode ?
4. Comment choisissez-vous les variables à inclure dans votre modèle ? Quelles sont les techniques 
que vous utilisez pour sélectionner les variables les plus importantes ? 
5. Pouvez-vous expliquer l'algorithme de clustering k-means? Comment l'utiliseriez-vous pour regrouper 
des données en groupes homogènes ?
6. Pouvez-vous décrire une technique que vous avez utilisée pour réduire la dimensionnalité de données 
complexes ? Pourquoi avez-vous choisi cette technique ? 
7. Comment traitez-vous les données déséquilibrées (imbalanced data) ? Pouvez-vous expliquer les méthodes 
que vous utilisez pour résoudre ce problème ?
8. Comment mesurez-vous les performances de votre modèle ? Quelles sont les mesures que vous utilisez 
pour évaluer la qualité de votre modèle ?
9.  Pouvez-vous expliquer la différence entre l'apprentissage supervisé et l'apprentissage non supervisé ? 
Dans quels cas utiliseriez-vous l'une ou l'autre méthode ?
10. Comment traitez-vous les données aberrantes (outliers) dans un ensemble de données ? 
Quelles sont les techniques que vous utilisez pour identifier et traiter les outliers ?


**[QCM] Cloud AI:**
1. La cross-validation est une technique qui permet de tester la robustesse d'un modèle en l'entraînant 
sur un sous-ensemble de données et en le testant sur un autre sous-ensemble de données. Cela permet de 
vérifier que le modèle est capable de généraliser sur des données qu'il n'a pas vues lors de l'entraînement.
2.  Il existe plusieurs techniques pour traiter les valeurs manquantes, notamment la suppression des lignes ou 
des colonnes contenant des valeurs manquantes, l'imputation des valeurs manquantes par des moyennes ou des médianes, 
l'imputation des valeurs manquantes par des valeurs prédites à l'aide d'un modèle, etc. Le choix de la technique dépend 
des caractéristiques des données et de l'objectif de l'analyse.
3. La régression linaire sert à prédire une valeur continue tandis que la régression logistique sert à prédire 
une valeur catégorielle. On utilise la régression linéaire dans le cas où l'on prédit le prix d'un maison, et la régression 
logistique dans le cas où l'on prédit si une personne a un cancer ou non.
4. Le choix des variables à inclure dans le modèle dépend de l'objectif de l'analyse et de l'ensemble de données. 
Les techniques de sélection de variables incluent l'analyse de corrélation, la régression linéaire multiple, 
la régression logistique, l'analyse de variance,...
5. Un algorithme de clustering k-means permet de regrouper des données en groupes homogènes. Il va nous 
permettre de trouver des clusters dans un ensemble de donnéespour ainsi déterminer des groupes de données 
qui sont similaires entre elles. Pour l'utiliser, il faut vectoriser les données et ensuite appliquer 
l'algorithme de clustering k-means tout en lui donnant le nombre de clusters que l'on souhaite.
6. Le choix de la technique dépend de l'objectif de l'analyse et des caractéristiques des données. 
Par exemple, si l'objectif est de réduire le nombre de variables tout en conservant autant d'informations 
que possible, PCA peut être utilisé.  Si l'objectif est de maximiser la séparation entre les classes, 
LDA peut être utilisé. Si les données ont des propriétés spécifiques, telles que la sparsité ou la 
non-négativité, des techniques spécifiques telles que NMF peuvent être utilisées. Le choix de la technique 
dépend donc des caractéristiques spécifiques des données et de l'objectif de l'analyse. 
7. La technique de suréchantillonnage consiste à créer des copies des données minoritaires 
pour augmenter leur nombre. La technique de sous-échantillonnage consiste à supprimer des données majoritaires 
pour réduire leur nombre.
8. Les métriques de performance dépendent du type de problème et des objectifs de l'analyse. 
Pour les problèmes de classification, des métriques telles que la précision, le rappel, la F-mesure et la 
courbe ROC sont souvent utilisées. Pour les problèmes de régression, des métriques telles que le coefficient 
de détermination (R²), l'erreur quadratique moyenne (MSE) et l'erreur absolue moyenne (MAE) peuvent être utilisées.
9. L'apprentissage surpervisé est utilisé lors de la prédiction d'une variable cible. L'apprentissage non supervisé 
est utilisé lorsqu'on n'a pas de variable cible ou lorsqu'on cherche à regrouper des données en groupes homogènes.
L'AS est utilisé pour la classification et la régression et l'ANS pour le clustering.
10. Les données abérantes sont des observations qui diffèrent considérablement des autres observations dans un ensemble 
de données. On peut les traiter en les supprimant ou en les remplaçant par des valeurs plus proches des autres données.