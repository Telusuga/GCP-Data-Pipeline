import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

beam_option=PipelineOptions(
    runner='DataflowRunner',
    project='erudite-justice-418518',
    job_name='bqload',
    region='us-central1',
    temp_location='gs://sdk_push/pipeline_dump'
)

def type_check(t):
    return print(type(t))


def json_convertor(t):
    try:
        return json.loads(t)
    except Exception as e:
        print('The following has been failed with the following {0}'.format(e))
    
with beam.Pipeline(options=beam_option) as P:
        input=(P
               | 'reading from file' >> beam.io.ReadFromText('gs://sdk_push/initial.json')
               | 'json convertor' >> beam.Map(json_convertor)
    )
        (input
        | 'loading data to Bigquery' >> beam.io.WriteToBigQuery(
            table='erudite-justice-418518.landing.table_2',
            schema='MatchId:Integer, SeriesId:Integer, SeriesName:String, MatchDesc:String, MatchFormat:String, StartDate:String, EndDate:String, State:String, Status:String',
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            custom_gcs_temp_location='gs://sdk_push/temp_1'
        ))
        
