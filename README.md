# Togo-Tech-Communities

Ce projet a pour but de mettre à la dispositions des tout le monde, des informations sur les communauté Technologiques du Togo, des infos commes leur site web, les differents liens de leurs comptes sur les reseaux sociaux ainsi que leurs github pour certains.

## la Stack du projet

- Flask (Micro Framework de Python)
- Tailwindcss ( tailwindcss.com )
- Boxicons (  boxicons.com)
- Python 3
- Sqlite3

Si votre communauté n'est pas dans le repo vous avez la possibilité de l'ajouter directement sur le site web vous même via ce lien  `fork`  ou
 via un PR ou faite le moi savoir pour que je l'ajoute.

## Ajout de la communauté par PR

- Les Etapes :

  - Forker ce repo en appuyant sur le bouton `fork`
  - Cloner le repo sur votre machine avec `git clone https://github.com/Likeur/RdcTechCommunities.git`

  - Creer une nouvelle Branche avec `git Branch nom_de_la_branche`
  - Switcher vers la nouvelle branche avec `git checkout votre_branche`
  - Naviguer vers le dossier cloné avec `cd Togo-Tech-Communities`
  - L'ouvrir avec vs code ou votre éditeur de text preféré
  - Naviguer vers le dossier `static/assets/communities`

  - puis ouvrez le fichier `data.json`

    Vous y trouverez une Liste d'objet

  - dans cette liste d'objet ajoutez un nouvel objet comme  ceci :

    `
     , {
    id : +1,
        community : {
                name: 'nom_de_la_communauté',
                linkedin: 'lien',
                whatsapp : 'lien',
                youtube : 'lien',
                github : 'lien',
             siteweb: 'lien'
            }
        },
    `
    (Si vous ne mettez pas de lien  laisser l'endroit vide comme ceci `''`)

    " sur l'id iterez en ajoutant un +1 sur le nombre précedant et ça sera bon " ,

  - Enregistrez le fichier avec `ctrl+s`
  - Sauvegardez vos modifications avec `git add .`
  - Faites un commit avec un message de vos modifications avec `git commit -m "votre_message"`
  - Faites un push vers le repos forker dans votre nouvelle branche avec `git push -u remote_name branch_name`

  - puis rentrez sur  github pour faire un `PR` (pull request) ensuite je vais `merge`  les modifs après verification.

    Et voilà normalement si vous avez suivis toutes les  etapes votre communauté sera sur la liste.

proudly made by ``AGBO Martin``

NB: c'est un OpenSource et ouvert à la contrubition inspirer par le project de RdcTechCommunities `https://github.com/Likeur/RdcTechCommunities.git` made by   ``Likeur off``
