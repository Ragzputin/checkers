#!/usr/bin/python
from Tkinter import *
import tkMessageBox


class CheckerBoard(Frame):

    def __init__(self, parent, icoord, prev_itm, moves, illegal, gnum, rnum, is_moved, ocrowns, gcrowns):
        Frame.__init__(self,parent)

        self.parent = parent
        self.icoord = icoord
        self.prev_itm = prev_itm
        self.moves = moves
        self.illegal = illegal
        self.gnum = gnum
        self.rnum = rnum
        self.is_moved = is_moved
        self.ocrowns = ocrowns
        self.gcrowns = gcrowns

        self.InitUI()

    def InitUI(self):

        self.parent.title("Let's play Checkers!")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self,bg="CadetBlue1")

        drag_data = {"x": 0, "y": 0, "item": None}
        init_data = {"x": 0, "y": 0, "item": None}
        final_coord = [0,0]


        #---------------------
        #COLUMN 1
        #---------------------
        re1 = canvas.create_rectangle(40, 30, 90, 80, outline="tomato", fill="tomato", tags="red")
        bl2 = canvas.create_rectangle(40, 80, 90, 130, outline="black", fill="black", tags="black")
        re3 = canvas.create_rectangle(40, 130, 90, 180, outline="tomato", fill="tomato", tags="red")
        bl4 = canvas.create_rectangle(40, 180, 90, 230, outline="black", fill="black", tags="black")
        re5 = canvas.create_rectangle(40, 230, 90, 280, outline="tomato", fill="tomato", tags="red")
        bl6 = canvas.create_rectangle(40, 280, 90, 330, outline="black", fill="black", tags="black")
        re7 = canvas.create_rectangle(40, 330, 90, 380, outline="tomato", fill="tomato", tags="red")
        bl8 = canvas.create_rectangle(40, 380, 90, 430, outline="black", fill="black", tags="black")

        #---------------------
        #COLUMN 2
        #---------------------
        bl9 = canvas.create_rectangle(90, 30, 140, 80, outline="black", fill="black", tags="black")
        re10 = canvas.create_rectangle(90, 80, 140, 130, outline="tomato", fill="tomato", tags="red")
        bl11 = canvas.create_rectangle(90, 130, 140, 180, outline="black", fill="black", tags="black")
        re12 = canvas.create_rectangle(90, 180, 140, 230, outline="tomato", fill="tomato", tags="red")
        bl13 = canvas.create_rectangle(90, 230, 140, 280, outline="black", fill="black", tags="black")
        re14 = canvas.create_rectangle(90, 280, 140, 330, outline="tomato", fill="tomato", tags="red")
        bl15 = canvas.create_rectangle(90, 330, 140, 380, outline="black", fill="black", tags="black")
        re16 = canvas.create_rectangle(90, 380, 140, 430, outline="tomato", fill="tomato", tags="red")

        #---------------------
        #COLUMN 3
        #---------------------
        re17 = canvas.create_rectangle(140, 30, 190, 80, outline="tomato", fill="tomato", tags="red")
        bl18 = canvas.create_rectangle(140, 80, 190, 130, outline="black", fill="black", tags="black")
        re19 = canvas.create_rectangle(140, 130, 190, 180, outline="tomato", fill="tomato", tags="red")
        bl20 = canvas.create_rectangle(140, 180, 190, 230, outline="black", fill="black", tags="black")
        re21 = canvas.create_rectangle(140, 230, 190, 280, outline="tomato", fill="tomato", tags="red")
        bl22 = canvas.create_rectangle(140, 280, 190, 330, outline="black", fill="black", tags="black")
        re23 = canvas.create_rectangle(140, 330, 190, 380, outline="tomato", fill="tomato", tags="red")
        bl24 = canvas.create_rectangle(140, 380, 190, 430, outline="black", fill="black", tags="black")

        #---------------------
        #COLUMN 4
        #---------------------
        bl25 = canvas.create_rectangle(190, 30, 240, 80, outline="black", fill="black", tags="black")
        re26 = canvas.create_rectangle(190, 80, 240, 130, outline="tomato", fill="tomato", tags="red")
        bl27 = canvas.create_rectangle(190, 130, 240, 180, outline="black", fill="black", tags="black")
        re28 = canvas.create_rectangle(190, 180, 240, 230, outline="tomato", fill="tomato", tags="red")
        bl29 = canvas.create_rectangle(190, 230, 240, 280, outline="black", fill="black", tags="black")
        re30 = canvas.create_rectangle(190, 280, 240, 330, outline="tomato", fill="tomato", tags="red")
        bl31 = canvas.create_rectangle(190, 330, 240, 380, outline="black", fill="black", tags="black")
        re32 = canvas.create_rectangle(190, 380, 240, 430, outline="tomato", fill="tomato", tags="red")

        #---------------------
        #COLUMN 5
        #---------------------
        re33 = canvas.create_rectangle(240, 30, 290, 80, outline="tomato", fill="tomato", tags="red")
        bl34 = canvas.create_rectangle(240, 80, 290, 130, outline="black", fill="black", tags="black")
        re35 = canvas.create_rectangle(240, 130, 290, 180, outline="tomato", fill="tomato", tags="red")
        bl36 = canvas.create_rectangle(240, 180, 290, 230, outline="black", fill="black", tags="black")
        re37 = canvas.create_rectangle(240, 230, 290, 280, outline="tomato", fill="tomato", tags="red")
        bl38 = canvas.create_rectangle(240, 280, 290, 330, outline="black", fill="black", tags="black")
        re39 = canvas.create_rectangle(240, 330, 290, 380, outline="tomato", fill="tomato", tags="red")
        bl40 = canvas.create_rectangle(240, 380, 290, 430, outline="black", fill="black", tags="black")

        #---------------------
        #COLUMN 6
        #---------------------
        bl41 = canvas.create_rectangle(290, 30, 340, 80, outline="black", fill="black", tags="black")
        re42 = canvas.create_rectangle(290, 80, 340, 130, outline="tomato", fill="tomato", tags="red")
        bl43 = canvas.create_rectangle(290, 130, 340, 180, outline="black", fill="black", tags="black")
        re44 = canvas.create_rectangle(290, 180, 340, 230, outline="tomato", fill="tomato", tags="red")
        bl45 = canvas.create_rectangle(290, 230, 340, 280, outline="black", fill="black", tags="black")
        re46 = canvas.create_rectangle(290, 280, 340, 330, outline="tomato", fill="tomato", tags="red")
        bl47 = canvas.create_rectangle(290, 330, 340, 380, outline="black", fill="black", tags="black")
        re48 = canvas.create_rectangle(290, 380, 340, 430, outline="tomato", fill="tomato", tags="red")

        #---------------------
        #COLUMN 7
        #---------------------
        re49 = canvas.create_rectangle(340, 30, 390, 80, outline="tomato", fill="tomato", tags="red")
        bl50 = canvas.create_rectangle(340, 80, 390, 130, outline="black", fill="black", tags="black")
        re51 = canvas.create_rectangle(340, 130, 390, 180, outline="tomato", fill="tomato", tags="red")
        bl52 = canvas.create_rectangle(340, 180, 390, 230, outline="black", fill="black", tags="black")
        re53 = canvas.create_rectangle(340, 230, 390, 280, outline="tomato", fill="tomato", tags="red")
        bl54 = canvas.create_rectangle(340, 280, 390, 330, outline="black", fill="black", tags="black")
        re55 = canvas.create_rectangle(340, 330, 390, 380, outline="tomato", fill="tomato", tags="red")
        bl56 = canvas.create_rectangle(340, 380, 390, 430, outline="black", fill="black", tags="black")

        #---------------------
        #COLUMN 8
        #---------------------
        bl57 = canvas.create_rectangle(390, 30, 440, 80, outline="black", fill="black", tags="black")
        re58 = canvas.create_rectangle(390, 80, 440, 130, outline="tomato", fill="tomato", tags="red")
        bl59 = canvas.create_rectangle(390, 130, 440, 180, outline="black", fill="black", tags="black")
        re60 = canvas.create_rectangle(390, 180, 440, 230, outline="tomato", fill="tomato", tags="red")
        bl61 = canvas.create_rectangle(390, 230, 440, 280, outline="black", fill="black", tags="black")
        re62 = canvas.create_rectangle(390, 280, 440, 330, outline="tomato", fill="tomato", tags="red")
        bl63 = canvas.create_rectangle(390, 330, 440, 380, outline="black", fill="black", tags="black")
        re64 = canvas.create_rectangle(390, 380, 440, 430, outline="tomato", fill="tomato", tags="red")


        def OnTokenButtonPress(event):
            # record the item and its location
            drag_data["item"] = canvas.find_closest(event.x, event.y)[0]
            drag_data["x"] = event.x
            drag_data["y"] = event.y


            init_data["item"] = drag_data["item"]
            init_data["x"] = drag_data["x"]
            init_data["y"] = drag_data["y"]

            item_below = canvas.find_overlapping(event.x,event.y,event.x,event.y)[0]
            self.icoord = ColumnRowCoords(item_below)


        def OnTokenButtonRelease(event):
            # reset the drag information
            drag_data["item"] = None
            drag_data["x"] = 0
            drag_data["y"] = 0

        def OnTokenMotion(event):
            # compute how much this object has moved
            delta_x = event.x - drag_data["x"]
            delta_y = event.y - drag_data["y"]

            # move the object the appropriate amount
            canvas.move(drag_data["item"], delta_x, delta_y)
            # record the new position
            drag_data["x"] = event.x
            drag_data["y"] = event.y

        def ColumnRowCoords(objID):
            coord = []

            #Configuring column coordinate:
            if objID > 0 and objID < 9:
                coord.append(1)
            elif objID >= 9 and objID < 17:
                coord.append(2)
            elif objID >= 17 and objID < 25:
                coord.append(3)
            elif objID >= 25 and objID < 33:
                coord.append(4)
            elif objID >= 33 and objID < 41:
                coord.append(5)
            elif objID >= 41 and objID < 49:
                coord.append(6)
            elif objID >= 49 and objID < 57:
                coord.append(7)
            else:
                coord.append(8)

            #Configuring row coordinate:
            if objID % 8 == 0:
                coord.append(8)
            elif objID % 8 == 1:
                coord.append(1)
            elif objID % 8 == 2:
                coord.append(2)
            elif objID % 8 == 3:
                coord.append(3)
            elif objID % 8 == 4:
                coord.append(4)
            elif objID % 8 == 5:
                coord.append(5)
            elif objID % 8 == 6:
                coord.append(6)
            elif objID % 8 == 7:
                coord.append(7)

            return coord

        def RectDims(coords):
            dims = []
            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0
            i = 1

            #while loop to configure dimensions
            while i < 9:
                #Configuring X-coordinates
                if coords[0] == i:
                    if i == 1:
                        x1 = 40
                        x2 = 90
                    elif i == 2:
                        x1 = 90
                        x2 = 140
                    elif i == 3:
                        x1 = 140
                        x2 = 190
                    elif i == 4:
                        x1 = 190
                        x2 = 240
                    elif i == 5:
                        x1 = 240
                        x2 = 290
                    elif i == 6:
                        x1 = 290
                        x2 = 340
                    elif i == 7:
                        x1 = 340
                        x2 = 390
                    elif i == 8:
                        x1 = 390
                        x2 = 440

                #Configuring X-coordinates
                if coords[1] == i:
                    if i == 1:
                        y1 = 30
                        y2 = 80
                    elif i == 2:
                        y1 = 80
                        y2 = 130
                    elif i == 3:
                        y1 = 130
                        y2 = 180
                    elif i == 4:
                        y1 = 180
                        y2 = 230
                    elif i == 5:
                        y1 = 230
                        y2 = 280
                    elif i == 6:
                        y1 = 280
                        y2 = 330
                    elif i == 7:
                        y1 = 330
                        y2 = 380
                    elif i == 8:
                        y1 = 380
                        y2 = 430
                i += 1

            dims.append(x1)
            dims.append(y1)
            dims.append(x2)
            dims.append(y2)

            return dims
        """
        def CenterPieces(dims,x,y):
            cent_x = dims[0] + 25
            cent_y = dims[1] + 25
            del_x = abs(x - cent_x)
            del_y = abs(y - cent_y)

            if x >= dims[0] and x < dims[2] and y >= dims[1] and y < dims[3]:
                if x < cent_x and y < cent_y:
                    canvas.move(init_data["item"],del_x,del_y)
                elif x < cent_x and y > cent_y:
                    canvas.move(init_data["item"],del_x,-1*del_y)
                elif x > cent_x and y < cent_y:
                    canvas.move(init_data["item"],-1*del_x,del_y)
                else:
                    canvas.move(init_data["item"],-1*del_x,-1*del_y)
        """

        #------------------------
        #Initializing Gray pieces
        #------------------------
        #Column 1:
        #40, 80, 90, 130
        g1 = canvas.create_oval(50,90,80,120, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #40, 180, 90, 230
        g2 = canvas.create_oval(50,190,80,220, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #40, 280, 90, 330
        g3 = canvas.create_oval(50,290,80,320, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #40, 380, 90, 430
        g4 = canvas.create_oval(50,390,80,420, outline="SlateGray4", fill="SlateGray4", tags="oval")

        #Column 2:
        #90, 30, 140, 80
        g5 = canvas.create_oval(100,40,130,70, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #90, 130, 140, 180
        g6 = canvas.create_oval(100,140,130,170, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #90, 230, 140, 280
        g7 = canvas.create_oval(100,240,130,270, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #90, 330, 140, 380
        g8 = canvas.create_oval(100,340,130,370, outline="SlateGray4", fill="SlateGray4", tags="oval")

        #Column 3:
        #140, 80, 190, 130
        g9 = canvas.create_oval(150,90,180,120, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #140, 180, 190, 230
        g10 = canvas.create_oval(150,190,180,220, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #140, 280, 190, 330
        g11 = canvas.create_oval(150,290,180,320, outline="SlateGray4", fill="SlateGray4", tags="oval")
        #140, 380, 190, 430
        g12 = canvas.create_oval(150,390,180,420, outline="SlateGray4", fill="SlateGray4", tags="oval")

        #------------------------
        #Initializing Red pieces
        #------------------------
        #Column 6:
        #290, 30, 340, 80
        r1 = canvas.create_oval(300,40,330,70, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #290, 130, 340, 180
        r2 = canvas.create_oval(300,140,330,170, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #290, 230, 340, 280
        r3 = canvas.create_oval(300,240,330,270, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #290, 330, 340, 380
        r4 = canvas.create_oval(300,340,330,370, outline="OrangeRed2", fill="OrangeRed2", tags="oval")

        #Column 7:
        #340, 80, 390, 130
        r5 = canvas.create_oval(350,90,380,120, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #340, 180, 390, 230
        r6 = canvas.create_oval(350,190,380,220, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #340, 280, 390, 330
        r7 = canvas.create_oval(350,290,380,320, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #340, 380, 390, 430
        r8 = canvas.create_oval(350,390,380,420, outline="OrangeRed2", fill="OrangeRed2", tags="oval")

        #Column 8:
        #390, 30, 440, 80
        r9 = canvas.create_oval(400,40,430,70, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #390, 130, 440, 180
        r10 = canvas.create_oval(400,140,430,170, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #390, 230, 440, 280
        r11 = canvas.create_oval(400,240,430,270, outline="OrangeRed2", fill="OrangeRed2", tags="oval")
        #390, 330, 440, 380
        r12 = canvas.create_oval(400,340,430,370, outline="OrangeRed2", fill="OrangeRed2", tags="oval")

        def PieceLogic(event):
            if self.is_moved == True:
                self.is_moved = False

            OnTokenButtonRelease(event)
            bl_tags = canvas.find_withtag("black")
            cur_itm = canvas.find_closest(event.x,event.y)[0]
            item_below = canvas.find_overlapping(event.x,event.y,event.x,event.y)[0]
            itm_tuple = canvas.find_overlapping(event.x,event.y,event.x,event.y)

            final_coord = ColumnRowCoords(item_below)

            row_diff = abs(final_coord[1] - self.icoord[1])
            col_diff = abs(final_coord[0] - self.icoord[0])

            same_colour = False
            if ((self.prev_itm > 64 and self.prev_itm < 77) and (cur_itm > 64 and cur_itm < 77)) \
                    and self.illegal != True:
                same_colour = True
                tkMessageBox.showinfo(title=None, message="Orange's Turn!")
                if self.is_moved != True:
                    delta_x = init_data["x"] - event.x
                    delta_y = init_data["y"] - event.y
                    canvas.move(init_data["item"],delta_x,delta_y)
                    self.is_moved = True


            elif ((self.prev_itm > 76 and self.prev_itm < 90) and (cur_itm > 76 and cur_itm < 90)) \
                    and self.illegal != True:
                same_colour = True
                tkMessageBox.showinfo(title=None, message="Gray's Turn!")
                if self.is_moved != True:
                    delta_x = init_data["x"] - event.x
                    delta_y = init_data["y"] - event.y
                    canvas.move(init_data["item"],delta_x,delta_y)
                    self.is_moved = True


            for item in bl_tags:
                if item == item_below and len(itm_tuple) == 2 and row_diff > 0 and col_diff > 0:
                    sq_dims = RectDims(final_coord)
                    self.moves += 1
                    print "Moves: ", self.moves
                    if final_coord[0] == 1 and cur_itm > 76 and same_colour != True:
                        canvas.itemconfig(cur_itm,fill="OrangeRed4",outline="OrangeRed4")
                        self.ocrowns.append(cur_itm)
                        print "self.ocrowns: ", self.ocrowns
                    elif final_coord[0] == 8 and cur_itm < 77 and same_colour != True:
                        canvas.itemconfig(cur_itm,fill="gray25",outline="gray25")
                        self.gcrowns.append(cur_itm)
                        print "self.gcrowns: ", self.gcrowns

                    gcrn_itm = 0
                    for i in self.gcrowns:
                        if i == cur_itm and same_colour != True:
                            gcrn_itm = i
                            break

                    print
                    print "gcrn_itm: ", gcrn_itm

                    ocrn_itm = 0
                    for i in self.ocrowns:
                        if i == cur_itm and same_colour != True:
                            ocrn_itm = i
                            break

                    print
                    print "ocrn_itm: ", ocrn_itm

                    if col_diff == 2 and row_diff == 2 and self.moves > 1:
                        dpiece_coord = []
                        dpiececol = 0
                        dpiecerow = 0
                        self.prev_itm = cur_itm
                        if final_coord[0] > self.icoord[0] and final_coord[1] > self.icoord[1]:
                            if cur_itm < 77 or ocrn_itm == cur_itm:
                                dpiececol = self.icoord[0] + 1
                                dpiecerow = self.icoord[1] + 1
                                dpiece_coord.append(dpiececol)
                                dpiece_coord.append(dpiecerow)
                            else:
                                self.illegal = True
                                delta_x = init_data["x"] - event.x
                                delta_y = init_data["y"] - event.y
                                canvas.move(init_data["item"],delta_x,delta_y)
                                break
                        elif final_coord[0] > self.icoord[0] and final_coord[1] < self.icoord[1]:
                            if cur_itm < 77 or ocrn_itm == cur_itm:
                                dpiececol = self.icoord[0] + 1
                                dpiecerow = self.icoord[1] - 1
                                dpiece_coord.append(dpiececol)
                                dpiece_coord.append(dpiecerow)
                            else:
                                self.illegal = True
                                delta_x = init_data["x"] - event.x
                                delta_y = init_data["y"] - event.y
                                canvas.move(init_data["item"],delta_x,delta_y)
                                break
                        elif final_coord[0] < self.icoord[0] and final_coord[1] > self.icoord[1]:
                            if cur_itm > 76 or gcrn_itm == cur_itm:
                                dpiececol = self.icoord[0] - 1
                                dpiecerow = self.icoord[1] + 1
                                dpiece_coord.append(dpiececol)
                                dpiece_coord.append(dpiecerow)
                            else:
                                self.illegal = True
                                delta_x = init_data["x"] - event.x
                                delta_y = init_data["y"] - event.y
                                canvas.move(init_data["item"],delta_x,delta_y)
                                break
                        elif final_coord[0] < self.icoord[0] and final_coord[1] < self.icoord[1]:
                            if cur_itm > 76 or gcrn_itm == cur_itm:
                                dpiececol = self.icoord[0] - 1
                                dpiecerow = self.icoord[1] - 1
                                dpiece_coord.append(dpiececol)
                                dpiece_coord.append(dpiecerow)
                            else:
                                self.illegal = True
                                delta_x = init_data["x"] - event.x
                                delta_y = init_data["y"] - event.y
                                canvas.move(init_data["item"],delta_x,delta_y)
                                break

                        if len(dpiece_coord) != 0 and same_colour != True:
                            dims = RectDims(dpiece_coord)
                            dpiece = canvas.find_enclosed(dims[0],dims[1],dims[2],dims[3])
                            if len(dpiece) == 0:
                                delta_x = init_data["x"] - event.x
                                delta_y = init_data["y"] - event.y
                                canvas.move(init_data["item"],delta_x,delta_y)
                                break
                            else:
                                print "Dead piece:", dpiece
                                if (cur_itm < 77 and dpiece[0] > 76) or (cur_itm > 76 and dpiece[0] < 77):
                                    canvas.delete(dpiece)
                                    if dpiece[0] < 77:
                                        self.gnum -= 1
                                        print "gnum: ", self.gnum
                                    else:
                                        self.rnum -= 1
                                        print "rnum: ", self.rnum

                                    if self.gnum == 0 or self.rnum == 0:
                                        if self.gnum > self.rnum:
                                            tkMessageBox.showinfo(title=None,message="Game Over! Gray Wins!")
                                        else:
                                            tkMessageBox.showinfo(title=None,message="Game Over! Orange Wins!")
                                else:
                                    delta_x = init_data["x"] - event.x
                                    delta_y = init_data["y"] - event.y
                                    canvas.move(init_data["item"],delta_x,delta_y)
                                    self.prev_itm = 0
                        break

                    elif col_diff == 1 and row_diff == 1:
                        if (cur_itm > 64 and cur_itm < 77) and cur_itm != gcrn_itm:
                            if final_coord[0] < self.icoord[0]:
                                continue
                        elif (cur_itm > 76 and cur_itm < 90) and cur_itm != ocrn_itm:
                            if final_coord[0] > self.icoord[0]:
                                continue

                        self.prev_itm = cur_itm
                        break

            else:
                if same_colour == False:
                    delta_x = init_data["x"] - event.x
                    delta_y = init_data["y"] - event.y
                    canvas.move(init_data["item"],delta_x,delta_y)



        canvas.tag_bind("oval", "<ButtonPress-1>", OnTokenButtonPress)
        canvas.tag_bind("oval", "<B1-Motion>", OnTokenMotion)
        canvas.tag_bind("oval", "<ButtonRelease-1>", PieceLogic)
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    rturn = False
    gturn = False
    gcount = 0
    rcount = 0
    ex = CheckerBoard(root, [], 0, 0, False, 12, 12, False, [], [])
    root.geometry("480x460+500+200")
    root.mainloop()

if __name__ == '__main__':
    main()