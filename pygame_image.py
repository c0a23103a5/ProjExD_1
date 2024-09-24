import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_f = pg.transform.flip(bg_img, True, False)#練習7
    pl_img = pg.image.load("fig/3.png")#練習2
    pl_img = pg.transform.flip(pl_img, True, False)#練習2
    pl_rct = pl_img.get_rect()#練習8-1　rectオブジェクトの取得
    pl_rct.center = (300, 200)#練習8-2　rectを使った初期座標の設定


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #キーボード入力
        key_lst = pg.key.get_pressed()#練習8-2　キーリストの取得
        dx, dy = 0, 0
        if key_lst[pg.K_UP]:
            dy = -1
        if key_lst[pg.K_DOWN]:
            dy = 1
        if key_lst[pg.K_LEFT]:
            dx = -1
        if key_lst[pg.K_RIGHT]:
            dx = 2#演習1　右へ倍速で移動

        pl_rct.move_ip((dx, dy))#演習2

        #背景表示
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])#練習6
        screen.blit(bg_img_f, [x+1600, 0])#練習7

        screen.blit(bg_img, [x+3200, 0])#練習7
        screen.blit(bg_img_f, [x+4800, 0])#練習7

        #プレイヤー機表示
        pl_rct.move_ip((-1, 0))#演習1　非操作時、左に流れる
        screen.blit(pl_img, pl_rct) #練習4
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()