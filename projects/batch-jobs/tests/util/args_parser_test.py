import pytest

from batch_jobs.util.args_parser import DatePartition, read_args


def test_date_partition_returns_year():
    partition_dt = DatePartition("my_date", "2023-01-01")

    assert partition_dt.year() == "2023"


def test_date_partition_str_returns_dt_with_equality_to_date():
    partition_dt = DatePartition("my_date", "2023-01-01")

    assert str(partition_dt) == "dt=2023-01-01"


def test_read_args_with_short_arg_returns_partition_arg():
    args = read_args(["-p", "2023-01-01"])
    assert args.partition == "2023-01-01"


def test_read_args_with_long_arg_returns_partition_arg():
    args = read_args(["--partition", "2023-01-01"])
    assert args.partition == "2023-01-01"


def test_read_args_with_unknown_args_exits_with_non_zero_code():
    with pytest.raises(SystemExit, match="2"):
        read_args(["--partition", "2023-01-01", "--foo", "bar"])


def test_read_args_with_missing_arg_exits_with_non_zero_code():
    with pytest.raises(SystemExit, match="2"):
        read_args([])
