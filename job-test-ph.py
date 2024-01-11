from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


DAG_NAME = "test_dag"

doc_md_DAG = """ Ce DAG, permet d'exécuter manuellement les tâches en spécifiant les tâches à exécuter. """


def execute_tasks(**kwargs):
    # Récupérer les paramètres spécifiés lors de l'exécution du DAG
    task_to_execute = kwargs["dag_run"].conf.get("tasks_to_execute", [])

    for task_id in task_to_execute:
        # Dynamiquement definition et execution
        task = PythonOperator(
            task_id=task_id,
            python_callable=lambda: print(f"Execution de la tâche {task_id}"),
            dag=dag,
        )
        task.execute(context=kwargs)


default_args = dict(
    owner="junior_T",
    retries=1,
)

dag = DAG(
    DAG_NAME,
    default_args=default_args,
    start_date=datetime(2024, 1, 10),
    description="DAG avec 3 tâches",
    schedule_interval=None,  # car DAG déclenché manuellement
    doc_md=doc_md_DAG,
)

execution_tasks = PythonOperator(
    task_id="execute_tasks",
    python_callable=execute_tasks,
    provide_context=True,
    dag=dag,
)

# ordre et dépendance
execution_tasks
