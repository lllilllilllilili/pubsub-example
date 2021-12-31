from google.cloud import bigquery
import base64, json, sys, os

def pubsub_to_bigq(event, context):
   pubsub_message = base64.b64decode(event['data']).decode('utf-8')
   print(pubsub_message)
   print(pubsub_message[8:])
   print(type(pubsub_message))
   table ={
      'message' : pubsub_message[8:]
   }
   #table = json.dumps(table)
   #table = json.loads(table)
   #table=pubsub_message[8:]
   print(pubsub_message[8:])
   print(type(table))
   
   #to_bigquery(os.environ['dataset'], os.environ['table'], table)
   to_bigquery('test_dataset','test_table',table)

def to_bigquery(dataset, table, document):
   bigquery_client = bigquery.Client()
   dataset_ref = bigquery_client.dataset(dataset)
   table_ref = dataset_ref.table(table)
   table = bigquery_client.get_table(table_ref)
   errors = bigquery_client.insert_rows_json(table, [document])
   if errors != [] :
      print(errors, file=sys.stderr)