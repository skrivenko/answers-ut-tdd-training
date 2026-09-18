from datetime import datetime

from freezegun import freeze_time

from gilded_rose import GildedRose


class FakeReceipt:
    def __init__(self, status, label="receipt"):
        self.status = status
        self._label = label

    def __repr__(self):
        return self._label


def test_empty_receipts():
    report = GildedRose([], []).generate_receipt_report()
    assert "can_be_returned: 0\n" in report
    assert "cannot_be_returned: 0\n" in report
    assert "archived: 0\n" in report


def test_counts_can_be_returned():
    report = GildedRose([], [FakeReceipt("can_be_returned")]).generate_receipt_report()
    assert "can_be_returned: 1\n" in report


def test_counts_cannot_be_returned():
    report = GildedRose([], [FakeReceipt("cannot_be_returned")]).generate_receipt_report()
    assert "cannot_be_returned: 1\n" in report


def test_counts_archived():
    report = GildedRose([], [FakeReceipt("archived")]).generate_receipt_report()
    assert "archived: 1\n" in report


def test_non_archived_appears_in_details():
    receipt = FakeReceipt(
        "can_be_returned", label="boots, Alice, 2026-07-27 10:00, can_be_returned")
    report = GildedRose([], [receipt]).generate_receipt_report()
    assert str(receipt) in report


def test_archived_excluded_from_details():
    receipt = FakeReceipt(
        "archived", label="boots, Alice, 2026-07-01 10:00, archived")
    report = GildedRose([], [receipt]).generate_receipt_report()
    assert str(receipt) not in report


@freeze_time("2026-07-13 15:30:00")
def test_header_contains_current_datetime():
    report = GildedRose([], [], datetime.now).generate_receipt_report()
    assert "2026-07-13 15:30:00" in report


@freeze_time("2026-07-13 15:30:00")
def test_full_report_with_one_receipt_per_status():
    can = FakeReceipt("can_be_returned",
                      "sword, Alice, 2026-07-27 10:00, can_be_returned")
    cannot = FakeReceipt("cannot_be_returned",
                         "boots, Bob, 2026-07-20 10:00, cannot_be_returned")
    archived = FakeReceipt(
        "archived", "shield, Carol, 2026-06-01 10:00, archived")
    rose = GildedRose([], [can, cannot, archived], datetime.now)

    report = rose.generate_receipt_report()

    expected = (
        f"===== Receipt Report [2026-07-13 15:30:00] =====\n"
        "can_be_returned: 1\n"
        "cannot_be_returned: 1\n"
        "archived: 1\n"
        "\n"
        "sword, Alice, 2026-07-27 10:00, can_be_returned\n"
        "boots, Bob, 2026-07-20 10:00, cannot_be_returned\n"
    )
    assert report == expected
