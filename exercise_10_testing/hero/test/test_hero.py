from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Gosho", 1, 50, 50)
        self.enemy = Hero("Pesho", 1, 40, 40)

    def test_init_correct(self):
        self.assertEqual(self.hero.username, "Gosho")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 50)
        self.assertEqual(self.hero.damage, 50)

    def test_if_hero_battling_himself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_if_hero_battling_without_health_raises_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_hero_battling_an_enemy_without_health_raises_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ve.exception), "You cannot fight Pesho. He needs to rest")

    def test_if_battle_ends_in_draw(self):
        self.enemy.health = 50
        self.enemy.damage = 50
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "Draw")

    def test_if_hero_wins_and_stats_increase_properly(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 15)
        self.assertEqual(self.hero.damage, 55)
        self.assertEqual(result, "You win")

    def test_if_hero_loses_and_enemy_stats_increase_properly(self):
        self.enemy.health = 100
        self.enemy.damage = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 55)
        self.assertEqual(self.enemy.damage, 105)
        self.assertEqual(result, "You lose")

    def test__str__returns_correct_data(self):
        self.assertEqual(
            "Hero Gosho: 1 lvl\n" +
            "Health: 50\n" +
            "Damage: 50\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()
