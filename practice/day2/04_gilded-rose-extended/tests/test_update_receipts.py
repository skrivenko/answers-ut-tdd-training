from datetime import datetime, timedelta

from freezegun import freeze_time

from gilded_rose import GildedRose


def test_keep_can_be_returned_receipt_status(monday_morning_receipt):
    with freeze_time(monday_morning_receipt.return_deadline):
        gilded_rose = GildedRose([], [monday_morning_receipt])
        gilded_rose.update_receipts_for_date(datetime.now())
        assert monday_morning_receipt.status == "can_be_returned"


def test_update_receipt_to_cannot_be_returned(monday_morning_receipt):
    with freeze_time(monday_morning_receipt.return_deadline + timedelta(days=1)):
        gilded_rose = GildedRose([], [monday_morning_receipt])
        gilded_rose.update_receipts_for_date(datetime.now())
        assert monday_morning_receipt.status == "cannot_be_returned"


def test_keep_cannot_be_returned_receipt_status(monday_morning_receipt):
    with freeze_time(monday_morning_receipt.return_deadline + timedelta(days=30)):
        gilded_rose = GildedRose([], [monday_morning_receipt])
        gilded_rose.update_receipts_for_date(datetime.now())
        assert monday_morning_receipt.status == "cannot_be_returned"


def test_update_receipt_to_archived(monday_morning_receipt):
    with freeze_time(monday_morning_receipt.return_deadline + timedelta(days=31)):
        gilded_rose = GildedRose([], [monday_morning_receipt])
        gilded_rose.update_receipts_for_date(datetime.now())
        assert monday_morning_receipt.status == "archived"
