from enum import Enum

from pydantic import BaseModel as PydanticBaseModel


def to_camel(string: str) -> str:
    head, *tail = string.split("_")
    return "".join(head, *map(str.capitalize, tail))


class BaseModel(PydanticBaseModel):
    """convert the snake_case definitions to the actual models implementations"""

    alias_generator = to_camel
    use_enum_values = True


class BaseProduct(BaseModel):
    """Base object that all product objects contain"""

    id: str
    publicName: str
    type: str


class SummaryDay(BaseModel):
    date: str
    content: str


class Summary(BaseModel):
    days: list[SummaryDay]


# TODO: add type to what each day is
class TerrainAndTravelAdvice(BaseModel):
    days: list[dict] * 3


class Communication(BaseModel):
    headline: str
    sms: ""


class Image(BaseModel):
    id: str
    url: str
    width: int
    height: int
    credit: ""
    caption: str
    tag: str


class Media(BaseModel):
    # note that Images is captialized in snake and camel case
    Images: list[Image]


class DangerRatingDay(BaseModel):
    position: int
    alp: str  # alpine / above treeline
    tln: str  # treeline
    btl: str  # below treeline
    date: str


class DangerRatings(BaseModel):
    """days a 3 item array for [today, tomorrow, day_after]"""

    days: DangerRatingDay * 3


class AvalancheProblem(BaseModel):
    type: str
    aspectElevations: list[AspectElevation]


class AvalancheForecast(BaseProduct):
    polygons: list[str]
    areaId: str
    forecaster: str
    issue_date_time: str
    expiry_date_time: str
    is_translated: str
    weather_summary: Summary
    snowpack_summary: Summary
    avlanache_summary: Summary
    terrain_and_travel_advice: TerrainTravelAdice
    communication: Communication
    media: Media
    dangerRatings: DangerRatings


class ProductType(Enum):
    AVALANCHE_FORECAST = "avalancheforecast"
    SPECIAL_PRODUCT = "specialproduct"
    REGIONAL_DISCUSSION = "regionaldiscussion"


class SpecialProductType(Enum):
    SPECIAL_ADVISORY = "specialAdvisory"
    WARNING = "warning"
    WATCH = "watch"


# class AspectElevation(Enum):
