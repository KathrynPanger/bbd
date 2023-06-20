import pytest

from bbd import census, models


def test_api_key_required():
    with pytest.raises(ValueError):
        census.construct_api_call(
            geography=models.Geography.STATE,
            variables="B03003_001E",
            year=2018,
            dataset=census.DataSets.ACS5_DETAIL,
        )
