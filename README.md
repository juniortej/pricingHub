# PricingHub Technical Test

## Description

Ce projet contient un DAG (Directed Acyclic Graph) Airflow pour un test technique. Le DAG permet d'exécuter des tâches en spécifiant les tâches à exécuter lors du déclenchement manuel du DAG.

## Configuration des Tâches

Avant d'exécuter le DAG, assurez-vous de bien définir les tâches que vous souhaitez exécuter dans la configuration. Utilisez le champ "Conf" pour spécifier les tâches à exécuter en utilisant par exemple la structure JSON suivante :

```json
{
  "tasks_to_execute": ["tache1", "tache3"]
}
Remplacez "tache1", "tache3" par les noms des tâches que vous souhaitez exécuter.