# flake8: noqa
import warnings

try:
    from qadataframe.qadataframe import version
except ImportError as e:  # pragma: no cover

    def version() -> str:
        return ""

    # this is only useful for documentation
    warnings.warn("qadataframe binary missing!")

import qadataframe.testing as testing
from qadataframe.cfg import (  # flake8: noqa. We do not export in __all__
    Config,
    toggle_string_cache,
)
from qadataframe.convert import from_arrow, from_dict, from_dicts, from_pandas, from_records
from qadataframe.datatypes import (
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Duration,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    List,
    Null,
    Object,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Utf8,
)
from qadataframe.exceptions import (
    ArrowError,
    ComputeError,
    NoDataError,
    NotFoundError,
    SchemaError,
    ShapeError,
)
from qadataframe.internals.expr import Expr
from qadataframe.internals.frame import (  # flake8: noqa # TODO: remove need for wrap_df
    DataFrame,
    wrap_df,
)
from qadataframe.internals.functions import arg_where, concat, date_range, get_dummies
from qadataframe.internals.lazy_frame import LazyFrame
from qadataframe.internals.lazy_functions import _date as date
from qadataframe.internals.lazy_functions import _datetime as datetime
from qadataframe.internals.lazy_functions import (
    all,
    any,
    apply,
    arange,
    argsort_by,
    avg,
    col,
    collect_all,
    concat_list,
    concat_str,
    count,
    cov,
    duration,
    exclude,
    first,
    fold,
    format,
    groups,
    head,
    last,
    lit,
    map,
    map_binary,
    max,
    mean,
    median,
    min,
    n_unique,
    pearson_corr,
    quantile,
    repeat,
    select,
    spearman_rank_corr,
    std,
    struct,
    sum,
    tail,
)
from qadataframe.internals.lazy_functions import to_list as list
from qadataframe.internals.lazy_functions import var
from qadataframe.internals.series import (  # flake8: noqa # TODO: remove need for wrap_s
    Series,
    wrap_s,
)
from qadataframe.internals.whenthen import when
from qadataframe.io import (
    read_avro,
    read_csv,
    read_ipc,
    read_ipc_schema,
    read_json,
    read_parquet,
    read_sql,
    scan_csv,
    scan_ipc,
    scan_parquet,
)
from qadataframe.string_cache import StringCache

__all__ = [
    "exceptions",
    "NotFoundError",
    "ShapeError",
    "SchemaError",
    "ArrowError",
    "ComputeError",
    "NoDataError",
    "DataFrame",
    "Series",
    "LazyFrame",
    # qadataframe.datatypes
    "DataType",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "Float32",
    "Float64",
    "Boolean",
    "Utf8",
    "List",
    "Date",
    "Datetime",
    "Time",
    "Object",
    "Categorical",
    "Struct",
    # qadataframe.io
    "read_csv",
    "read_parquet",
    "read_json",
    "read_sql",
    "read_ipc",
    "scan_csv",
    "scan_ipc",
    "scan_parquet",
    "read_ipc_schema",
    "read_avro",
    # qadataframe.stringcache
    "StringCache",
    # qadataframe.config
    "Config",
    # qadataframe.internal.when
    "when",
    # qadataframe.internal.expr
    "Expr",
    # qadataframe.internal.functions
    "arg_where",
    "concat",
    "date_range",
    "get_dummies",
    "repeat",
    # qadataframe.internal.lazy_functions
    "col",
    "count",
    "std",
    "var",
    "max",
    "min",
    "sum",
    "mean",
    "avg",
    "median",
    "n_unique",
    "first",
    "last",
    "head",
    "tail",
    "lit",
    "pearson_corr",
    "spearman_rank_corr",
    "cov",
    "map",
    "apply",
    "map_binary",
    "fold",
    "any",
    "all",
    "groups",
    "quantile",
    "arange",
    "argsort_by",
    "concat_str",
    "concat_list",
    "collect_all",
    "exclude",
    "format",
    "datetime",  # named _datetime, see import above
    "date",  # name _date, see import above
    "list",  # named to_list, see import above
    "select",
    "var",
    # qadataframe.convert
    "from_dict",
    "from_dicts",
    "from_records",
    "from_arrow",
    "from_pandas",
    # testing
    "testing",
]

__version__ = version()

import os

os.environ["POLARS_ALLOW_EXTENSION"] = "true"
