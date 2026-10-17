# Troop.py
from PIL import Image, ImageTk
import math

class Troop:
    def __init__(self, canvas, stats, sizes, x, y, troop_name, troop_id, speedX, speedY, canvasReference):
        self.canvas = canvas
        self.name = troop_name
        self.id = troop_id

        self.x = x
        self.y = y
        self.friendly = stats["friendly"]
        self.speed = stats["speed"]
        self.health = stats["health"]
        self.damage = stats["damage"]
        self.type = stats["type"]
        self.color = stats["color"]
        self.size = sizes[stats["size"]]
        self.vision = stats["vision"]
        self.attackSpeed = stats["attackSpeed"]*1000 #ottieni i dati in millisecondi
        self.sprite_path = stats.get("sprite_path", None)

        self.vx = speedX
        self.vy = speedY

        #ottieni la reference del canvas, ottenendo tutti i poteri di modificare cosa c'è sul gioco manco l'admin
        self.canvasReference = canvasReference 

        self.canMove = False
        self.enemyInRange = False
        self.enemyAtLeft = False
        self.enemyAbove = False
        self.enemyBelow = False
        self.nearestEnemy = 0
        self.nearestEnemyId = 0
        self.haveObjective = False

        self.active = True
        self.attackCooldown = 0
        self._move_job = None
        self._update_job = None

        self.canvas_id = self._place_on_canvas()
        self.CheckIfSpell()
        if self.active:
            self._move_job = self.canvas.after(50, self.move)
            self._update_job = self.canvas.after(50, self.Update)

    def _place_on_canvas(self):

        if self.sprite_path:
            try:
                img = Image.open(self.sprite_path)
                img = img.resize((self.size * 5, self.size * 5))
                self._tk_image = ImageTk.PhotoImage(img)
                if not hasattr(self.canvas, 'images'):
                    self.canvas.images = []
                self.canvas.images.append(self._tk_image)
                return self.canvas.create_image(self.x, self.y, image=self._tk_image, tags=str(self.id))
            except Exception as e:
                print(f"Sprite load failed for {self.name}: {e}")

        # fallback: colored rectangle
        return self.canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, tags=str(self.id)
        )

    def move(self, dx=None, dy=None):
        if not self.active:
            return

        if dx is not None:
            self.vx = dx
        if dy is not None:
            self.vy = dy

        # Default to stored velocity if no manager pathing is available.
        dx = self.vx or 0
        dy = self.vy or 0

        if self.canvasReference and hasattr(self.canvasReference, 'damage_tower') and self.enemyInRange == False:
            x = self.x
            y = self.y
            if 245 > x > 150 or x < 54:
                if y > 160:
                    dx, dy = self.speed, 0
                else:
                    if x > 190:
                        dx, dy = -self.speed, 0
                    else:
                        self.canvasReference.damage_tower(x - 45, y - 10, x, y + 10, self.damage, "troop", self.attackCooldown, self.attackSpeed, self.id)
                        dx, dy = 0, 0

            elif 150 >= x > 55 or x > 246:
                if y > 160:
                    dx, dy = -self.speed, 0
                else:
                    if x < 110:
                        dx, dy = self.speed, 0
                    else:
                        self.canvasReference.damage_tower(x, y - 10, x + 45, y + 10, self.damage, "troop", self.attackCooldown, self.attackSpeed, self.id)
                        dx, dy = 0, 0

            else:
                if y > 160:
                    dx, dy = 0, -self.speed
                else:
                    if x < 150:
                        if self.canvasReference.leftTowerAlive:
                            self.canvasReference.damage_tower(x - 10, y, x + 10, y + 20, self.damage, "troop", self.attackCooldown, self.attackSpeed, self.id)
                            dx, dy = 0, 0
                        else:
                            if y > 100:
                                dx, dy = 0, -self.speed
                            else:
                                dx, dy = self.speed, 0
                    else:
                        if self.canvasReference.rightTowerAlive:
                            self.canvasReference.damage_tower(x - 10, y, x + 10, y + 20, self.damage, "troop", self.attackCooldown, self.attackSpeed, self.id)
                            dx, dy = 0, 0
                        else:
                            if y > 100:
                                dx, dy = 0, -self.speed
                            else:
                                dx, dy = -self.speed, 0

        if self.enemyInRange:
            if self.enemyAtLeft:
                dx = -self.speed
            else:
                dx = self.speed

            if self.enemyAbove:
                dy = -self.speed
            else:
                dy = self.speed

        self.x += dx
        self.y += dy
        self.canvas.move(self.canvas_id, dx, dy)

        # schedule next frame (50 ms)
        self._move_job = self.canvas.after(50, self.move)

    #aggiorna ogni frame(50 ms)
    def Update(self):
        if not self.active:
            return

        #controlla la vita
        if self.health <= 0:
            self.destroy()
            return

        self.attackCooldown += 50

        #controlla se ci sono truppe nemiche in range
        for troop in self.canvasReference.troops_in_game:
            if troop is self or troop.friendly or self.haveObjective:
                continue
            self.CheckInRange(self.x, self.y, troop.x, troop.y, troop.id)

        self._update_job = self.canvas.after(50, self.Update)

    def CheckInRange(self, selfX, selfY, enemyX, enemyY, id):
        if abs(selfX - enemyX) <= self.vision and abs(selfY - enemyY) <= self.vision:
            self.enemyInRange = True
            if selfX > enemyX:
                self.enemyAtLeft = True
            elif selfX < enemyX:
                self.enemyAtLeft = False
            if selfY > enemyY:
                self.enemyAbove = True
            elif selfY < enemyY:
                self.enemyAbove = False
                
            if math.hypot(selfX - enemyX, selfY - enemyY) <= self.nearestEnemy or self.nearestEnemy == 0:
                self.haveObjective = True
                self.nearestEnemyId = id
                self.nearestEnemy = math.hypot(selfX - enemyX, selfY - enemyY) #ipotenusa tra il nemico e la truppa

        else:
            self.enemyInRange = False

    def take_damage(self, amount):
        self.health -= amount

    def destroy(self):
        self.active = False

        # cancel any pending callbacks
        if self._move_job is not None:
            self.canvas.after_cancel(self._move_job)
        if self._update_job is not None:
            self.canvas.after_cancel(self._update_job)

        self.canvas.delete(self.canvas_id)
        if self in self.canvasReference.troops_in_game:
            self.canvasReference.troops_in_game.remove(self)

    def dealDamage(self, damage, target):
        target -= damage

    def CheckIfSpell(self):
        if self.type == "spell":
            self.active = False
            self.canvasReference.damage_tower(self.x - 45, self.y - 10, self.x, self.y + 10, self.damage, "spell", self.attackCooldown, self.attackSpeed)
            self.canvas.after(1000, self.destroy)