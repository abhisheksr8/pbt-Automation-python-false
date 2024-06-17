from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbtfalsepython.config.ConfigStore import *
from automationpbtfalsepython.functions import *

def script_execution(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print("Successfully Executed Son.")
    out0 = in0

    return out0
