import turtle as trtl
import random as rndm
import math as m

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("bg.gif")

score = 0 #score
playerAlive = True # states whether the player is alive or dead

# add sprites
playerShape = "ship.gif"
wn.addshape(playerShape)
enemy1Shape = "enemy1.gif"
wn.addshape(enemy1Shape)
enemy2Shape = "enemy2.gif"
wn.addshape(enemy2Shape)
enemy3Shape = "enemy3.gif"
wn.addshape(enemy3Shape)
shotShape = "shot.gif"
wn.addshape(shotShape)

# initialize player
player = trtl.Turtle(shape = playerShape)
player._delay(0)
player.speed(0)
player.pu()
player.goto(0, -300)
player.seth(90)

# initialize player's bullet
shot = trtl.Turtle(shape = shotShape)
shot.speed(0)
shot.seth(90)
shot.pu()

# this turtle writes "SCORE", "HIGH SCORE", and "YOU WIN!" or "YOU LOSE!"
fontTurtle = trtl.Turtle(visible = False)
fontTurtle._delay(0)
fontTurtle.speed(0)
fontTurtle.pencolor("red")
fontTurtle.pu()
fontTurtle.goto(-330, 460)

# this turtle updates your score
scoreTurtle = trtl.Turtle(visible = False)
scoreTurtle._delay(0)
scoreTurtle.speed(0)
scoreTurtle.pencolor("white")
scoreTurtle.pu()
scoreTurtle.goto(-170, 460)

# write score stuff
scoreTurtle.write(score, font = ("Impact", 40, "bold"))
fontTurtle.write("SCORE", font = ("Impact", 40, "bold"))
fontTurtle.goto(-40, 460)
fontTurtle.write("HIGH SCORE", move = True, font = ("Impact", 40, "bold"))
fontTurtle.fd(20)
fontTurtle.pencolor("white")
fontTurtle.write(5200, font = ("Impact", 40, "bold"))

# lists that enemies go into (each list represents one row of enemies)
enemies1 = []
enemies2 = []
enemies3 = []
enemyLists = [enemies1, enemies2, enemies3] # list of the other lists
enemyStartingX = -185 # enemyStartingX is where the program starts to initialize the enemies

# initialize enemies
for i in range(10):
    enemy = trtl.Turtle(shape = enemy2Shape)
    enemy._delay(0)
    enemy.speed(0)
    enemy.seth(270)
    enemy.pu()
    enemy.goto(enemyStartingX, 85)
    enemies1.append(enemy)
    enemyStartingX += 40
enemyStartingX = -225
for i in range(12):
    enemy2 = trtl.Turtle(shape = enemy3Shape)
    enemy2._delay(0)
    enemy2.speed(0)
    enemy2.seth(270)
    enemy2.pu()
    enemy2.goto(enemyStartingX, 40)
    enemies2.append(enemy2)
    enemyStartingX += 40
enemyStartingX = -265
for i in range(14):
    enemy3 = trtl.Turtle(shape = enemy1Shape)
    enemy3._delay(0)
    enemy3.speed(0)
    enemy3.seth(270)
    enemy3.pu()
    enemy3.goto(enemyStartingX, 0)
    enemies3.append(enemy3)
    enemyStartingX += 40

shotStatus = 0 # specifies whether the player's bullet is moving or not (1 = moving, 0 = not)

# define functions
def left():
    player.setx(player.xcor()-20)
def right():
    player.setx(player.xcor()+20)
def shoot():
    global shotStatus
    shotStatus = 1
# the distance functions check the distance between the player bullet and the enemies, the enemy bullets and the player, and the enemies and the player
def distance1(t1, t2):
    global shotStatus, score
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        enemy.ht()
        enemy.goto(0, 2000) # move off of the screen
        enemies1.remove(enemy)
        shotStatus = 0
        # update score
        score += 200
        scoreTurtle.clear()
        scoreTurtle.write(score, font = ("Impact", 40, "bold"))
def distance2(t1, t2):
    global shotStatus, score
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        enemy.ht()
        enemy.goto(0, 2000) # move off of the screen
        enemies2.remove(enemy)
        shotStatus = 0
        # update score
        score += 150
        scoreTurtle.clear()
        scoreTurtle.write(score, font = ("Impact", 40, "bold"))
def distance3(t1, t2):
    global shotStatus, score
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        enemy.ht()
        enemy.goto(0, 2000) # move off of the screen
        enemies3.remove(enemy)
        shotStatus = 0
        # update score
        score += 100
        scoreTurtle.clear()
        scoreTurtle.write(score, font = ("Impact", 40, "bold"))
def distancePlayer(t1, t2):
    global shotStatus, score, playerAlive
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        playerAlive = False
        player.ht()
        enemyShot.ht()
        player.goto(0, 2000) # move off of the screen
        shotStatus = 0
