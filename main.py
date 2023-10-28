import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [(255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 192, 203),
    (128, 0, 128),
    (139, 69, 19),
    (144, 238, 144),
    (135, 206, 250),
    (245, 245, 220),
    (128, 128, 128),
    (255, 255, 224),
    (128, 128, 0),
    (211, 211, 211),
    (65, 105, 225),
    (75, 0, 130),
    (230, 230, 250),
    (173, 216, 230),
    (255, 105, 180),
    (0, 128, 0),
    (255, 215, 0),
    (64, 224, 208),
    (255, 240, 245),
    (169, 169, 169),
    (85, 107, 47),
    (139, 0, 0),
    (0, 0, 139),
    (205, 149, 117),
    (0, 206, 209),
    (148, 0, 211),
    (255, 127, 80),
    (34, 139, 34),
    (70, 130, 180),
    (205, 127, 50),
    (50, 205, 50),
    (173, 216, 230),
    (244, 164, 96),
    (205, 92, 92),
    (210, 105, 30),
    (139, 0, 0),
    (128, 128, 144),
    (255, 192, 203),
    (175, 238, 238),
    (230, 230, 250),
    (50, 205, 50)]



# La classe Balle donne les paramètres, dessine et déplace les balles qui bougent à l'écran
class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randrange(-7, 7, 2)
        self.change_y = random.randrange(-7, 7, 2)
        self.rayon = random.randint(10, 30)
        self.couleur = random.choice(COLORS)

    # Mise à jour de la position de la balle, en vérifiant les bords de l'écran
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1

        if self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

    # Dessine la balle à l'écran
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)

# La classe Rectangle donne les paramètres, dessine et déplace les rectangles qui bougent à l'écran
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randrange(-7, 7, 2)
        self.change_y = random.randrange(-7, 7, 2)
        self.width = random.randint(20, 70)
        self.height = random.randint(20, 70)
        self.color = random.choice(COLORS)
        self.angle = random.random() * 360

    # Mise à jour de la position du rectangle, en vérifiant les bords de l'écran
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.x = 0
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1

        if self.y < 0:
            self.y = 0
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1

    # Dessine le rectangle à l'écran
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

# La classe MyGame gère le jeu
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []

    # Ajoute une balle si le bouton de gauche de la souris est cliqué et ajoute un rectangle si le bouton de droite de la souris est cliqué
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y)
            self.balles.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y)
            self.rectangles.append(rectangle)

    def setup(self):
        pass

    # Dessine chaque balle et rectangle dans la liste
    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.draw()
        for rectangle in self.rectangles:
            rectangle.draw()

    # Mise à jour des positions des balles et des rectangles
    def update(self, delta_time):
        for balle in self.balles:
            balle.update()
        for rectangle in self.rectangles:
            rectangle.update()

def main():
    my_game = MyGame()
    arcade.run()

main()
