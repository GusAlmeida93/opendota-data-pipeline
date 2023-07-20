from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateClusterOperator, DataprocSubmitJobOperator, DataprocDeleteClusterOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

CLUSTER_NAME = "hello-cluster"
PROJECT_ID = 'opendota-data-pipeline'
REGION = 'us-east1'
BUCKET = 'opendota-dataproc'
FOLDER = 'hello-world/'
PYSPARK_FILE = 'hello_world.py'

CLUSTER_CONFIG = {
    "master_config": {
        "num_instances": 1,
        "machine_type_uri": "e2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 30},
    },
    "worker_config": {
        "num_instances": 2,
        "machine_type_uri": "e2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 30},
    },
    }

PYSPARK_JOB  = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": f"gs://{BUCKET}/{FOLDER}{PYSPARK_FILE}"},
    }


with DAG(
    dag_id='hello_world_dataproc',
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['hello_world_dataproc'],
    
) as dag:

    create_cluster = DataprocCreateClusterOperator(
        task_id="create_cluster",
        project_id=PROJECT_ID,
        cluster_config=CLUSTER_CONFIG,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        gcp_conn_id="teste"
    )

    spark_submit = DataprocSubmitJobOperator(
        task_id="spark_submit", 
        job=PYSPARK_JOB, 
        region=REGION, 
        project_id=PROJECT_ID,
        gcp_conn_id="teste"
    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        cluster_name=CLUSTER_NAME,
        region=REGION,
        gcp_conn_id="teste"
    )
    
    create_cluster >> spark_submit >> delete_cluster