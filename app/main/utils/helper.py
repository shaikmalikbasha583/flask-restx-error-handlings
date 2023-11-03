import datetime


def get_isoformated_timestamp(input_timestamp: datetime.datetime) -> str:
    return input_timestamp.isoformat(sep="T", timespec="milliseconds") + "Z"
