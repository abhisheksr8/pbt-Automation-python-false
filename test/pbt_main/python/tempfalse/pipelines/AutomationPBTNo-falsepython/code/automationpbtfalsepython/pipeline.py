from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automationpbtfalsepython.config.ConfigStore import *
from automationpbtfalsepython.functions import *
from prophecy.utils import *
from automationpbtfalsepython.graph import *

def pipeline(spark: SparkSession) -> None:
    df_s3_source_dataset = s3_source_dataset(spark)
    create_lookup_test(spark, df_s3_source_dataset)
    df_select_all_from_in0 = select_all_from_in0(spark, df_s3_source_dataset)
    df_reformatted_customers = reformatted_customers(spark, df_s3_source_dataset)
    df_script_execution = script_execution(spark, df_reformatted_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("AutomationPBT-falsepython")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/AutomationPBTNo-falsepython")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/AutomationPBTNo-falsepython", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
