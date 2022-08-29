import bullets


class SpecialAttack(bullets.Bullet):

    def __init__(self, rect, side):
        super().__init__(rect, side)
        self.rect = rect
        self.side = side
        self.bulletlist = []
        for i in range(9):
            bullet3 = bullets.Bullet(self.rect, self.side)
            self.bulletlist.append(bullet3)

    def shots(self):
        for bullet in self.bulletlist:
            i = self.bulletlist.index(bullet) % 9
            match i:
                case 0:  # NW
                    bullet.rect.x -= 2
                    bullet.rect.y -= 2
                case 1:  # N
                    bullet.rect.y -= 2
                case 2:  # NE
                    bullet.rect.x += 2
                    bullet.rect.y -= 2
                case 3:  # E
                    bullet.rect.x += 2
                case 4:  # SE
                    bullet.rect.x += 2
                    bullet.rect.y += 2
                case 5:  # S
                    bullet.rect.y += 2
                case 6:  # SW
                    bullet.rect.y += 2
                    bullet.rect.x -= 2
                case 7:  # W
                    bullet.rect.x -= 2
                case _:  # Default nach oben
                    bullet.rect.y -= 2

    def update(self):
        self.shots()

    def getlist(self):
        return self.bulletlist

