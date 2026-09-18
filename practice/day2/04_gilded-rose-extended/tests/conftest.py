from datetime import datetime, timedelta

from freezegun import freeze_time
from pytest import fixture

from gilded_rose import Item, Receipt
from tests.testable_receipt import TestableReceipt


@fixture
def regular_item():
    return Item("Regular item", 50, 50)


@fixture
def sulfuras():
    return Item("Sulfuras, Hand of Ragnaros", 0, 0)


@fixture
def five_days_left_concert_ticket():
    return Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)


@fixture
def five_quality_left_done_boots():
    return Item("Boots", 50, 5)


@fixture
def five_quality_left_brie():
    return Item("Aged Brie", 50, 5)


@fixture
@freeze_time("2026-07-11")
def receipt_for_ticket_to_concert_in_five_days(five_days_left_concert_ticket):
    return Receipt(five_days_left_concert_ticket, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-11")
def receipt_for_five_quality_left_boots(five_quality_left_done_boots):
    return Receipt(five_quality_left_done_boots, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13")
def receipt_for_five_quality_left_brie(five_quality_left_brie):
    return Receipt(five_quality_left_brie, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13")
def receipt_for_zero_sell_in_zero_quality_sulfuras(sulfuras):
    return Receipt(sulfuras, "Thrall", datetime.now())


@fixture
def regular_receipt(regular_item):
    return lambda purchase_date: Receipt(regular_item, "Thrall", purchase_date)


@fixture
def regular_testable_receipt(regular_item):
    return lambda purchase_date, now_override: TestableReceipt(now_override, regular_item, "Thrall", purchase_date)


@fixture
@freeze_time("2026-07-11")
def saturday_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-12")
def sunday_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 10:00")
def monday_morning_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 18:00")
def monday_evening_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 10:00")
def expired_monday_morning_receipt(regular_item, monday_morning_receipt):
    return TestableReceipt(
        monday_morning_receipt.return_deadline + timedelta(days=1),
        regular_item,
        monday_morning_receipt.customer_name,
        monday_morning_receipt.purchase_datetime,
    )


@fixture
@freeze_time("2026-07-13 10:00")
def archived_monday_morning_receipt(regular_item, monday_morning_receipt):
    return TestableReceipt(
        monday_morning_receipt.return_deadline + timedelta(days=31),
        regular_item,
        monday_morning_receipt.customer_name,
        monday_morning_receipt.purchase_datetime,
    )
