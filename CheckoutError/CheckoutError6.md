<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Merci donc pour corriger directement sur github, j'ai ca :

[BootdevStaticSiteGenerator](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/tree/main)
/[public](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/tree/main/public)
/
images
/
t
[](https://github.com/Punkyherisson)[Punkyherisson](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/commits?author=Punkyherisson)
[Lost 4 hours, using solution](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/commit/6a28c0b34235296a0f41d490f8df57b68aa7fc30)
[6a28c0b](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/commit/6a28c0b34235296a0f41d490f8df57b68aa7fc30) · 7 months ago
Name
Last commit message
Last commit date
[..](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/tree/main/public)
[rivendell.png](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/blob/main/public/images/rivendell.png)
[Copy Static added](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/commit/561e57f33855fd28d2189c5269c31dc27cb54a01)
7 months ago
[rivendell.png:Zone.Identifier](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/blob/main/public/images/rivendell.png%3AZone.Identifier)
[Lost 4 hours, using solution](https://github.com/Punkyherisson/BootdevStaticSiteGenerator/commit/6a28c0b34235296a0f41d490f8df57b68aa7fc30)
7 months ago
Je supprime uniquement celui avec le Zone.identifier ?

Oui, il faut supprimer **uniquement le fichier `rivendell.png:Zone.Identifier`**, car c’est celui qui est interdit sous Windows et cause toutes les erreurs lors du checkout.

Le fichier `rivendell.png` normal doit être conservé, car c’est l’image valide utilisée par ton projet.

### Étapes sur GitHub pour supprimer ce fichier :

1. Clique sur le fichier `rivendell.png:Zone.Identifier` dans l’interface GitHub.
2. Clique sur l’icône de la poubelle ou sur “Delete” (supprimer).
3. Confirme la suppression dans un commit.
4. Une fois cette opération faite, ton dépôt ne contiendra plus ce fichier problématique.

Après cela, tu devrais pouvoir cloner ou faire un checkout sur ton PC Windows sans problème. Le fichier normal `rivendell.png` restera présent et utilisable sans erreur.

Supprimer ce seul fichier suffit à résoudre l’erreur liée aux noms invalides sous Windows.[^1][^2]

<div align="center">⁂</div>

[^1]: https://stackoverflow.com/questions/69878907/unable-to-fork-personal-github-repository

[^2]: https://github.com/orgs/community/discussions/55138

