#=============================================================================================
#31/01/2023 -Rodri Noya-

#Herramienta en python para
# - hacer snapshots de prometheus
# - comprimirlosi
# - guardarlos en gcp bucket

#=============================================================================================
from google.cloud import storage
import subprocess
import requests
import sys
import os
import base64

class PrometheusBackupTool:
    def __init__(self, bucket_name, file_name):
        self.bucket_name           = bucket_name
        self.file_name             = file_name
        self.credentials           = ''

    def create_backup(self):
        try:
            backup_directory = "/app/backups"
            if not os.path.exists(backup_directory):
                print(f" + Creating backup folder")
                os.makedirs(backup_directory)
            print(f" + Creating backup: {self.file_name}")
            cmd = f"tar czf /app/backups/{self.file_name} /shared-folder"
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            print(output.decode('utf-8'))
            print(f" [OK] Backup creation successful en /app/backups/{self.file_name}")
        #except Exception as e:
        except subprocess.CalledProcessError as e:
            print(" [FAIL] Error during backup creation:", e.output.decode('utf-8'))
            #print("Something went wrong with the backup creation", str(e))
            sys.exit(" - Stoping execution")

    def upload_backup(self):
        try:
            cmd = f"cat /app/credentials/credentials.json"
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            print(f' + Uploading backup to bucket: {self.bucket_name}')
            # Upload the backup to GCP bucket
            client = storage.Client()
            bucket = client.get_bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            blob.upload_from_filename(f'/app/backups/{self.file_name}')
            print(' [OK] Upload complete!')
        except Exception as e:
            print(" [FAIL] Failed to upload backup to GCP bucket", str(e))
            sys.exit("Stopping execution")

if __name__ == "__main__":
    bucket_name           = os.environ.get("BUCKET_NAME")
    file_name             = os.environ.get("FILE_NAME")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'/app/credentials/credentials.json'

    prometheus  = PrometheusBackupTool(bucket_name, file_name)

    prometheus.create_backup()
    prometheus.upload_backup()
