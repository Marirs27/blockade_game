import pygame
from pygame.locals import *
from random import randint

#variables
white = [255,255,255]
border_color = [0,75,102]
bg_color = [0,0,0]
size = [900,700]
block_colors = [
    [51,255,255],
    [51,153,255],
    [255,153,51],
    [255,255,51],
    [51,255,51],
    [255,51,255],
    [255,51,51]
]
running = True
base = [[0]*20 for i in range(20)]
base_color = [[0]*20 for i in range(20)]
# base = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]]
# base_color = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 6, 0, 0, 0, 0, 0, 5, 5, 5], [3, 3, 3, 3, 0, 5, 6, 6, 2, 2, 5, 6, 6, 5, 0, 0, 4, 4, 5, 2]]
start_x = 35
start_y = 45
block_size = 30
block_separation = 3
FPS = 1
score = 0
block_count = 0
level = 0
speed = 200

def set_play_screen():
    screen = pygame.display.set_mode(size)
    screen.fill(white)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont('algerian', 25)
    font_body = pygame.font.SysFont('algerian', 20)

    #set border and separation
    pygame.draw.rect(screen,border_color,Rect(0,0,900,700))
    pygame.draw.rect(screen,bg_color,Rect(6,10,688,681),0,3)
    pygame.draw.rect(screen,white,Rect(702,12,190,680),3,3)
    pygame.draw.rect(screen,white,Rect(721,31,151,100),1,3)
    pygame.draw.rect(screen,white,Rect(721,190,151,200),1,3)
    pygame.draw.rect(screen,white,Rect(721,469,151,200),1,3)

    pygame.draw.rect(screen,white,Rect(732,40,129,40),1,3)
    text = font.render('SCORE', True, white, border_color)
    text_box = Rect(757,46,146,20)
    screen.blit(text,text_box)
    for i in range(5):
        block = Rect(729+(27*i),90,26,26)
        pygame.draw.rect(screen,bg_color,block,0,3)
        text = font.render('0', True, white, bg_color)
        text_block = Rect(735+(27*i),89,26,26)
        screen.blit(text,text_block)

    pygame.draw.rect(screen,white,Rect(732,199,129,40),1,3)
    text = font.render('CONTROLS', True, white, border_color)
    text_box = Rect(737,205,146,20)
    screen.blit(text,text_box)
    text = font_body.render('SPACE - Pause', True, white, border_color)
    text_box = Rect(726,265,146,20)
    screen.blit(text,text_box)
    text = font_body.render('RIGHT  - RIGHT', True, white, border_color)
    text_box = Rect(726,285,146,20)
    screen.blit(text,text_box)
    text = font_body.render('LEFT    - LEFT', True, white, border_color)
    text_box = Rect(726,305,146,20)
    screen.blit(text,text_box)
    text = font_body.render('DOWN   - SPEED', True, white, border_color)
    text_box = Rect(726,325,146,20)
    screen.blit(text,text_box)
    text = font_body.render('UP      - ROTATE', True, white, border_color)
    text_box = Rect(726,345,146,20)
    screen.blit(text,text_box)

    pygame.draw.rect(screen,white,Rect(732,478,129,40),1,3)
    text = font.render('NEXT UP', True, white, border_color)
    text_box = Rect(747,484,146,20)
    screen.blit(text,text_box)

    pygame.display.update()
    return screen,clock

def generate_block(): 
    shape_pos = [    
        [[8,1],[9,1],[10,1],[11,1]],
        [[8,0],[8,1],[9,1],[10,1]],
        [[8,1],[9,1],[10,1],[10,0]],
        [[8,0],[8,1],[9,1],[9,0]],
        [[8,1],[9,1],[9,0],[10,0]],
        [[9,0],[8,1],[9,1],[10,1]],
        [[8,0],[9,0],[9,1],[10,1]]
    ]
    index = randint(0,len(shape_pos)-1)
    return shape_pos[index],index

def draw_block(pos):
    block = []
    for p in pos:
        block.append(Rect(start_x+p[0]*(block_size+block_separation),start_y+p[1]*(block_size+block_separation),block_size,block_size))
    return block

def update_block_center(block,pos):
    for i in range(len(pos)):
        block[i].center = [start_x+pos[i][0]*(block_size+block_separation),start_y+pos[i][1]*(block_size+block_separation)]

