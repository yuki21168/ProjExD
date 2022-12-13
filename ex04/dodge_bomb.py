import pygame as pg
import random
import sys
import tkinter.messagebox as tkm
import tkinter as tk


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko, tate

def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    tori_sfc2 = pg.image.load("fig/5.png")
    tori_sfc2 = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct2 = tori_sfc.get_rect()
    tori_rct2.center = 700, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc2, tori_rct2)

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    #爆弾を増やす
    bomb_sfc2 = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc2, (255, 0, 255), (30, 30), 30)
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct2.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
    vx2, vy2 = +1, +1

    bomb_sfc3 = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc3.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc3, (255, 255, 0), (50, 50), 50)
    bomb_rct3 = bomb_sfc3.get_rect()
    bomb_rct2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct2.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc3, bomb_rct3) 
    vx3, vy3 = +1, +1

    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        #爆弾増やす
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
        yoko, tate = check_bound(bomb_rct2, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        #爆弾増やす
        bomb_rct3.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb_sfc3, bomb_rct3) 
        yoko, tate = check_bound(bomb_rct3, scrn_rct)
        vx3 *= yoko
        vy3 *= tate

        # 練習８
        #爆弾にあたるとメッセージが出る
        if tori_rct.colliderect(bomb_rct):
                    root = tk.Tk()
                    root.withdraw()
                    tkm.showinfo("ドンマイ","Game Over")#コメントを表示
                    return
        elif tori_rct.colliderect(bomb_rct2):
                    root = tk.Tk()
                    root.withdraw()
                    tkm.showinfo("ドンマイ","Game Over")#コメントを表示
                    return
        elif tori_rct.colliderect(bomb_rct2):
                    root = tk.Tk()
                    root.withdraw()
                    tkm.showinfo("ドンマイ","Game Over")#コメントを表示
                    return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()