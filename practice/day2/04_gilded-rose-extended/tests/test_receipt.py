from datetime import datetime, timedelta


def test_return_deadline_is_16_days_for_saturday(saturday_receipt):
    assert saturday_receipt.return_deadline == (
        saturday_receipt.purchase_datetime + timedelta(days=16))


def test_return_deadline_is_15_days_for_sunday(sunday_receipt):
    assert sunday_receipt.return_deadline == (
        sunday_receipt.purchase_datetime + timedelta(days=15))


def test_return_deadline_is_14_days_for_weekday(monday_morning_receipt):
    assert monday_morning_receipt.return_deadline == (
        monday_morning_receipt.purchase_datetime + timedelta(days=14))


def test_return_deadline_is_15_days_for_weekday_after_1800(monday_evening_receipt):
    assert monday_evening_receipt.return_deadline == (
        monday_evening_receipt.purchase_datetime + timedelta(days=15))


def test_status_is_can_be_returned_on_purchase_day(regular_testable_receipt):
    purchase_datetime = datetime(2026, 7, 13, 10)
    receipt = regular_testable_receipt(purchase_datetime, purchase_datetime)

    assert receipt.status == "can_be_returned"


def test_status_is_can_not_be_returned_on_16th_day(expired_monday_morning_receipt):
    assert expired_monday_morning_receipt.status == "cannot_be_returned"


def test_status_is_archived_on_31st_day_after_expiration(archived_monday_morning_receipt):
    assert archived_monday_morning_receipt.status == "archived"


def test_deadline_in_3_days_for_receipt_for_ticket_to_concert_in_five_days(receipt_for_ticket_to_concert_in_five_days):
    receipt = receipt_for_ticket_to_concert_in_five_days
    expected_return_deadline = receipt.purchase_datetime + timedelta(days=3)
    assert receipt.return_deadline == expected_return_deadline


def test_deadline_in_3_days_for_receipt_for_five_quality_left_boots(receipt_for_five_quality_left_boots):
    receipt = receipt_for_five_quality_left_boots
    expected_return_deadline = receipt.purchase_datetime + timedelta(days=3)
    assert receipt.return_deadline == expected_return_deadline


def test_deadline_as_usual_for_five_quality_left_brie(receipt_for_five_quality_left_brie):
    receipt = receipt_for_five_quality_left_brie
    expected_return_deadline = receipt.purchase_datetime + timedelta(days=14)
    assert receipt.return_deadline == expected_return_deadline


def test_deadline_as_usual_for_sulfuras(receipt_for_zero_sell_in_zero_quality_sulfuras):
    receipt = receipt_for_zero_sell_in_zero_quality_sulfuras
    expected_return_deadline = receipt.purchase_datetime + timedelta(days=14)
    assert receipt.return_deadline == expected_return_deadline