def update_pos(pos,inc):
    for p in pos:
        p[0] += inc[0]
        p[1] += inc[1]
    return pos

def move_block(screen,block,color,clock,FPS):
    for unit in block:
        pygame.draw.rect(screen,color,unit,0,3)
        pygame.display.update(unit)
    pygame.time.delay(speed)
    for unit in block:
        pygame.draw.rect(screen,bg_color,unit,0,3)
        pygame.display.update(unit)

def freeze_block(screen,block,color):
    for unit in block:
        pygame.draw.rect(screen,color,unit,0,3)
        pygame.display.update(unit)

def is_stackable(pos):
    for p in pos:
        if not (p[1] < 19 and base[p[1]+1][p[0]] == 0) :
            return False
    return True
        
def populate_base(base,base_color,index,pos):
    for p in pos:
        base[p[1]][p[0]] = 1
        base_color[p[1]][p[0]] = index
    return base,base_color

def reset_block():
    pos,index = generate_block()
    return draw_block(pos),index,pos,len(pos)//2,1

def is_collision(base,pos,inc):
    for p in pos:
        x_pos = p[0]+inc[0]
        y_pos = p[1]+inc[1]
        # Check for borders
        if not (x_pos>=0 and x_pos<20) or not (y_pos>=-1 and y_pos<20):
            return True
        # Check for collition
        elif base[y_pos][x_pos] == 1:
            return True
    return False

def rotate_block(pos,median):
    rotated_pos = []
    med = pos[median]
    for i in range(len(pos)):
        new = []
        x = med[0]-pos[i][0]
        y = med[1]-pos[i][1]
        new.append(pos[i][0]+(x-y))
        new.append(pos[i][1]+(x+y))
        rotated_pos.append(new)
    return rotated_pos

def display_game_over(screen,clock):
    border_box = Rect(200,250,300,100)
    box = Rect(210,260,280,80)
    text_box = Rect(250,280,150,100)
    running = True

    while running:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                running = False
                break
        if running == False:
            break
        pygame.draw.rect(screen,white,border_box)
        pygame.draw.rect(screen,bg_color,box)
        font = pygame.font.SysFont('algerian', 35)
        text = font.render('GAME OVER!', True, block_colors[6], bg_color)
        screen.blit(text,text_box)
        pygame.display.update()
        clock.tick(1)
        text = font.render('GAME OVER!', True, bg_color, bg_color)
        screen.blit(text,text_box)
        pygame.display.update()
        clock.tick(1)

def pause_screen(screen):
    border_box = Rect(200,250,300,140)
    box = Rect(205,255,290,130)
    title_box = Rect(285,265,150,100)
    body_box_1 = Rect(250,320,150,100)
    body_box_2 = Rect(295,350,150,100)
    pausing = True
    running = True
    while pausing:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pausing = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausing = False
        pygame.draw.rect(screen,white,border_box)
        pygame.draw.rect(screen,bg_color,box)
        font = pygame.font.SysFont('algerian', 35)
        font_body = pygame.font.SysFont('algerian', 20)
        text = font.render('PAUSED', True, border_color, bg_color)
        screen.blit(text,title_box)
        text = font_body.render('PRESS SPACE AGAIN', True, border_color, bg_color)
        screen.blit(text,body_box_1)
        text = font_body.render('TO RESUME', True, border_color, bg_color)
        screen.blit(text,body_box_2)
        pygame.display.update()

    pygame.draw.rect(screen,bg_color,border_box)
    pygame.display.update()
    return running    

def check_for_level_clear(base,base_color):
    l = len(base)
    blank_index = False
    for i in range(l):
        if sum(base[i]) == l:
            blank_index = i
            new_b = [[0 for _ in range(l)]]
            new_c = [[0 for _ in range(l)]]
            new_base = [base[w] for w in range(l) if w != i]
            new_b.extend(new_base)
            base = new_b.copy()
            new_base_color = [base_color[w] for w in range(l) if w != i]
            new_c.extend(new_base_color)
            base_color = new_c.copy()
    return base,base_color,blank_index

