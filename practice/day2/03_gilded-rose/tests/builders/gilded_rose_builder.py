from gilded_rose import GildedRose, Item


class GildedRoseBuilder:
    def __init__(self):
        self.items = []

    def with_item(self, item: Item) -> "GildedRoseBuilder":
        self.items.append(item)
        return self

    def with_regular_item(self) -> "GildedRoseBuilder":
        from tests.builders.create import REGULAR_ITEM
        self.items.append(Item(REGULAR_ITEM, 10, 20))
        return self

    def with_aged_brie(self) -> "GildedRoseBuilder":
        from tests.builders.create import AGED_BRIE
        self.items.append(Item(AGED_BRIE, 10, 20))
        return self

    def with_backstage_passes(self) -> "GildedRoseBuilder":
        from tests.builders.create import BACKSTAGE_PASSES
        self.items.append(Item(BACKSTAGE_PASSES, 10, 20))
        return self

    def with_sulfuras(self) -> "GildedRoseBuilder":
        from tests.builders.create import SULFURAS
        self.items.append(Item(SULFURAS, -1, 80))
        return self

    def with_sell_in(self, sell_in: int) -> "GildedRoseBuilder":
        self.items[-1].sell_in = sell_in
        return self

    def with_quality(self, quality: int) -> "GildedRoseBuilder":
        self.items[-1].quality = quality
        return self

    def please(self) -> GildedRose:
        return GildedRose(self.items)
