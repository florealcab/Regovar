Logs et gestion des erreurs
===========================

Codes d'erreur et documentation
-------------------------------
Les erreurs gérées par Regovar sont identifiées et documentées afin de permettre un support efficace autant pour les développeurs qui tomberaient dessus pour la première fois que pour les utilisateurs finaux qui pourront alors se référer à la documentation en ligne concernant l'erreur.

Le code erreur est un identifiant à 7 caractères qui suit la nomenclature suivante :

| `E` | `0` | `00` | `000` |
| --- | --- | ---- | ----- |
|| Code module| code sous-module |Code de l'erreur|


**Liste des Modules**

| Code module | Description |
|------|-------------|
|`0`| "Setup". Erreur concernant l'installation ou la configuration du server|
|`1`| Erreur concernant la base de données ou le model. Le code concernant ces erreurs se trouvera dans le module Python : `regovar/core/model` |
|`2`| Erreur concernant le coeur de l'application. Le code concernant ces erreurs se trouvera dans le module Python : `regovar/core/core` |
|`3`| Erreur concernant l'api rest. Le code concernant ces erreurs se trouvera dans le module Python : `regovar/web` |
|`4`| Erreur concernant l'api cli. Le code concernant ces erreurs se trouvera dans le module Python : `regovar/cli` |


**Liste des Sous-modules**

| Code module | Code sous-Module | Description |
|-------------|------------------|-------------|
|`0`| `-` | *pas de sous niveau* |
|`1`| `00` | UserModel |
|`1`| `01` | ProjectModel |
|`1`| `02` | EventModel |
|`1`| `03` | ... |
|`2`| `00` | UserManager |
|`2`| `01` | ProjectManager |
|`2`| `03` | ... |
|`3`| `00` | UserHandler |
|`3`| `01` | ProjectHandler |
|`3`| `03` | ... |


**Exemple** 
 * `E201001` : 


Log
===
Comme tout serveur qui se respecte, Regovar log tout se qu'il fait. L'endroit où sont écrits les logs est configurable dans le fichier de conf.

**3 niveau de log prévu :**

| Niveau de log | Description |
|------|-------------|
|info| Pour du debug ou pour horodater des événements utiles à l'analyse des logs|
|warning| Quand une erreur non critique survient, c'est-à-dire n'engendrant pas de corruption ou de perte de données. En général, les erreurs gérées (ayant un code d'erreur) sont non critiques. En cas de doute, utiliser error.
|error| Quand une erreur critique survient. Par exemple la tentative de création d'un nouveau user avec un login déjà existant provoque une erreur critique car toutes les infos concernant le nouveau user sont perdues par le serveur.|

**Identifiant unique des erreurs :**
Quand il s'agit d'une erreur gérée, on vient de le voir, un code d'erreur est généré. Mais afin de faciliter la communication entre les utilisateurs non techniques et les administrateurs, lorsqu'une erreur survient, un identifiant unique est généré (de type uuid). Cet identifiant identifie clairement dans le log l'endroit où s'est produit l'erreur. Ainsi les utilisateurs non techniques pourront simplement transmettre cet identifiant aux administrateurs qui pourront rapidement et sans soucis retrouver le "passage" des logs concernant l'erreur et ainsi avoir l'historique de ce qui s'est passé.


Pour les développeurs
---------------------
Vous trouverez tout ça dans le module `regovar/core/framework`.






