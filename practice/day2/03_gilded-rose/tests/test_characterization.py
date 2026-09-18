from tests.builders.create import (
    Create,
    REGULAR_ITEM,
    AGED_BRIE,
    BACKSTAGE_PASSES,
    SULFURAS,
)


# tests for regular item


def test_regular_item_decreases_quality_and_sell_in_by_one():
    gilded_rose = (
        Create.gilded_rose()
        .with_regular_item()
        .with_sell_in(10)
        .with_quality(20)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{REGULAR_ITEM}, 9, 19"


def test_regular_item_decreases_by_two_after_sell_in_expires():
    gilded_rose = (
        Create.gilded_rose()
        .with_regular_item()
        .with_sell_in(0)
        .with_quality(5)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{REGULAR_ITEM}, -1, 3"


def test_regular_item_quality_stops_at_zero():
    gilded_rose = (
        Create.gilded_rose()
        .with_regular_item()
        .with_sell_in(5)
        .with_quality(0)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{REGULAR_ITEM}, 4, 0"


def test_expired_regular_item_quality_cannot_be_negative():
    gilded_rose = (
        Create.gilded_rose()
        .with_regular_item()
        .with_sell_in(-3)
        .with_quality(1)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{REGULAR_ITEM}, -4, 0"


# tests for backstage passes


def test_backstage_passes_increase_by_one_when_more_than_10_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(12)
        .with_quality(34)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 11, 35"


def test_backstage_passes_increase_by_two_when_10_to_6_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(10)
        .with_quality(34)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 9, 36"


def test_backstage_passes_increase_by_three_when_5_or_fewer_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(5)
        .with_quality(40)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 4, 43"


def test_backstage_passes_quality_cannot_exceed_50_when_more_than_10_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(12)
        .with_quality(50)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 11, 50"


def test_backstage_passes_quality_cannot_exceed_50_when_10_to_6_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(5)
        .with_quality(49)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 4, 50"


def test_backstage_passes_quality_cannot_exceed_50_when_5_or_fewer_days_left():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(5)
        .with_quality(48)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, 4, 50"


def test_backstage_passes_drop_to_zero_after_concert():
    gilded_rose = (
        Create.gilded_rose()
        .with_backstage_passes()
        .with_sell_in(0)
        .with_quality(45)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{BACKSTAGE_PASSES}, -1, 0"


# tests for aged brie


def test_aged_brie_increases_quality_over_time():
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(3)
        .with_quality(45)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, 2, 46"


def test_aged_brie_increases_twice_faster_after_expiration():
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(0)
        .with_quality(45)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, -1, 47"


def test_aged_brie_quality_cannot_exceed_50():
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(3)
        .with_quality(49)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, 2, 50"


def test_aged_brie_with_quality_50_cannot_exceed_50():
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(5)
        .with_quality(50)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, 4, 50"


def test_expired_aged_brie_with_quality_50_cannot_exceed_50():
    gilded_rose = (
        Create.gilded_rose()
        .with_aged_brie()
        .with_sell_in(-1)
        .with_quality(50)
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{AGED_BRIE}, -2, 50"


# tests for sulfuras


def test_sulfuras_does_not_change_quality_or_sell_in():
    gilded_rose = (
        Create.gilded_rose()
        .with_sulfuras()
        .please()
    )

    gilded_rose.update_quality()

    assert str(gilded_rose.items[0]) == f"{SULFURAS}, -1, 80"
