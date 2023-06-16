# Reparation-par-SVD
L’objectif de ce projet est de restaurer une image abîmée en utilisant l’approximation de rang faible basée sur la décomposition en valeurs singulières (SVD). Nous quantifions la qualité de l’approximation en évaluant l’erreur quadratique et l’erreur selon la norme de Frobenius.

1. Charger l’image en noir et blanc et le masque à l’aide de la fonction imread de matplotlib.
2. Convertir le masque en un masque binaire.
3. Appliquer la décomposition en valeurs singulières sur l’image en noir et blanc.
4. Tronquer les matrices U, s et Vt pour obtenir une approximation de rang faible de l’image.
5. Reconstruire l’image approximée à partir des matrices tronquées.
6. Restaurer l’image en utilisant l’image approximée pour les pixels endommagés.
7. Calculer l’erreur quadratique et l’erreur selon la norme de Frobenius entre l’image originale
et l’image restaurée.
8. Afficher les images avant et après restauration.
   
Nous avons utilisé une image en noir et blanc de cheval avec une ligne endommagée. Le
masque de la ligne endommagée a également été fourni. En appliquant l’approximation de rang
faible basée sur la décomposition en valeurs singulières, nous avons pu restaurer l’image.
Nous avons ajusté le rang de l’approximation pour obtenir des résultats différents et avons
calculé l’erreur quadratique et l’erreur selon la norme de Frobenius pour évaluer la qualité de
l’approximation. Les images restaurées montrent que la ligne endommagée a été éliminée avec
succès.

# Conclusion
La décomposition en valeurs singulières et l’approximation de rang faible se sont révélées
être une méthode efficace pour restaurer une image abîmée. En utilisant l’approximation de
rang faible de l’image, nous avons pu restaurer l’image en noir et blanc en éliminant la ligne
endommagée. L’évaluation de l’erreur quadratique et l’erreur selon la norme de Frobenius a
permis de quantifier la qualité de l’approximation.

