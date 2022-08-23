import pyglet
from objects.paddle import Paddle
from objects.ball import Ball

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()

left_player = Paddle(30, 200, pyglet.window.key.W, pyglet.window.key.S)
left_player.set_startpos(window, batch, True)

right_player = Paddle(30, 200, pyglet.window.key.UP, pyglet.window.key.DOWN)
right_player.set_startpos(window, batch, False)

players = [left_player, right_player]

ball = Ball(30, 30, 100, 200)
ball.create_bounding(window, batch)

@window.event
def on_key_press(symbol, modifiers):
    for p in players:
        p.handle_key_press(symbol)


@window.event
def on_key_release(symbol, modifiers):
    for p in players:
        p.handle_key_release(symbol)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    for p in players:
        p.update(dt, window)
    ball.update(dt, window, players)
    

pyglet.clock.schedule_interval(update, 0.001)
pyglet.app.run()