import arcade

arcade.open_window(600 ,600 ,'Arcade')
arcade.set_background_color(arcade.color.WHITE)
lozi_red = arcade.color.RED
lozi_blue = arcade.color.BLUE
w = 30
h = 30
center_x = 50
center_y = 500
far = 0

arcade.start_render()

for row in range(10):
    for column in range(10):
        if row % 2 ==0 :
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(center_x + far, center_y, w, h, lozi_blue, 45)
            else:
                arcade.draw_rectangle_filled(center_x + far, center_y, w, h, lozi_red, 45)    
        else:
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(center_x + far, center_y, w, h, lozi_red, 45)
            else:
                arcade.draw_rectangle_filled(center_x + far, center_y, w, h, lozi_blue, 45)   

        far+=50
    
    center_y -= 50
    far = 0     

arcade.finish_render()
arcade.run()