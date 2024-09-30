from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events():
    global running,act
    global dirx, diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx+=1
                act = 1
            elif event.key == SDLK_LEFT:
                dirx-=1
                act = 2
            if event.key == SDLK_UP:
                diry += 1
                act = 0
            elif event.key == SDLK_DOWN:
                diry -= 1
                act = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx-=1
            elif event.key == SDLK_LEFT:
                dirx+=1
            if event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
        # fill here


running = True
act = 0
x = 800 // 2
y = 600 // 2
frame = 0
dirx = 0
diry = 0

while running:
    clear_canvas()
    grass.draw(400, 300)
    character.clip_draw(frame*60,act*60,60,60,x,y,150,150)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    delay(0.05)

close_canvas()

