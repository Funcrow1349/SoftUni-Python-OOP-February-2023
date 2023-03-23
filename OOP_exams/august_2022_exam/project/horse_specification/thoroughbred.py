from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREASE_IN_TRAINING = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_INCREASE_IN_TRAINING <= self.MAX_SPEED:
            self.speed += self.SPEED_INCREASE_IN_TRAINING

        else:
            self.speed = self.MAX_SPEED