def distancePlayerEnemy(t1, t2):
    global shotStatus, score, playerAlive
    distance = m.sqrt(m.pow(t1.xcor()-t2.xcor(),2) + m.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        playerAlive = False
        player.ht()
        enemyShot.ht()
        player.goto(0, 2000) # move off of the screen
        shotStatus = 0
def ightImmaHeadOutInitializer():
    wn.onkeypress(ightImmaHeadOut, ";")
def ightImmaHeadOut():
    fontTurtle.goto(-200, 400)
    fontTurtle.write("ight imma head out", 40, font = ("Impact", 40, "normal"))

# define keypresses
wn.onkeypress(left, "a")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "d")
wn.onkeypress(right, "Right")
wn.onkeypress(shoot, "space")
wn.onkeypress(ightImmaHeadOutInitializer, "l")
wn.listen()

shotCountdown = 0 # this variable is the delay between enemy shots and also the delay between enemy movements

# initialize enemy bullet
enemyShot = trtl.Turtle(shape = shotShape)
enemyShot.speed(0)
enemyShot.seth(270)
enemyShot.pu()
enemyShot.goto(0, -1000)

enemyDirections = ["Up", "Down", "Down", "Left", "Right"] # directions the enemies can move

# reduce the speed of the enemies
for enemy in enemies1:
    enemy.speed(1)
for enemy in enemies2:
    enemy.speed(1)
for enemy in enemies3:
    enemy.speed(1)

while True:
    if playerAlive == False: # if player is dead
        break # end the while loop
    if enemies1 == [] and enemies2 == [] and enemies3 == []: #if all enemy lists are empty (all enemies are dead)
        break # end the while loop
    shotCountdown += 1
    # this if statement makes the enemies move
    if shotCountdown % 3200 == 0:
        enemyDirection = rndm.choice(enemyDirections) # choose random direction
        if enemyDirection == "Up":
            for enemy in enemies1:
                enemy.sety(enemy.ycor() + 15)
            for enemy in enemies2:
                enemy.sety(enemy.ycor() + 15)
            for enemy in enemies3:
                enemy.sety(enemy.ycor() + 15)
        if enemyDirection == "Down":
            for enemy in enemies1:
                enemy.sety(enemy.ycor() - 15)
            for enemy in enemies2:
                enemy.sety(enemy.ycor() - 15)
            for enemy in enemies3:
                enemy.sety(enemy.ycor() - 15)
        if enemyDirection == "Left":
            for enemy in enemies1:
                enemy.setx(enemy.xcor() - 15)
            for enemy in enemies2:
                enemy.setx(enemy.xcor() - 15)
            for enemy in enemies3:
                enemy.setx(enemy.xcor() - 15)
        if enemyDirection == "Right":
            for enemy in enemies1:
                enemy.setx(enemy.xcor() + 15)
            for enemy in enemies2:
                enemy.setx(enemy.xcor() + 15)
            for enemy in enemies3:
                enemy.setx(enemy.xcor() + 15)
    # this if statement makes a random enemy shoot at the player
    if shotCountdown % 3000 == 0:
        while True:
            if enemyLists != []: # if the list of enemy lists is not empty
                enemyList = rndm.choice(enemyLists) # select a random list
                if enemyList == []: # if the selected enemy list is empty
                    enemyList = rndm.choice(enemyLists) # choose another list
                else:
                    break # end the while loop (the while loop runs until a non-empty list is found, or if there isn't one it won't run at all)
            else:
                break # end the while loop (the while loop runs until a non-empty list is found, or if there isn't one it won't run at all)
        shootingEnemy = rndm.choice(enemyList) # select a random enemy from the selected list to shoot
        # move the enemy bullet to the selected enemy
        enemyShot.ht()
        enemyShot.goto(shootingEnemy.xcor(), shootingEnemy.ycor())
        enemyShot.st()
    enemyShot.fd(0.2)
    if shotStatus == 0: # if the player's bullet is not moving
        shot.goto(player.xcor(), player.ycor() + 5) # constantly move it to the player's position
    else:
        shot.fd(0.2)
    if shot.ycor() > 350: # return the bullet if it gets too high
        shotStatus = 0
    # check for collisions between objects
    for enemy in enemies1:
        distancePlayerEnemy(enemy, player)
        distance1(enemy, shot)
    for enemy in enemies2:
        distancePlayerEnemy(enemy, player)
        distance2(enemy, shot)
    for enemy in enemies3:
        distancePlayerEnemy(enemy, player)
        distance3(enemy, shot)
    distancePlayer(player, enemyShot)

if playerAlive == True: # if the player survived
    # move the bullets off of the screen
    shot.goto(1200, 0)
    enemyShot.goto(1200, 0)
    fontTurtle.goto(-300, -40)
    fontTurtle.write("YOU WIN!", font = ("Impact", 120, "bold"))
    fontTurtle.sety(fontTurtle.ycor() - 100)
if playerAlive == False: # if the player died
    # move the enemies off the screen
    for enemy in enemies1:
        enemy.ht()
    for enemy in enemies2:
        enemy.ht()
    for enemy in enemies3:
        enemy.ht()
    # move the bullets off the screen
    shot.goto(1200, 0)
    enemyShot.goto(1200, 0)
    fontTurtle.goto(-350, -40)
    fontTurtle.write("GAME OVER", font = ("Impact", 120, "bold"))

wn.mainloop()
