from tests.builders.gilded_rose_builder import GildedRoseBuilder


REGULAR_ITEM = "Elixir of the Mongoose"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class Create:
    @staticmethod
    def gilded_rose() -> GildedRoseBuilder:
        return GildedRoseBuilder()
