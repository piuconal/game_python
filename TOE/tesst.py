import sys
import pygame
import numpy as np
import math
import time
from collections import defaultdict
from constants import *

#set up game
diem = defaultdict(int)
tinh = defaultdict(int)

for i in range(ROW):
    for j in range(COL):
        tinh[(i,j)] = -1000000000
def initDiem(): #lưu điểm của từng mẫu, _ tương ứng với 1 ô trống
    diem["OX_"] = 1
    diem["_XO"] = 1
    diem["_X_"] = 10
    diem["OXX_"] = 10
    diem["_XXO"] = 10
    diem["_XX_"] = 100
    diem["_X_X_"] = 100
    diem["OX_XX_"] = 100
    diem["OXXX_"] = 100
    diem["_X_XXO"] = 100
    diem["_XXXO"] = 100
    diem["_XXX_" ] = 1000
    diem["_X_XX_"] = 1000
    diem["_XX_X_"] = 1000
    diem["OXX_XX_" ] = 1200
    diem["_XX_XXO"] = 1200
    diem["OXXXX_" ] = 1200
    diem["_XXXXO" ] = 1200
    diem["OXXX_XX_"] = 1200
    diem["_XX_XXXO"] = 1200
    diem["OXX_XXX_"] = 1200
    diem["_XXX_XXO"] = 1200
    diem["_XX_XX_"] = 1200
    diem["_XXX_X_" ] = 1300
    diem["_X_XXX_" ] = 1300
    diem["OXXXX_X_"] = 1300
    diem["OXXXX_XO" ] = 1300
    diem["_X_XXXXO" ] = 1300
    diem["_XXXX_" ] = 100000000
    diem["OXXXXX_" ] = 1000000000
    diem["_XXXXXO" ] = 1000000000
    diem["_XXXXX_" ] = 1000000000
    diem["OXXXXXO" ] = 1000000000

initDiem()


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE BY HOANG VU')
screen.fill(WHITE)
terminal = ["_X_XX_","_XXX_","_XX_X_","OXX_XX_","_XX_XXO","OXXXX_","_XXXXO","OXXX_XX_","_XX_XXXO","OXX_XXX_","_XXX_XXO","_XX_XX_","_XXX_X_","_X_XXX_","OXXXX_X_","OXXXX_XO","_X_XXXXO"]
normal = ["_X_X_","_XX_","_XXXO","OXXX_","OX_XX_","_XX_XO","OXX_X_","_X_XXO"]