def render_screen(screen,base,base_color,blank_index):
    start = 0
    x = start_x-(block_size//2)
    y = start_y-(block_size//2)
    pygame.draw.rect(screen,bg_color,Rect(6,10,688,681),0,3)
    pygame.display.update()
    if blank_index:
        l = len(base[0])
        blank = [0 for i in range(l)]
        new_base = []
        new_color = []
        for i in range(1,l):
            new_base.append(base[i])
            new_color.append(base_color[i])
            if i == blank_index:
                new_base.append(blank)
                new_color.append(blank)
        base = new_base.copy()
        base_color = new_color.copy()
    for i in range(len(base)):
        for j in range(len(base[i])):
            if base[i][j] == 1:
                unit = Rect(x+(j)*(block_size+block_separation),y+(i)*(block_size+block_separation),block_size,block_size)
                pygame.draw.rect(screen,block_colors[base_color[i][j]],unit,0,3)
                pygame.display.update(unit)

def display_next_block(screen,temp_index,temp_pos):
    horizonatal_spread = len(set([temp_pos[0][0],temp_pos[1][0],temp_pos[2][0],temp_pos[3][0]]))
    if horizonatal_spread == 4:
        adjustment = [13.13,15]
    elif horizonatal_spread == 3:
        adjustment = [13.65,15.6] 
    elif horizonatal_spread == 2:
        adjustment = [14.13,15.6] 
    temp_pos = [[p[0]+adjustment[0],p[1]+adjustment[1]] for p in temp_pos]
    block = draw_block(temp_pos)
    pygame.draw.rect(screen,border_color,Rect(730,520,140,140),0,3)
    pygame.time.delay(speed)
    for unit in block:
        pygame.draw.rect(screen,block_colors[temp_index],unit,0,3)
    pygame.display.update()

def refresh_score(screen,score,display_score_prev):
    digits = len(str(score))
    display_score = ['0' for _ in range(5-digits)]
    display_score.extend([i for i in str(score)])

    font = pygame.font.SysFont('algerian', 25)
    for i in range(5):
        if display_score[i] != display_score_prev[i]:
            block = Rect(729+(27*i),90,26,26)
            pygame.draw.rect(screen,bg_color,block,0,3)
            pygame.display.update(block)
            text = font.render(display_score[i], True, white, bg_color)
            text_block = Rect(735+(27*i),89,26,26)
            screen.blit(text,text_block)
    return display_score          

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('BLOCKADE')
    screen,clock = set_play_screen()
    pos,index = generate_block()
    next_pos,next_index = generate_block()
    block = draw_block(pos)
    median = len(pos)//2
    display_next_block(screen,next_index,next_pos)
    display_score_prev = ['0','0','0','0','0']
    render_screen(screen,base,base_color,False)
    while running:
        FPS = 1
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = pause_screen(screen)
                if event.key == pygame.K_LEFT:
                    if not is_collision(base,pos,[-1,0]):
                        pos = update_pos(pos,[-1,0]).copy()
                elif event.key == pygame.K_RIGHT:
                    if not is_collision(base,pos,[1,0]):
                        pos = update_pos(pos,[1,0]).copy()
                elif event.key == pygame.K_DOWN:
                    if not is_collision(base,pos,[0,1]):
                        pos = update_pos(pos,[0,1]).copy()
                elif event.key == pygame.K_UP:
                    rotated_pos = rotate_block(pos,median)
                    if not is_collision(base,rotated_pos,[0,0]):
                        pos = rotated_pos
                FPS = 0
        if running == False:
            break
        update_block_center(block,pos)
        if (is_collision(base,pos,[0,0])):
            display_game_over(screen,clock)
            break
        move_block(screen,block,block_colors[index],clock,FPS)
        if is_stackable(pos):
            if FPS == 1:
                pos = update_pos(pos,[0,1]).copy()
        else:
            freeze_block(screen,block,block_colors[index])
            score += 25
            block_count += 1
            if block_count%5 == 0:
                level += 1
                if speed > 500:
                    speed -= 100
                elif speed > 100:
                    speed -= 50
            base,base_color = populate_base(base,base_color,index,pos)
            base,base_color,blank_index = check_for_level_clear(base,base_color)
            if blank_index:
                score += 100
                render_screen(screen,base,base_color,blank_index)
                pygame.time.delay(300)
                render_screen(screen,base,base_color,False)
            pos = [p for p in next_pos]
            index = next_index
            block,next_index,next_pos,median,flipper = reset_block()
            display_score_prev = refresh_score(screen,score,display_score_prev).copy()
            display_next_block(screen,next_index,next_pos)
    pygame.display.update()
    pygame.quit()
