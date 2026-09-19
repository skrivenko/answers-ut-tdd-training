import json
from pathlib import Path
from gilded_rose import GildedRose, Item


def test_quality_of_all_items_within_7_days():
    items = [
        Item("Elixir of the Mongoose", 5, 7),
        Item("Aged Brie", 2, 0),
        Item("Aged Brie", -1, 49),
        Item("Sulfuras, Hand of Ragnaros", -1, 80),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
    ]

    days = 7

    actual = _generate_actual_output(items, days)
    expected = _load_expected_output()

    assert actual == expected


def _generate_actual_output(items, days):
    gilded_rose = GildedRose(items)

    actual = []
    for i in range(days):
        actual.append(f"-------- day {i} --------")
        for item in items:
            actual.append(str(item))
        gilded_rose.update_quality()

    return actual


def _load_expected_output():
    expected_path = Path(__file__).parent / "resources" / "golden_master_test_expected.txt"
    return json.loads(expected_path.read_text())