class Board():
    def __init__(self,board = None):
       
        if board != None:
            self.squares = np.array(board.squares)
        else:
            self.squares = np.zeros((ROW,COL))
        
        
        
    def  mark_sqr(self , row , col , player):
        self.squares[row][col] = player    
    
    def empty_sqr(self,row, col):
        return self.squares[row][col] == 0
    def check_row(self, player):
        neg_pl = 1 if player == 2 else 2
        x = np.ones(5)*player
        for i in range(ROW):
            for j in range(ROW-4):
                mt = self.squares[i ,j : j+5]
                if np.equal(mt , x).all():
                    
                    return ((i,j),(i,j+4))
        return None                
    def check_col(self, player):
        neg_col = 1 if player== 2 else 1
        x = np.ones(5)*player
        for i in range(ROW-4):
            for j in range(ROW):
                mt = self.squares[i:i+5 , j]
                if np.equal(mt , x).all():
                    
                    return ((i,j) , (i+4,j))
        return None   

    def check_dia(self, player):
        neg_col = 1 if player ==2 else 1
        x = np.ones(5)*player
        for i in range(ROW -4):
            for j in range(ROW-4):
                mt = self.squares[i: i+5 , j: j+5]
                if np.equal(mt.diagonal(),x ).all():
                   
                    return ((i,j),(i+4,j+4))
                if np.equal(np.fliplr(mt).diagonal() , x ).all():
                    
                    return ((i+4,j),(i,j+4))
        return None

    def check_win(self , player):
        if self.check_row(player) != None:
            return self.check_row(player)
        if self.check_col(player) != None:
            return self.check_col(player)
        if self.check_dia(player) != None:
            return self.check_dia(player)
        return None        

    def draw_win(self, move,player):
        dau = (move[0][1]*SQSIZE + SQSIZE//2 , move[0][0]*SQSIZE + SQSIZE//2)
        cuoi = (move[1][1]*SQSIZE + SQSIZE//2 , move[1][0]*SQSIZE + SQSIZE//2)
        color = CROSS_COLOUR if player ==1 else CIR_COLOUR
        pygame.draw.line(screen, color , dau,cuoi ,LINE_WIDTH) 

    def generate_move(self ):
        moves = []
        for i in range(ROW):
            for j in range(ROW):
                if self.squares[i][j] > 0:
                    continue
                check = 0
                for k in [-1,0,1]:
                    for h in [-1,0,1]:
                        u = i + k
                        t = j+h
                        if 0 <= u < ROW and 0 <= t < ROW:
                            if self.squares[u][t] != 0:
                                moves.append((i,j))
                                check =1 
                                break
                    if check == 1:
                        break        
        return moves
    def generate_threat_move(self ):
        moves = []
        for i in range(ROW):
            for j in range(ROW):
                if self.squares[i][j] > 0:
                    continue
                check = 0
                for k in [-1,0,1]:
                    for h in [-1,0,1]:
                        u = i + k
                        t = j+h
                        if 0 <= u < ROW and 0 <= t < ROW:
                            if self.squares[u][t] != 0:
                                moves.append((i,j))
                                check =1 
                                break
                    if check == 1:
                        break        
        return moves
    def changeToPattern(self,arr,player):
        s = ""
        opp = player%2+1
        for x in arr:
            if x == player:
                s+= "X"
            elif x == opp:
                s+="O"
            else:
                s+="_"
        return s
    def is_Five(self,s):
        if s == "OXXXXX" or s == "XXXXXO" or s == "_XXXXX" or s == "XXXXX_":
            return True
        return False
    def is_Four(self,s):
        if s == "_XXXX_":
            return True
        return False
    def is_Four_One_End(self,s):
        if s == "OXXXX_" or s == "_XXXXO" or  s == "OXXX_X" or s == "OX_XXX" or s == "X_XXXO" or s == "XXX_XO" or s == "XX_XXO" or s == "OXX_XX":
            return True
        return False

    def is_Three(self,s):
        if s == "_XXX__" or s == "__XXX_" or  s == "_X_XX_" or s == "_XX_X_" or s == "_XX_XX" or s == "XX_XX_":
            return True
        return False
    def threat_search_col(self,player):
        neg = player%2+1
        for i in range(ROW-5):
            for j in range(ROW):
                mt = self.squares[i: i+6 , j ]
                s = self.changeToPattern(mt,player)
                if self.is_Five(s):
                    return 5
        for i in range(ROW-5):
            for j in range(ROW):
                mt = self.squares[i: i+6 , j ]
                s = self.changeToPattern(mt,player)
                
                if self.is_Four(s):
                    return 4   
        for i in range(ROW-5):
            for j in range(ROW):
                mt = self.squares[i: i+6 , j ]
                s = self.changeToPattern(mt,player)
                if s == "__XXX_" :
                    self.mark_sqr(i+1,j,neg)
                    self.mark_sqr(i+5,j,neg)
                    return 2
                elif s == "_XXX__":
                    self.mark_sqr(i,j,neg)
                    self.mark_sqr(i+4,j,neg)
                    return 2
                elif self.is_Four_One_End(s):
                    for k in range(len(mt)):
                        if mt[k] == 0:
                            mt[k] = neg
                    return 3
                elif self.is_Three(s) :
                    for k in range(len(mt)):
                        if mt[k] == 0:
                            mt[k] = neg
                    return 2
        return 0
    

    def threat_search_row(self,player):
        neg = player%2+1
        for i in range(ROW):
            for j in range(ROW-5):
                mt = self.squares[i , j : j+6]
                s = self.changeToPattern(mt,player)
                if s == "OXXXXX" or s == "XXXXXO" or s == "_XXXXX" or s == "XXXXX_":
                    return 5
        for i in range(ROW):
            for j in range(ROW-5):
                mt = self.squares[i , j : j+6]
                s = self.changeToPattern(mt,player)
                
                if s == "_XXXX_":
                    return 4
          
        for i in range(ROW):
            for j in range(ROW-5):
                mt = self.squares[i , j : j+6]
                s = self.changeToPattern(mt,player)
                if s == "__XXX_" :
                    self.mark_sqr(i,j+1,neg)
                    self.mark_sqr(i,j+5,neg)
                    return 2
                elif s == "_XXX__":
                    self.mark_sqr(i,j,neg)
                    self.mark_sqr(i,j+4,neg)
                    return 2
                elif self.is_Four_One_End(s):
                    for k in range(len(mt)):
                        if mt[k] == 0:
                            mt[k] = neg
                    return 3
                elif self.is_Three(s) :
                    for k in range(len(mt)):
                        if mt[k] == 0:
                            mt[k] = neg
                    return 2
        return 0
    
    def threat_search_dia(self,player):
        neg = player%2+1
        for i in range(ROW -5):
            for j in range(ROW-5):
                mt = self.squares[i: i+6 , j: j+6]
                
                s = self.changeToPattern(mt.diagonal(),player)
                
                if self.is_Five(s):
                    return 5
                
                s = self.changeToPattern(np.fliplr(mt).diagonal(),player)
                
                if self.is_Five(s):
                    return 5
        for i in range(ROW -5):
             for j in range(ROW-5):
                mt = self.squares[i: i+6 , j: j+6]
                s = self.changeToPattern(mt.diagonal(),player)
                if self.is_Four(s):
                    return 4
                
                s = self.changeToPattern(np.fliplr(mt).diagonal(),player)
                if self.is_Four(s):
                    return 4
                
        for i in range(ROW -5):
            for j in range(ROW-5):
                mt = self.squares[i: i+6 , j: j+6]
                
                s = self.changeToPattern(mt.diagonal(),player)
           
                if s == "__XXX_" :
                    self.mark_sqr(i+1,j+1,neg)
                    self.mark_sqr(i+5,j+5,neg)
                    return 2
                elif s == "_XXX__":
                    self.mark_sqr(i,j,neg)
                    self.mark_sqr(i+4,j+4,neg)
                    return 2
                elif self.is_Three(s) or self.is_Four_One_End(s):
                    for k in range(len(mt)):
                        for l in range(len(mt)):
                            if k == l and mt[k][l] == 0: mt[k][l] = neg
                    return 2
                
                s = self.changeToPattern(np.fliplr(mt).diagonal(),player)
           
                if s == "__XXX_" :
                    self.mark_sqr(i+4,j+1,neg)
                    self.mark_sqr(i,j+5,neg)
                    return 2
                elif s == "_XXX__":
                    self.mark_sqr(i+5,j,neg)
                    self.mark_sqr(i+1,j+4,neg)
                    return 2
                elif self.is_Three(s) or self.is_Four_One_End(s):
                     for k in range(len(mt)):
                        for l in range(len(mt)):
                            if k + l == 5 and mt[k][l] == 0: mt[k][l] = neg
                     return 2
               
        return 0
class Ai:
    no_alphabeta_counter = 0
    counter = 0
    cost = []
    threat_counter = 0

    @classmethod    
    def search_winning_moves(cls , board:Board):
        
        allpossible_move = board.generate_move()
        for move in allpossible_move:
            temp_board = Board(board = board)
            temp_board.mark_sqr(move[0],move[1],2)
            
            if temp_board.check_win(2):
                return (None,move)
        for move in allpossible_move:
            temp_board = Board(board = board)

            temp_board.mark_sqr(move[0],move[1],1)
            
            if temp_board.check_win(1):
                return (None,move)    
        return (None,None)
    @classmethod
    def search_winning_moves_player(cls , board:Board,player):
        
        allpossible_move = board.generate_move()
        for move in allpossible_move:
            temp_board = Board(board = board)
            temp_board.mark_sqr(move[0],move[1],player)
            
            if temp_board.check_win(player):
                return True     
        return False
            
            
            
            
            
            
        
    @classmethod
    def find_threat_move(cls,board: Board,kt,truoc ,start = 0):
        cls.threat_counter += 1
        end = time.time()
        if end - start > 30: return None,0
        temp_board = Board(board=board)
        thu = max(temp_board.threat_search_col(2),temp_board.threat_search_dia(2),temp_board.threat_search_row(2))
        temp_board = Board(board=board)
        test = max(temp_board.threat_search_col(1),temp_board.threat_search_dia(1),temp_board.threat_search_row(1))

        
        if test > thu:
            return None,0
        move = board.generate_move()
        
        for m in move:
            i,j = m[0],m[1]
            if board.squares[i][j] == 0:
                temp_board.mark_sqr(i,j,2)
                tempp = Board(board =board)
                tempp.mark_sqr(i,j,2)
                kq = tempp.threat_search_col(2)
                if kq >= 4:
                    
                    cls.cost.insert(0,(i,j))
                   
                    return (i,j),kq
            
                    
                tempp = Board(board = board)
                tempp.mark_sqr(i,j,2)

                kq = tempp.threat_search_row(2)
                if kq >= 4:
                    
                   
                    cls.cost.insert(0,(i,j))
                    
                    return (i,j),kq
                tempp = Board(board = board)
                tempp.mark_sqr(i,j,2)

                kq = tempp.threat_search_dia(2)
                if kq >= 4:
                    
                    cls.cost.insert(0,(i,j))
                    
                    return (i,j),kq
        for m in move:
            i,j = m[0],m[1]
            kc = abs(truoc[0]-i)+abs(truoc[1]-j)
            if board.squares[i][j] == 0 and (kc <= 4 or kt == False):
                temp_board.mark_sqr(i,j,2)
                tempp = Board(board =board)
                tempp.mark_sqr(i,j,2)

                kq = tempp.threat_search_col(2)
                if kq != 0:
                    vitri,diem = cls.find_threat_move(tempp,True,(i,j),start)
                    if diem >= 4:
                            
                            cls.cost.insert(0,(i,j))
                            
                            return (i,j),diem
            
                    
                tempp = Board(board = board)
                tempp.mark_sqr(i,j,2)

                kq = tempp.threat_search_row(2)
                if kq != 0:
                        vitri,diem = cls.find_threat_move(tempp,True,(i,j),start)
                        if diem >= 4:
                            print(diem)
                            cls.cost.insert(0,(i,j))
                            print(cls.cost)
                            return (i,j),diem
                tempp = Board(board = board)
                tempp.mark_sqr(i,j,2)

                kq = tempp.threat_search_dia(2)
                if kq != 0:
                        vitri,diem = cls.find_threat_move(tempp,True,(i,j),start)
                        if diem >= 4:
                            print(diem)
                            cls.cost.insert(0,(i,j))
                            print(cls.cost)
                            return (i,j),diem
            
        
        return None,0

              
                    
    @classmethod
    def find_next_move(cls,board : Board,depth): #Tìm kiếm nước đi tiếp theo của mãy
        #TH1: Nước đi tiếp theo là nước đi win của người hoặc máy
        value,move = cls.search_winning_moves(board)
        cls.counter = 0
        if move != None:
            cls.cost.clear()
            return move
        #TH2: Tiến hành tìm kiếm cờ đôi cho máy bằng thuật toán ThreatMoveSearch
        print("##################################")
        start = time.time()
        cls.threat_counter = 0
        if len(cls.cost) == 0:
            
            move,diem = cls.find_threat_move(board,kt=False,truoc=(0,0),start= start)
        elif len(cls.cost) == 1:
                cls.cost.clear()
                move,diem = cls.find_threat_move(board,kt=False,truoc=(0,0),start= start)
        else:
            b = cls.cost.pop(0)
            return b
        print("Threat Counter: "+str(cls.threat_counter))
        if move != None:
            print(cls.cost)
            cls.cost.pop(0)
            return move
        cls.no_alphabeta_counter = 0
        start = time.time()
        cls.minmax_alphabeta_test(board,depth,-10000000000,10000000000,True)
        print("Chua Su Dung AlphaBeTa " + str(cls.no_alphabeta_counter))
        print("Thoi gian tim kiem "+str(time.time()-start))
        cls.counter = 0
        #Nếu không có nước cờ đôi tiến hành tìm kiếm nước đi bằng giải thuật minimax
        start = time.time()
        value , move = cls.minmax_alphabeta(board, depth ,-10000000000,10000000000,True)
        print("Da Su Dung AlphaBeTa " + str(cls.counter))
        print("Thoi gian tim kiem "+str(time.time()-start))
        if move != None:
                return move
        else:
                move = (ROW//2 , ROW//2)
        return move
    @classmethod
    def minmax_alphabeta_test(cls , board: Board , depth , alpha,beta , is_O):
        cls.no_alphabeta_counter += 1
        if depth == 0: #Tham số depth chỉ độ sâu cây tìm kiếm, khi độ sâu về 0 thì tiến hành kết thúc
            return (cls.evaluate(board ,is_O) , None)
        all_possible_moves = board.generate_move() #Tìm kiếm tất cả các nước đi có thể
        all_possible_moves = cls.sortt(board , all_possible_moves) #sử dụng hàm sort để sắp xếp các nước đi với mong muốn tìm được các nước đi tốt sớm hơn
        if len(all_possible_moves) == 0:# Không có nước đi nào hợp lệ
            return (cls.evaluate_board(board, not is_O), None)
        best_move = None #khỏi tạo nước đi tốt nhất hiện tại
        if is_O: #nếu là lượt máy 
            best_value = math.inf #giá trị tốt nhất là -vô cùng
            for move in all_possible_moves: #duyệt qua tất cả các nước đi có thể
                temp_board = Board(board= board) # 1 bàn cờ mới copy của bàn cờ hiện tại
                temp_board.mark_sqr(move[0],move[1],2) #Đánh dấu chọn ô này là nước đi tiếp theo của máy
               

               
                value , temp = cls.minmax_alphabeta_test(temp_board, depth-1,alpha,beta,not is_O) #đệ quy 
                if value > tinh[move]: #dict tinh để lưu giá trị tốt nhất của 1 ô hiện tại cho mục đích sắp xếp ở hàm sortt trên
                    tinh[move] = value
                
                if value < best_value: #cập nhật value, best_value nếu kq tốt hơn
                    best_value = value
                    best_move = move
               
              
        else:#lượt người đánh
            best_value = -math.inf #tương tự nhưng best_value cho gtln
            for move in all_possible_moves:
                temp_board = Board(board= board)
                temp_board.mark_sqr(move[0],move[1],1)
                value , temp = cls.minmax_alphabeta_test(temp_board, depth-1,alpha,beta,not is_O)
                
                if value > best_value:
                    best_value = value
                    best_move = move
              
        return (best_value ,best_move)
    @classmethod
    def minmax_alphabeta(cls , board: Board , depth , alpha,beta , is_O):
        if alpha < beta: cls.counter += 1
        if depth == 0: #Tham số depth chỉ độ sâu cây tìm kiếm, khi độ sâu về 0 thì tiến hành kết thúc
            
            return (cls.evaluate(board ,is_O) , None)
        all_possible_moves = board.generate_move() #Tìm kiếm tất cả các nước đi có thể
        if len(all_possible_moves) == 0:# Không có nước đi nào hợp lệ
            return (cls.evaluate_board(board, not is_O), None)
        best_move = None #khỏi tạo nước đi tốt nhất hiện tại
        if is_O: #nếu là lượt máy 
            best_value = math.inf #giá trị tốt nhất là vô cùng
            for move in all_possible_moves: #duyệt qua tất cả các nước đi có thể
                #temp_board = Board(board= board) # 1 bàn cờ mới copy của bàn cờ hiện tạia
                board.mark_sqr(move[0],move[1],2) #Đánh dấu chọn ô này là nước đi tiếp theo của máy

                value , temp = cls.minmax_alphabeta(board, depth-1,alpha,beta,not is_O) #mở động độ sâu cây tìm kiếm 
                if value > tinh[move]: #dict tinh để lưu giá trị tốt nhất của 1 ô hiện tại cho mục đích sắp xếp ở hàm sortt trên
                    tinh[move] = value
                
                if value < best_value: #cập nhật value, best_value nếu kq tốt hơn
                    best_value = value
                    best_move = move
               
                if best_value < beta: #cắt tỉa alpha, cật nhật giá trị của beta
                    beta = best_value
                board.mark_sqr(move[0],move[1],0)
                if alpha >= beta:#nếu thỏa mãn điều kiện alpha >= beta thì dừng tìm kiếm tại nút sâu hơn
                   return (best_value ,best_move)    
        else:#lượt người đánh
            best_value = -math.inf #tương tự nhưng best_value cho gtnn
            for move in all_possible_moves:
                
                board.mark_sqr(move[0],move[1],1)
                
                value , temp = cls.minmax_alphabeta(board, depth-1,alpha,beta,not is_O)
                
                if value > best_value:
                    best_value = value
                    best_move = move
                if best_value > alpha:
                    alpha = best_value
                board.mark_sqr(move[0],move[1],0)
                if beta <= alpha:
                   return (best_value, best_move)
        return (best_value ,best_move)
    
    @classmethod
    def sortt(cls , board : Board , line): #sortt theo điểm của từng ô, ô nào có tinh[n] cao hơn thì có thể tốt hơn
        def my_func(board, move):
            x, y = move
            count = 0
            size = ROW

            for i in [-1, 0, 1,-2,2]:
                for j in [-1, 0, 1,-2,2]:
                    if 0 <= x+i < size and 0 <= y+j < size:
                        if board.squares[x+i][y+j] != 0:
                            count += 1
            return count

        return sorted(line, key=lambda move: tinh[move], reverse=True)

    @classmethod
    def evaluate(cls,board : Board ,is_Oturn): #Hàm đánh giá độ tốt của bàn cờ tại 1 trạng thái
        X_score = cls.get_score(board , 1)
        O_score = cls.get_score(board , 2)
       
        
        return X_score - 0.5*O_score
        
        

    @classmethod
    def get_score(cls, board : Board , player): #tính điểm của từng người
        mau = {}
        cls.mau_col( board , mau ,player) # điểm hàng dọc
        cls.mau_row( board, mau , player) #điểm hàng ngang
        cls.mau_cheo(board ,mau , player)   #điểm đường chéo
        return cls.get_score_consecutive(mau) # hàm tính tổng điểm

    

    
    @classmethod
    def mau_col(cls , board : Board , mau , player):
        board.squares
        for i in range(ROW):
                       
            cls.get_patterns(board.squares[:, i],mau , player)
    @classmethod
    def mau_row(cls , board : Board , mau , player):
        matrix = board.squares
        for i in range(ROW):
            cls.get_patterns(matrix[i] , mau ,player)
    @classmethod
    def mau_cheo(cls, board: Board , mau, player):
        size = ROW
        matrix1 = board.squares
        matrix2 = matrix1[::-1, :]
        for i in range(-size+1, size):
            cls.get_patterns(matrix1.diagonal(i), mau, player)
            cls.get_patterns(matrix2.diagonal(i), mau, player)
    @classmethod
    def get_patterns(cls , line , mau, player): #lấy ra các mẫu để tính điểm vd 'XOOOO' '_X_'
        
        col = player
        neg = player%2 + 1
        s = ''
        old = 0
        for i,c in enumerate(line):
            if c == neg:
                if i+1 < len(line) and line[i+1] == player:
                    s += 'O'
            if c == col:
                
                s += 'X'
            elif c == 0:
                s += '_'
                if i+1 < len(line) and line[i+1] != player:
                    if s in mau.keys():
                        mau[s] += 1
                    else:
                        mau[s] = 1
                    
                    s = ''
                    continue
            
            if i+1 < len(line) and line[i+1] == neg:
                s += 'O'
               

                if s in mau.keys():
                        mau[s] += 1
                else:
                        mau[s] = 1
                s = ''

        if s in mau.keys():
                        mau[s] += 1
        else:
                        mau[s] = 1
                  

    @classmethod
    def get_score_consecutive(cls , pattern_dc):
        score = 0
        
        for pattern in pattern_dc:
            score += diem[pattern]*pattern_dc[pattern] #điểm được cộng = điểm của mẫu * tần xuất xuất hiện của mẫu đó
        
        
        return score
    
class Game:
    def __init__(self):
        self.board = Board()
        self.show_lines()
        self.player = 1
        self.game_over =0

    def show_lines(self):
        #draw vertical
        for i in range (1,ROW):
            pygame.draw.line(screen, LINE_COLOUR ,(SQSIZE*i , 0),(SQSIZE*i , HEIGHT),3)
        #draw horizantal
        for i in range (1,COL):
            pygame.draw.line(screen, LINE_COLOUR ,( 0, SQSIZE*i),(WIDTH , SQSIZE*i),3)
    
    def change_player(self):
        self.player = self.player%2 + 1
    
    def draw_fig(self,row,col):
        if self.player == 1:
            pygame.draw.line(screen , CROSS_COLOUR , (col*SQSIZE+SPACE , row*SQSIZE+SPACE), ((col+1)*SQSIZE-SPACE , (row+1)*SQSIZE-SPACE),LINE_WIDTH)
            pygame.draw.line(screen , CROSS_COLOUR , (col*SQSIZE+SPACE , (row+1)*SQSIZE-SPACE), ((col+1)*SQSIZE-SPACE , row*SQSIZE+SPACE),LINE_WIDTH)
        if self.player == 2:
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE),2)
            center = (col*SQSIZE + SQSIZE // 2 , row*SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen , CIR_COLOUR , center , SQSIZE / 4, LINE_WIDTH)
    def draw_white(self,row,col):
        pygame.draw.rect(screen,LINE_COLOUR,pygame.Rect(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE),2)


def main():
    game = Game()
    last = (0,0)
    while True:
        if game.player == 1 and game.game_over == 0:
            one_click = True
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and one_click:
                    one_click = False
                    pos = event.pos
                    col= int(pos[0] // SQSIZE)
                    row = int(pos[1] // SQSIZE)
                    if game.board.empty_sqr(row,col):
                        game.board.mark_sqr(row,col , game.player)
                        game.draw_fig(row , col)
                        move = game.board.check_win(game.player)
                        if move != None:
                            game.game_over = 1
                            game.board.draw_win(move , game.player)  
                        game.draw_white(last[0],last[1])
                        game.change_player() 

        elif game.player == 2 and game.game_over == 0:
            
            move = Ai.find_next_move(game.board ,2)   
            print(Ai.counter)
            last = move
            game.board.mark_sqr(move[0],move[1],game.player)
            game.draw_fig(move[0],move[1]) 
            move = game.board.check_win(game.player)
            if move != None:
                            game.game_over = 1
                            game.board.draw_win(move , game.player) 
            game.change_player()
        else:
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main()