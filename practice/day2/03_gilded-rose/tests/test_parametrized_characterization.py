import pytest
from tests.builders.create import (
    Create,
    REGULAR_ITEM,
    AGED_BRIE,
    BACKSTAGE_PASSES,
    SULFURAS,
)


@pytest.mark.parametrize(
    "start_sell_in, start_quality, expected_sell_in, expected_quality, description",
    [
        (10, 20, 9, 19, "regular item decreases quality and sell in by one"),
        (0, 5, -1, 3, "regular item decreases by two after sell in expires"),
        (5, 0, 4, 0, "regular item quality stops at zero"),
        (-3, 1, -4, 0, "expired regular item quality cannot be negative"),
    ],
)
def test_regular_item_behavior(start_sell_in, start_quality, expected_sell_in, expected_quality, description):
    gilded_rose = (
        Create.gilded_rose()
        .with_regular_item()
        .with_sell_in(start_sell_in)
        .with_quality(start_quality)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{REGULAR_ITEM}, {expected_sell_in}, {expected_quality}", description


@pytest.mark.parametrize(
    "start_sell_in, start_quality, expected_sell_in, expected_quality, description",
    [
        (12, 34, 11, 35, "backstage passes increase by one when more than 10 days left"),
        (10, 34, 9, 36, "backstage passes increase by two when 10 to 6 days left"),
        (5, 40, 4, 43, "backstage passes increase by three when 5 or fewer days left"),
        (12, 50, 11, 50, "backstage passes quality cannot exceed 50 when more than 10 days left"),
        (5, 49, 4, 50, "backstage passes quality cannot exceed 50 when 10 to 6 days left"),
        (5, 48, 4, 50, "backstage passes quality cannot exceed 50 when 5 or fewer days left"),
        (0, 45, -1, 0, "backstage passes drop to zero after concert"),
    ],
)
def test_backstage_passes_behavior(start_sell_in, start_quality, expected_sell_in, expected_quality, description):
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(start_sell_in)
        .with_quality(start_quality)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, {expected_sell_in}, {expected_quality}", description


@pytest.mark.parametrize(
    "start_sell_in, start_quality, expected_sell_in, expected_quality, description",
    [
        (3, 45, 2, 46, "aged brie increases quality over time"),
        (0, 45, -1, 47, "aged brie increases twice faster after expiration"),
        (3, 49, 2, 50, "aged brie quality cannot exceed 50"),
        (5, 50, 4, 50, "aged brie with quality 50 cannot exceed 50"),
        (-1, 50, -2, 50, "expired aged brie with quality 50 cannot exceed 50"),
    ],
)
def test_aged_brie_behavior(start_sell_in, start_quality, expected_sell_in, expected_quality, description):
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(start_sell_in)
        .with_quality(start_quality)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, {expected_sell_in}, {expected_quality}", description


@pytest.mark.parametrize(
    "start_sell_in, start_quality, expected_sell_in, expected_quality, description",
    [
        (-1, 80, -1, 80, "sulfuras does not change quality or sell in"),
    ],
)
def test_sulfuras_behavior(start_sell_in, start_quality, expected_sell_in, expected_quality, description):
    gilded_rose = (
        Create.gilded_rose()
        .with_sulfuras()
        .with_sell_in(start_sell_in)
        .with_quality(start_quality)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{SULFURAS}, {expected_sell_in}, {expected_quality}", description
