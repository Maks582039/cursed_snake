import pygame
import random
H_rect = 18
W_rect = 18
mass=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,4,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
H_mass=len(mass); W_mass=len(mass[0])

WIN_H=H_rect*H_mass; WIN_W=W_rect*W_mass
clock=pygame.time.Clock()
sc=pygame.display.set_mode((WIN_W, WIN_H))
run=True

while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            run=False
    sc.fill((255, 255, 255))
    for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    tri = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 3 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odt = [i, j]
                elif mass[i][j] == 4:
                    cht = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odn = [i, j]
    # Яблоки
    tr = True
    for i in range(H_mass):
        for j in range(W_mass):
            if mass[i][j] == 2:
                tr = False
                break
        if not(tr):
            break
    if tr:
        dedok = random.randint(0, W_mass-1)
        dedok2 = random.randint(0, H_mass-1)
        mass[dedok][dedok2] = 2
    # Движение змейки
    if odt[0] < tri[0] or odt[1] < tri[1]:
        for i in range(H_mass-1, -1, -1):
            for j in range(W_mass-1, -1, -1):
                if mass[i][j] == 3:
                    if i >= 0 and i < H_mass and mass[i-1][j] == 1:
                        mass[i+1][j] = 3
                    elif j >= 0 and j < W_mass and mass[i][j-1] == 1:
                        mass[i][j+1] = 3
                    mass[i][j] = 1
                elif mass[i][j] == 4:
                    mass[i][j] = 0
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    mass[i][j] = 4
    else:
        for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    if i < H_mass and i >= 0 and mass[i+1][j] == 1:
                        mass[i-1][j] = 3
                    elif j < W_mass and j >= 0 and mass[i][j+1] == 1:
                        mass[i][j-1] = 3
                    mass[i][j] = 1
                elif mass[i][j] == 4:
                    mass[i][j] = 0
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    mass[i][j] = 4
    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    tri = [i, j]
                elif mass[i][j] == 4:
                    cht = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odn = [i, j]
        if tri[0] < H_mass and tri[0] >= 0 and (mass[tri[0]+1][tri[1]] == 0 or mass[tri[0]+1][tri[1]] == 2):
            mass[tri[0]+1][tri[1]] = 3
        mass[tri[0]][tri[1]] = 1
        mass[cht[0]][cht[1]] = 0
        mass[odn[0]][odn[1]] = 4
    elif keys[pygame.K_d]:
        for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    tri = [i, j]
                elif mass[i][j] == 4:
                    cht = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odn = [i, j]
        if tri[0] < H_mass and tri[0] >= 0 and (mass[tri[0]][tri[1]+1] == 0 or mass[tri[0]][tri[1]+1] == 2):
            mass[tri[0]][tri[1]+1] = 3
        mass[tri[0]][tri[1]] = 1
        mass[cht[0]][cht[1]] = 0
        mass[odn[0]][odn[1]] = 4
    elif keys[pygame.K_a]:
        for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    tri = [i, j]
                elif mass[i][j] == 4:
                    cht = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odn = [i, j]
        if tri[1] < H_mass and tri[1] >= 0 and (mass[tri[0]][tri[1]-1] == 0 or mass[tri[0]][tri[1]-1] == 2):
            mass[tri[0]][tri[1]-1] = 3
        mass[tri[0]][tri[1]] = 1
        mass[cht[0]][cht[1]] = 0
        mass[odn[0]][odn[1]] = 4
    elif keys[pygame.K_w]:
        for i in range(H_mass):
            for j in range(W_mass):
                if mass[i][j] == 3:
                    tri = [i, j]
                elif mass[i][j] == 4:
                    cht = [i, j]
                elif j < W_mass and j >= 0 and i < H_mass and i >= 0 and mass[i][j] == 1 and 4 in [mass[i+1][j], mass[i-1][j], mass[i][j+1], mass[i][j-1]]:
                    odn = [i, j]
        if tri[0] < H_mass and tri[0] >= 0 and (mass[tri[0]-1][tri[1]] == 0 or mass[tri[0]-1][tri[1]] == 2):
            mass[tri[0]-1][tri[1]] = 3
        mass[tri[0]][tri[1]] = 1
        mass[cht[0]][cht[1]] = 0
        mass[odn[0]][odn[1]] = 4
    # Отрисовывание змейки
    for i in range(H_mass):
        for j in range(W_mass):
            if mass[i][j] == 1:
                pygame.draw.rect(sc, (0, 255, 0), (j*W_rect, i*H_rect, W_rect, H_rect))
            elif mass[i][j] == 2:
                pygame.draw.rect(sc, (255, 0, 0), (j*W_rect, i*H_rect, W_rect, H_rect))
            elif mass[i][j] == 3:
                pygame.draw.rect(sc, (0, 200, 0), (j*W_rect, i*H_rect, W_rect, H_rect))
            elif mass[i][j] == 4:
                pygame.draw.rect(sc, (0, 100, 0), (j*W_rect, i*H_rect, W_rect, H_rect))
    pygame.display.update()
    clock.tick(5)
pygame.quit()