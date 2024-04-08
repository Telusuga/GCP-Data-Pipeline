from googleapiclient.discovery import build

def dataflow_trigger(cloud_event, environment):
    try:
        dataflow = build('dataflow', 'v1b3')
        project_id='erudite-justice-418518'
        location='us-central1'
        body={
    'jobName':'bqload',
    'parameters':{
        'bigQueryLoadingTemporaryDirectory':'gs://temp_df_0305/df/',
        'outputTable':'erudite-justice-418518.landing.df-test',
        'inputFilePattern':'gs://input_bucket_0305/initial.json',
        'JSONPath':'gs://temp_df_0305/bq.json',
        'javascriptTextTransformGcsPath': "gs://temp_df_0305/function.js",
        "javascriptTextTransformFunctionName": "jsonConvertor"
    }
}
        template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

        #response = dataflow.projects().jobs().update(jobId='bqload', body={}).execute()
        response = dataflow.projects().locations().templates().launch(projectId=project_id,location=location,body=body,gcsPath=template_path).execute()
        print('Dataflow job triggered:', response)
        
        return 'Dataflow job triggered successfully'
    except Exception as e:
        print('Failed due to the following error:', e)
        return 'Dataflow job failed'