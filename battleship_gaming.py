############# BASE Info################

import os

# the x-axis wise board
boardX = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
          "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
          "Z": 26}
# the y-axis wise board
boardY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
board = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1",
         "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2",
         "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2", "A3", "B3",
         "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3",
         "U3", "V3", "W3", "X3", "Y3", "Z3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4",
         "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4", "A5", "B5", "C5", "D5",
         "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5",
         "W5", "X5", "Y5", "Z5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6",
         "O6", "P6", "Q6", "R6", "S6", "T6", "U6", "V6", "W6", "X6", "Y6", "Z6", "A7", "B7", "C7", "D7", "E7", "F7",
         "G7", "H7", "I7", "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7",
         "Y7", "Z7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8", "N8", "O8", "P8",
         "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
         "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9", "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9",
         "A0", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "K10", "L10", "M10", "N10", "O10", "P10",
         "Q10", "R10", "S10", "T10", "U10", "V10", "W10", "X10", "Y10", "Z10"]
error_message = "Entry is not valid, try again"

# Instructions for the game
rules = """\

Prepare for Battle:
Secretly place your fleet of 5 ships on your grid. 
To place each ship choose grid location start and end grid location.  
Locations must be adjacent to each other.

How to Play:
You and your opponent will alternate turns, typing out one shot per turn to try and hit each other's ships.

Winning The Game:
If you're the first player to sink your opponent's entire fleet of 5 ship, you win the game!

"""
# View of the board for players
initialboard = """\
{A1}    {B1}    {C1}    {D1}    {E1}    {F1}    {G1}    {H1}    {I1}    {J1}    {K1}    {L1}    {M1}    {N1}    {O1}    {P1}    {Q1}    {R1}    {S1}    {T1}    {U1}    {V1}    {W1}    {X1}    {Y1}    {Z1}
{A2}    {B2}    {C2}    {D2}    {E2}    {F2}    {G2}    {H2}    {I2}    {J2}    {K2}    {L2}    {M2}    {N2}    {O2}    {P2}    {Q2}    {R2}    {S2}    {T2}    {U2}    {V2}    {W2}    {X2}    {Y2}    {Z2}
{A3}    {B3}    {C3}    {D3}    {E3}    {F3}    {G3}    {H3}    {I3}    {J3}    {K3}    {L3}    {M3}    {N3}    {O3}    {P3}    {Q3}    {R3}    {S3}    {T3}    {U3}    {V3}    {W3}    {X3}    {Y3}    {Z3}
{A4}    {B4}    {C4}    {D4}    {E4}    {F4}    {G4}    {H4}    {I4}    {J4}    {K4}    {L4}    {M4}    {N4}    {O4}    {P4}    {Q4}    {R4}    {S4}    {T4}    {U4}    {V4}    {W4}    {X4}    {Y4}    {Z4}
{A5}    {B5}    {C5}    {D5}    {E5}    {F5}    {G5}    {H5}    {I5}    {J5}    {K5}    {L5}    {M5}    {N5}    {O5}    {P5}    {Q5}    {R5}    {S5}    {T5}    {U5}    {V5}    {W5}    {X5}    {Y5}    {Z5}
{A6}    {B6}    {C6}    {D6}    {E6}    {F6}    {G6}    {H6}    {I6}    {J6}    {K6}    {L6}    {M6}    {N6}    {O6}    {P6}    {Q6}    {R6}    {S6}    {T6}    {U6}    {V6}    {W6}    {X6}    {Y6}    {Z6}
{A7}    {B7}    {C7}    {D7}    {E7}    {F7}    {G7}    {H7}    {I7}    {J7}    {K7}    {L7}    {M7}    {N7}    {O7}    {P7}    {Q7}    {R7}    {S7}    {T7}    {U7}    {V7}    {W7}    {X7}    {Y7}    {Z7}
{A8}    {B8}    {C8}    {D8}    {E8}    {F8}    {G8}    {H8}    {I8}    {J8}    {K8}    {L8}    {M8}    {N8}    {O8}    {P8}    {Q8}    {R8}    {S8}    {T8}    {U8}    {V8}    {W8}    {X8}    {Y8}    {Z8}
{A9}    {B9}    {C9}    {D9}    {E9}    {F9}    {G9}    {H9}    {I9}    {J9}    {K9}    {L9}    {M9}    {N9}    {O9}    {P9}    {Q9}    {R9}    {S9}    {T9}    {U9}    {V9}    {W9}    {X9}    {Y9}    {Z9}
{A0}    {B0}    {C0}    {D0}    {E0}    {F0}    {G0}    {H0}    {I0}    {J0}    {K0}    {L0}    {M0}    {N0}    {O0}    {P0}    {Q0}    {R0}    {S0}    {T0}    {U0}    {V0}    {W0}    {X0}    {Y0}    {Z0} 
"""

# Creating Empty board1 for first player
board1 = """\
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
"""
# Creating empty board2 for 2nd player
board2 = """\
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}
"""

# Display for the hit word
word_hit = """\
        
███      ███  ████████  █████████
███      ███    ███        ███   
████████████    ███        ███     
███      ███    ███        ███  
███      ███  ████████     ███    
               
"""
# Display for the miss word
word_miss = """\
           
   ████    ████    ████████ ████████ ████████  
████   ████   ████   ████   ████     ████         
████          ████   ████       ████     ████
████          ████ ████████ ████████ ████████   
           
"""
# Welcome display for the game
word_battleship = """\
                          
████████████      ████     ████████ ████████ ████     ████████ ████████ ████   ████ ████████ ███████████
████    ████  ████    ████   ████     ████   ████     ████     ████     ████   ████   ████   ████   ████
████████████  ████████████   ████     ████   ████     ████████ ████████ ███████████   ████   ███████████
████    ████  ████    ████   ████     ████   ████     ████         ████ ████   ████   ████   ████
████████████  ████    ████   ████     ████   ████████ ████████ ████████ ████   ████ ████████ ████
                                                                
"""


##########END OF BASE##########
# Player class initializing all the attributes used in the game
class Players:
    def __init__(self, name):
        boardavailable = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1",
                          "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1", "A2", "B2", "C2", "D2",
                          "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2",
                          "T2", "U2", "V2", "W2", "X2", "Y2", "Z2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
                          "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3",
                          "X3", "Y3", "Z3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4",
                          "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4", "A5",
                          "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5",
                          "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5", "A6", "B6", "C6", "D6", "E6",
                          "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6",
                          "U6", "V6", "W6", "X6", "Y6", "Z6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7",
                          "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7",
                          "Y7", "Z7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8",
                          "N8", "O8", "P8", "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8", "A9", "B9",
                          "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9",
                          "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9", "A0", "B0", "C0", "D0", "E0", "F0",
                          "G0", "H0", "I0", "J0", "K0", "L0", "M0", "N0", "O0", "P0", "Q0", "R0", "S0", "T0", "U0",
                          "V0", "W0", "X0", "Y0", "Z0"]
        board_confirmed = True
        aircraft_location = []
        destroyer_1_location = []
        destroyer_2_location = []
        battleship_location = []
        crusier_location = []
        aircraft_complete = False
        destroyer_1_complete = False
        destroyer_2_complete = False
        battleship_complete = False
        crusier_complete = False
        board_playing_game = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1",
                              "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1", "A2", "B2", "C2", "D2",
                              "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2",
                              "T2", "U2", "V2", "W2", "X2", "Y2", "Z2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
                              "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3",
                              "X3", "Y3", "Z3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4",
                              "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4", "A5",
                              "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5",
                              "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5", "A6", "B6", "C6", "D6", "E6",
                              "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6",
                              "U6", "V6", "W6", "X6", "Y6", "Z6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7",
                              "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7",
                              "Y7", "Z7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8",
                              "N8", "O8", "P8", "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8", "A9", "B9",
                              "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9",
                              "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9", "A0", "B0", "C0", "D0", "E0", "F0",
                              "G0", "H0", "I0", "J0", "K0", "L0", "M0", "N0", "O0", "P0", "Q0", "R0", "S0", "T0", "U0",
                              "V0", "W0", "X0", "Y0", "Z0"]
        aircraft_sunk = False
        destroyer_1_sunk = False
        destroyer_2_sunk = False
        battleship_sunk = False
        crusier_sunk = False
        # Reference to the current instance of the class
        #
        self.name = name
        self.boardavailable = boardavailable
        self.board_confirmed = board_confirmed
        self.aircraft_location = aircraft_location
        self.destroyer_1_location = destroyer_1_location
        self.destroyer_2_location = destroyer_2_location
        self.battleship_location = battleship_location
        self.crusier_location = crusier_location
        self.aircraft_complete = aircraft_complete
        self.destroyer_1_complete = destroyer_1_complete
        self.destroyer_2_complete = destroyer_2_complete
        self.battleship_complete = battleship_complete
        self.crusier_complete = crusier_complete
        self.board_playing_game = board_playing_game
        self.aircraft_sunk = aircraft_sunk
        self.destroyer_1_sunk = destroyer_1_sunk
        self.destroyer_2_sunk = destroyer_2_sunk
        self.battleship_sunk = battleship_sunk
        self.crusier_sunk = crusier_sunk

    # creating the aircraft method by passing the self argument
    def aircraft(self):
        complete = False
        self.complete = complete
        # Creating temporary location for aircraft as empty
        aircraft_temp_location = []
        # Displaying the size of aircraft to the player into upper case
        print("aircraft Size is 9")
        # Player1 giving the start title
        aircraft_start = input("START TILE: ").upper()
        # Player2 giving the end title and converting into upper case
        aircraft_end = input("END TILE: ").upper()
        if aircraft_start in self.boardavailable:
            if aircraft_end in self.boardavailable:
                if aircraft_start[0].upper() == aircraft_end[0].upper():
                    if int(aircraft_end[1:]) > int(aircraft_start[1:]) and int(aircraft_end[1:]) == int(
                            aircraft_start[1:]) + 8:
                        # converting into integers
                        tnum = int(aircraft_end[1:]) - 7
                        secondtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_end[1:]) - 6
                        thirdtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_end[1:]) - 5
                        fourthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_end[1:]) - 4
                        fifthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_end[1:]) - 3
                        sixthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_end[1:]) - 2
                        seventhtile = aircraft_start[0] + str(tnum)
                        tnum2 = int(aircraft_end[1:]) - 1
                        eighthtile = aircraft_start[0] + str(tnum2)
                        # Appending the titles to the aircraft_temp_location
                        aircraft_temp_location.append(aircraft_start)
                        aircraft_temp_location.append(secondtile)
                        aircraft_temp_location.append(thirdtile)
                        aircraft_temp_location.append(fourthtile)
                        aircraft_temp_location.append(fifthtile)
                        aircraft_temp_location.append(sixthtile)
                        aircraft_temp_location.append(seventhtile)
                        aircraft_temp_location.append(eighthtile)
                        aircraft_temp_location.append(aircraft_end)
                        complete = True
                    elif int(aircraft_start[1:]) > int(aircraft_end[1:]) and int(aircraft_start[1:]) == int(
                            aircraft_end[1:]) + 8:
                        tnum = int(aircraft_start[1:]) - 7
                        secondtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_start[1:]) - 6
                        thirdtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_start[1:]) - 5
                        fourthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_start[1:]) - 4
                        fifthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_start[1:]) - 3
                        sixthtile = aircraft_start[0] + str(tnum)
                        tnum = int(aircraft_start[1:]) - 2
                        seventhtile = aircraft_start[0] + str(tnum)
                        tnum2 = int(aircraft_start[1:]) - 1
                        eighthtile = aircraft_start[0] + str(tnum2)
                        # Appending the titles to the aircraft_temp_location
                        aircraft_temp_location.append(aircraft_start)
                        aircraft_temp_location.append(eighthtile)
                        aircraft_temp_location.append(seventhtile)
                        aircraft_temp_location.append(sixthtile)
                        aircraft_temp_location.append(fifthtile)
                        aircraft_temp_location.append(fourthtile)
                        aircraft_temp_location.append(thirdtile)
                        aircraft_temp_location.append(secondtile)
                        aircraft_temp_location.append(aircraft_end)
                        complete = True
                    else:
                        # printing the error method
                        print_error()

                # Conditions to check the start and end of the air craft from intial
                elif aircraft_start[1:] == aircraft_end[1:]:
                    if boardX[aircraft_end[0].upper()] > boardX[aircraft_start[0].upper()] and boardX[
                        aircraft_end[0].upper()] == boardX[aircraft_start[0].upper()] + 8:
                        tnum = boardX[aircraft_end[0]] - 7
                        secondtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX[aircraft_end[0]] - 6
                        thirdtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX[aircraft_end[0]] - 5
                        fourthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX[aircraft_end[0]] - 4
                        fifthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX[aircraft_end[0]] - 3
                        sixthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX[aircraft_end[0]] - 2
                        seventhtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum2 = boardX[aircraft_end[0]] - 1
                        eighthtile = getletter(tnum2) + str(aircraft_start[1:])
                        aircraft_temp_location.append(aircraft_start)
                        aircraft_temp_location.append(secondtile)
                        aircraft_temp_location.append(thirdtile)
                        aircraft_temp_location.append(fourthtile)
                        aircraft_temp_location.append(fifthtile)
                        aircraft_temp_location.append(sixthtile)
                        aircraft_temp_location.append(seventhtile)
                        aircraft_temp_location.append(eighthtile)
                        aircraft_temp_location.append(aircraft_end)
                        complete = True
                    elif boardX.get(aircraft_start[0].upper()) > boardX.get(aircraft_end[0].upper()) and boardX.get(
                            aircraft_start[0].upper()) == boardX.get(aircraft_end[0].upper()) + 8:
                        tnum = boardX.get(aircraft_start[0].upper()) - 7
                        secondtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX.get(aircraft_start[0].upper()) - 6
                        thirdtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX.get(aircraft_start[0].upper()) - 5
                        fourthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX.get(aircraft_start[0].upper()) - 4
                        fifthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX.get(aircraft_start[0].upper()) - 3
                        sixthtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum = boardX.get(aircraft_start[0].upper()) - 2
                        seventhtile = getletter(tnum) + str(aircraft_start[1:])
                        tnum2 = boardX.get(aircraft_start[0].upper()) - 1
                        eighthtile = getletter(tnum2) + str(aircraft_start[1:])
                        aircraft_temp_location.append(aircraft_start)
                        aircraft_temp_location.append(eighthtile)
                        aircraft_temp_location.append(seventhtile)
                        aircraft_temp_location.append(sixthtile)
                        aircraft_temp_location.append(fifthtile)
                        aircraft_temp_location.append(fourthtile)
                        aircraft_temp_location.append(thirdtile)
                        aircraft_temp_location.append(secondtile)
                        aircraft_temp_location.append(aircraft_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in aircraft_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles aircraft Tiles:", aircraft_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in aircraft_temp_location:
                        self.aircraft_location.append(i)
                    for i in aircraft_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[De]"
                    tcomplete = True
                    self.aircraft_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    # creating the destroyer_1 method by passing the self argument
    def destroyer_1(self):
        complete = False
        self.complete = complete
        # Creating temporary location for destroyer_1 as empty array
        destroyer_1_temp_location = []
        # Displaying the size of destroyer_1 to the player
        print("destroyer_1 Size is 3")
        destroyer_1_start = input("START TILE: ").upper()
        destroyer_1_end = input("END TILE: ").upper()

        if destroyer_1_start in self.boardavailable:
            if destroyer_1_end in self.boardavailable:
                if destroyer_1_start[0].upper() == destroyer_1_end[0].upper():
                    if int(destroyer_1_end[1:]) > int(destroyer_1_start[1:]) and int(destroyer_1_end[1:]) == int(
                            destroyer_1_start[1:]) + 2:
                        tnum = int(destroyer_1_end[1:]) - 1
                        secondtile = destroyer_1_start[0] + str(tnum)
                        destroyer_1_temp_location.append(destroyer_1_start)
                        destroyer_1_temp_location.append(secondtile)
                        destroyer_1_temp_location.append(destroyer_1_end)
                        complete = True
                    elif int(destroyer_1_start[1:]) > int(destroyer_1_end[1:]) and int(destroyer_1_start[1:]) == int(
                            destroyer_1_end[1:]) + 2:
                        tnum = int(destroyer_1_start[1:]) - 1
                        secondtile = destroyer_1_start[0] + str(tnum)
                        destroyer_1_temp_location.append(destroyer_1_start)
                        destroyer_1_temp_location.append(secondtile)
                        destroyer_1_temp_location.append(destroyer_1_end)
                        complete = True
                    else:
                        print_error()

                # Conditions to check the start and end of the destryer_1 from intial
                elif destroyer_1_start[1:] == destroyer_1_end[1:]:
                    if boardX[destroyer_1_end[0].upper()] > boardX[destroyer_1_start[0].upper()] and boardX[
                        destroyer_1_end[0].upper()] == boardX[destroyer_1_start[0].upper()] + 2:
                        tnum = boardX[destroyer_1_end[0]] - 1
                        secondtile = getletter(tnum) + str(destroyer_1_start[1:])
                        destroyer_1_temp_location.append(destroyer_1_start)
                        destroyer_1_temp_location.append(secondtile)
                        destroyer_1_temp_location.append(destroyer_1_end)
                        complete = True
                    elif boardX.get(destroyer_1_start[0].upper()) > boardX.get(
                            destroyer_1_end[0].upper()) and boardX.get(destroyer_1_start[0].upper()) == boardX.get(
                        destroyer_1_end[0].upper()) + 2:
                        tnum = boardX.get(destroyer_1_start[0].upper()) - 1
                        secondtile = getletter(tnum) + str(destroyer_1_start[1:])
                        destroyer_1_temp_location.append(destroyer_1_start)
                        destroyer_1_temp_location.append(secondtile)
                        destroyer_1_temp_location.append(destroyer_1_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in destroyer_1_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles destroyer_1 Tiles:", destroyer_1_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in destroyer_1_temp_location:
                        self.destroyer_1_location.append(i)
                    for i in destroyer_1_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[S]"
                    tcomplete = True
                    self.destroyer_1_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    # creating the destroyer_2 method by passing the self argument
    def destroyer_2(self):
        complete = False
        self.complete = complete
        # Creating temporary location for destroyer_2 as empty array
        destroyer_2_temp_location = []
        # Displaying the size of destroyer_2 to the player
        print("destroyer_2 Size is 3")
        destroyer_2_start = input("START TILE: ").upper()
        destroyer_2_end = input("END TILE: ").upper()

        if destroyer_2_start in self.boardavailable:
            if destroyer_2_end in self.boardavailable:
                if destroyer_2_start[0].upper() == destroyer_2_end[0].upper():
                    # Condition to check the end is greater than the start
                    if int(destroyer_2_end[1:]) > int(destroyer_2_start[1:]) and int(destroyer_2_end[1:]) == int(
                            destroyer_2_start[1:]) + 2:
                        tnum = int(destroyer_2_end[1:]) - 1
                        secondtile = destroyer_2_start[0] + str(tnum)
                        destroyer_2_temp_location.append(destroyer_2_start)
                        destroyer_2_temp_location.append(secondtile)
                        destroyer_2_temp_location.append(destroyer_2_end)
                        complete = True
                    # Condition to check the start is greater than the end
                    elif int(destroyer_2_start[1:]) > int(destroyer_2_end[1:]) and int(destroyer_2_start[1:]) == int(
                            destroyer_2_end[1:]) + 2:
                        tnum = int(destroyer_2_start[1:]) - 1
                        secondtile = destroyer_2_start[0] + str(tnum)
                        destroyer_2_temp_location.append(destroyer_2_start)
                        destroyer_2_temp_location.append(secondtile)
                        destroyer_2_temp_location.append(destroyer_2_end)
                        complete = True
                    else:
                        print_error()

                # Conditions to check the start and end of the destryer_2 from intial
                elif destroyer_2_start[1:] == destroyer_2_end[1:]:
                    if boardX[destroyer_2_end[0].upper()] > boardX[destroyer_2_start[0].upper()] and boardX[
                        destroyer_2_end[0].upper()] == boardX[destroyer_2_start[0].upper()] + 2:
                        tnum = boardX[destroyer_2_end[0]] - 1
                        secondtile = getletter(tnum) + str(destroyer_2_start[1:])
                        destroyer_2_temp_location.append(destroyer_2_start)
                        destroyer_2_temp_location.append(secondtile)
                        destroyer_2_temp_location.append(destroyer_2_end)
                        complete = True
                    elif boardX.get(destroyer_2_start[0].upper()) > boardX.get(
                            destroyer_2_end[0].upper()) and boardX.get(destroyer_2_start[0].upper()) == boardX.get(
                        destroyer_2_end[0].upper()) + 2:
                        tnum = boardX.get(destroyer_2_start[0].upper()) - 1
                        secondtile = getletter(tnum) + str(destroyer_2_start[1:])
                        destroyer_2_temp_location.append(destroyer_2_start)
                        destroyer_2_temp_location.append(secondtile)
                        destroyer_2_temp_location.append(destroyer_2_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in destroyer_2_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles destroyer_2 Tiles:", destroyer_2_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in destroyer_2_temp_location:
                        self.destroyer_2_location.append(i)
                    for i in destroyer_2_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[Ca]"
                    tcomplete = True
                    self.destroyer_2_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    # creating the battleship method by passing the self argument
    def battleship(self):
        complete = False
        self.complete = complete
        # Creating temporary location for battleship as empty array
        battleship_temp_location = []
        # Displaying the size of Battleship to the player
        print("Battleship Size is 7")
        battleship_start = input("START TILE: ").upper()
        battleship_end = input("END TILE: ").upper()

        if battleship_start in self.boardavailable:
            if battleship_end in self.boardavailable:
                if battleship_start[0].upper() == battleship_end[0].upper():
                    if int(battleship_end[1:]) > int(battleship_start[1:]) and int(battleship_end[1:]) == int(
                            battleship_start[1:]) + 6:
                        tnum = int(battleship_end[1:]) - 5
                        secondtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_end[1:]) - 4
                        thirdtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_end[1:]) - 3
                        fourthtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_end[1:]) - 2
                        fifthtile = battleship_start[0] + str(tnum)
                        tnum2 = int(battleship_end[1:]) - 1
                        sixthtile = battleship_start[0] + str(tnum2)
                        # Appending the titles
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(fourthtile)
                        battleship_temp_location.append(fifthtile)
                        battleship_temp_location.append(sixthtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    # Condition to check the start is greater than the end
                    elif int(battleship_start[1:]) > int(battleship_end[1:]) and int(battleship_start[1:]) == int(
                            battleship_end[1:]) + 6:
                        tnum = int(battleship_start[1:]) - 5
                        secondtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_start[1:]) - 4
                        thirdtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_start[1:]) - 3
                        fourthtile = battleship_start[0] + str(tnum)
                        tnum = int(battleship_start[1:]) - 2
                        fifthtile = battleship_start[0] + str(tnum)
                        tnum2 = int(battleship_start[1:]) - 1
                        sixthtile = battleship_start[0] + str(tnum2)
                        # Appending the titles
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(sixthtile)
                        battleship_temp_location.append(fifthtile)
                        battleship_temp_location.append(fourthtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    else:
                        print_error()

                # Conditions to check the start and end of the battleship from intial
                elif battleship_start[1:] == battleship_end[1:]:
                    if boardX[battleship_end[0].upper()] > boardX[battleship_start[0].upper()] and boardX[
                        battleship_end[0].upper()] == boardX[battleship_start[0].upper()] + 6:
                        tnum = boardX[battleship_end[0]] - 5
                        secondtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX[battleship_end[0]] - 4
                        thirdtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX[battleship_end[0]] - 3
                        fourthtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX[battleship_end[0]] - 2
                        fifthtile = getletter(tnum) + str(battleship_start[1:])
                        tnum2 = boardX[battleship_end[0]] - 1
                        sixthtile = getletter(tnum2) + str(battleship_start[1:])
                        # Appending the titles
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(fourthtile)
                        battleship_temp_location.append(fifthtile)
                        battleship_temp_location.append(sixthtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    elif boardX.get(battleship_start[0].upper()) > boardX.get(battleship_end[0].upper()) and boardX.get(
                            battleship_start[0].upper()) == boardX.get(battleship_end[0].upper()) + 6:
                        tnum = boardX.get(battleship_start[0].upper()) - 5
                        secondtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX.get(battleship_start[0].upper()) - 4
                        thirdtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX.get(battleship_start[0].upper()) - 3
                        fourthtile = getletter(tnum) + str(battleship_start[1:])
                        tnum = boardX.get(battleship_start[0].upper()) - 2
                        fifthtile = getletter(tnum) + str(battleship_start[1:])
                        tnum2 = boardX.get(battleship_start[0].upper()) - 1
                        sixthtile = getletter(tnum2) + str(battleship_start[1:])
                        # Appending the titles
                        battleship_temp_location.append(battleship_start)
                        battleship_temp_location.append(sixthtile)
                        battleship_temp_location.append(fifthtile)
                        battleship_temp_location.append(fourthtile)
                        battleship_temp_location.append(thirdtile)
                        battleship_temp_location.append(secondtile)
                        battleship_temp_location.append(battleship_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in battleship_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        if complete == True:
            print("Tiles Battleship Tiles:", battleship_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in battleship_temp_location:
                        self.battleship_location.append(i)
                    for i in battleship_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[B]"
                    tcomplete = True
                    self.battleship_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    # creating the crusier method by passing the self argument
    def crusier(self):
        complete = False
        self.complete = complete
        # Creating temporary location for crusier as empty array
        crusier_temp_location = []
        # Displaying the size of crusier to the player
        print("crusier Size is 5")
        crusier_start = input("START TILE: ").upper()
        crusier_end = input("END TILE: ").upper()

        if crusier_start in self.boardavailable:
            if crusier_end in self.boardavailable:
                if crusier_start[0].upper() == crusier_end[0].upper():
                    if int(crusier_end[1:]) > int(crusier_start[1:]) and int(crusier_end[1:]) == int(
                            crusier_start[1:]) + 4:
                        tnum = int(crusier_end[1:]) - 3
                        secondtile = crusier_start[0] + str(tnum)
                        tnum2 = int(crusier_end[1:]) - 2
                        thirdtile = crusier_start[0] + str(tnum2)
                        tnum3 = int(crusier_end[1:]) - 1
                        fourthtile = crusier_start[0] + str(tnum3)
                        crusier_temp_location.append(crusier_start)
                        crusier_temp_location.append(secondtile)
                        crusier_temp_location.append(thirdtile)
                        crusier_temp_location.append(fourthtile)
                        crusier_temp_location.append(crusier_end)
                        complete = True
                    elif int(crusier_start[1:]) > int(crusier_end[1:]) and int(crusier_start[1:]) == int(
                            crusier_end[1:]) + 4:
                        tnum = int(crusier_start[1:]) - 3
                        secondtile = crusier_start[0] + str(tnum)
                        tnum2 = int(crusier_start[1:]) - 2
                        thirdtile = crusier_start[0] + str(tnum2)
                        tnum3 = int(crusier_start[1:]) - 1
                        fourthtile = crusier_start[0] + str(tnum3)
                        crusier_temp_location.append(crusier_start)
                        crusier_temp_location.append(fourthtile)
                        crusier_temp_location.append(thirdtile)
                        crusier_temp_location.append(secondtile)
                        crusier_temp_location.append(crusier_end)
                        complete = True
                    else:
                        print_error()

                # Conditions to check the start and end of the cruiser from initial
                elif crusier_start[1:] == crusier_end[1:]:
                    if boardX[crusier_end[0].upper()] > boardX[crusier_start[0].upper()] and boardX[
                        crusier_end[0].upper()] == boardX[crusier_start[0].upper()] + 4:
                        tnum = boardX[crusier_end[0]] - 3
                        secondtile = getletter(tnum) + str(crusier_start[1:])
                        tnum2 = boardX[crusier_end[0]] - 2
                        thirdtile = getletter(tnum2) + str(crusier_start[1:])
                        tnum3 = boardX[crusier_end[0]] - 1
                        fourthtile = getletter(tnum3) + str(crusier_start[1:])
                        crusier_temp_location.append(crusier_start)
                        crusier_temp_location.append(secondtile)
                        crusier_temp_location.append(thirdtile)
                        crusier_temp_location.append(fourthtile)
                        crusier_temp_location.append(crusier_end)
                        complete = True
                    # Condition to check the start is greater than the end
                    elif boardX.get(crusier_start[0].upper()) > boardX.get(crusier_end[0].upper()) and boardX.get(
                            crusier_start[0].upper()) == boardX.get(crusier_end[0].upper()) + 4:
                        tnum = boardX.get(crusier_start[0].upper()) - 3
                        secondtile = getletter(tnum) + str(crusier_start[1:])
                        tnum2 = boardX.get(crusier_start[0].upper()) - 2
                        thirdtile = getletter(tnum2) + str(crusier_start[1:])
                        tnum3 = boardX.get(crusier_start[0].upper()) - 1
                        fourthtile = getletter(tnum3) + str(crusier_start[1:])
                        crusier_temp_location.append(crusier_start)
                        crusier_temp_location.append(fourthtile)
                        crusier_temp_location.append(thirdtile)
                        crusier_temp_location.append(secondtile)
                        crusier_temp_location.append(crusier_end)
                        complete = True
                    else:
                        print_error()

                else:
                    print_error()

            else:
                print_error()

        else:
            print_error()

        for i in crusier_temp_location:
            if i not in self.boardavailable:
                complete = False
                print_error()
                break

        # Checking with  if condition the crusier tiles
        if complete == True:
            print("Tiles crusier Tiles:", crusier_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in crusier_temp_location:
                        self.crusier_location.append(i)
                    for i in crusier_temp_location:
                        tindex = self.boardavailable.index(i)
                        self.boardavailable[tindex] = "[C]"
                    tcomplete = True
                    self.crusier_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")


############# CLASS END

############ start functions ####
def getletter(number):
    for key, value in boardX.items():
        if value == number:
            return key


# Method to update the board
def print_updated_board(board, board2):
    print(board.format(*board2))


# method to display the error message
def print_error():
    print(error_message)


# creating the method of combine pieces by appending
def combine_pieces(d, s, c, b, ca):
    combine_list = []
    for i in d, s, c, b, ca:
        for g in i:
            combine_list.append(g)
    return combine_list


def check_suken_ship(player, attack_choice):
    # Increment the des_hit
    if player.aircraft_sunk == False:
        des_hit = 0
        for i in attack_choice:
            if i in player.aircraft_location:
                des_hit += 1
            if des_hit == 9:
                player.aircraft_sunk = True
                print("***You Sunk My aircraft!***")
                break
    # Increment the sub_hit
    if player.destroyer_1_sunk == False:
        sub_hit = 0
        for i in attack_choice:
            if i in player.destroyer_1_location:
                sub_hit += 1
            if sub_hit == 3:
                player.destroyer_1_sunk = True
                print("***You Sunk My destroyer_1!***")
                break
    # Increment the cr_hit
    if player.destroyer_2_sunk == False:
        cr_hit = 0
        for i in attack_choice:
            if i in player.destroyer_2_location:
                cr_hit += 1
            if cr_hit == 3:
                player.destroyer_2_sunk = True
                print("***You Sunk My destroyer_2!***")
                break
    # Increment the ba_hit
    if player.battleship_sunk == False:
        ba_hit = 0
        for i in attack_choice:
            if i in player.battleship_location:
                ba_hit += 1
            if ba_hit == 4:
                player.battleship_sunk = True
                print("***You Sunk My Battleship!***")
                break
    # Increment the ca_hit
    if player.crusier_sunk == False:
        ca_hit = 0
        for i in attack_choice:
            if i in player.crusier_location:
                ca_hit += 1
            if ca_hit == 5:
                player.crusier_sunk = True
                print("***You Sunk My crusier!***")
                break


# method to get the information of ship status
def ship_statues(player):
    aircraft = ""
    destroyer_1 = ""
    destroyer_2 = ""
    battleship = ""
    crusier = ""
    # Condition to check the aircraft sunk or alive
    if player.aircraft_sunk == True:
        aircraft = "Sunk"
    elif player.aircraft_sunk == False:
        aircraft = "Alive"
    # Condition to check the Destroyer_1 sunk or alive
    if player.destroyer_1_sunk == True:
        destroyer_1 = "Sunk"
    elif player.destroyer_1_sunk == False:
        destroyer_1 = "Alive"
    # Condition to check the Destroyer_2 sunk or alive
    if player.destroyer_2_sunk == True:
        destroyer_2 = "Sunk"
    elif player.destroyer_2_sunk == False:
        destroyer_2 = "Alive"
    # Condition to check the battleship sunk or alive
    if player.battleship_sunk == True:
        battleship = "Sunk"
    elif player.battleship_sunk == False:
        battleship = "Alive"
    # Condition to check the crusier sunk or alive
    if player.crusier_sunk == True:
        crusier = "Sunk"
    elif player.crusier_sunk == False:
        crusier = "Alive"

    # Displaying the status of enemy ships
    statements = """\
Enemy Ship Statues:
aircraft: {des}
destroyer_1: {sub}
destroyer_2: {cr}
Battleship: {ba}
crusier: {ca}
        """.format(des=aircraft, sub=destroyer_1, cr=destroyer_2, ba=battleship, ca=crusier)
    print(statements)


# checking all the ships suck is true to find the winner
def check_winner(player):
    if player.aircraft_sunk == True and player.destroyer_1_sunk == True and player.destroyer_2_sunk == True and player.battleship_sunk == True and player.crusier_sunk == True:
        return True
    else:
        return False


############ end of functions ############

#### GAME START####
print(word_battleship)
start_game = False
while start_game == False:
    start_input = input("Type s to start game or Type i for Instructions: ").upper()
    # Getting the instructions to play the game before we start
    if start_input == "I":
        print(rules)
    # getting the input to start the game by players
    elif start_input == "S":
        start_game = True
os.system('cls')
with open('battleship_text.txt') as f:
    contents = f.read()
    print("\n")
    print("The highest score till now with 27 hits:", contents)
    print("\n")

# Getting the player names to start the game
player_1_name = input("Input Player 1 Name: ")
player_2_name = input("Input Player 2 Name: ")

player1 = Players(player_1_name)
player2 = Players(player_2_name)

# Asking the players to start the game by setting up the board
ready = False
while ready == False:
    answer = input("Ready for Board Set-Up, yes or no: ")
    if answer == "yes":
        ready = True

######### BOARD SETUP Player 1 ########
print("Player 2 not looking the board start the ship placing ")
# getting the player1 input to display the  board
player1_board_list = player1.boardavailable
print(initialboard)

# calling destroyer_1 method and checking the condition when player1 is playing
player1.destroyer_1()
while player1.destroyer_1_complete == False:
    player1.destroyer_1()
print(player1.destroyer_1_location)
print_updated_board(board1, player1_board_list)

# calling destroyer_2 method and checking the condition
player1.destroyer_2()
while player1.destroyer_2_complete == False:
    player1.destroyer_2()
print(player1.destroyer_2_location)
print_updated_board(board1, player1_board_list)

# calling crusier method when player 1 is playing
player1.crusier()
while player1.crusier_complete == False:
    player1.crusier()
print(player1.crusier_location)
print_updated_board(board1, player1_board_list)

# calling battleship method when player1 is playing
player1.battleship()
while player1.battleship_complete == False:
    player1.battleship()
print(player1.battleship_location)
print_updated_board(board1, player1_board_list)

# calling Aircraft method and checking the while condition and printing the location
player1.aircraft()
while player1.aircraft_complete == False:
    player1.aircraft()
print(player1.aircraft_location)
print_updated_board(board1, player1_board_list)

ready = False
while ready == False:
    answer = input("Are you complete viewing your board? yes or no ")
    if answer == "yes":
        ready = True
        os.system('cls')

########### BOARD SETUP Player 2 ###########
print("Player 1 not looking the board start the ship placing ")
ready = False
# getting the player2 input to display the board to start the game
while ready == False:
    answer = input("Ready for Board Set-Up, yes or no: ")
    if answer == "yes":
        ready = True

player2_board_list = player2.boardavailable
print(initialboard)

# calling destroyer_1 method and checking the condition
player2.destroyer_1()
while player2.destroyer_1_complete == False:
    player2.destroyer_1()
print(player2.destroyer_1_location)
print_updated_board(board2, player2_board_list)

# calling destroyer_2 method and checking the condition
player2.destroyer_2()
while player2.destroyer_2_complete == False:
    player2.destroyer_2()
print(player2.destroyer_2_location)
print_updated_board(board2, player2_board_list)

# calling crusier method when player 2 is playing
player2.crusier()
while player2.crusier_complete == False:
    player2.crusier()
print(player2.crusier_location)
print_updated_board(board2, player2_board_list)

# calling battleship method when player2 is playing
player2.battleship()
while player2.battleship_complete == False:
    player2.battleship()
print(player2.battleship_location)
print_updated_board(board2, player2_board_list)

# calling Aircraft method and checking the while condition and printing the location
player2.aircraft()
while player2.aircraft_complete == False:
    player2.aircraft()
print(player2.aircraft_location)
print_updated_board(board2, player2_board_list)

ready = False
while ready == False:
    answer = input("Are you complete viewing your board? yes or no ")
    if answer == "yes":
        ready = True
        os.system('cls')

############### GAME START ###############
p1name = player1.name
p2name = player2.name
player1_game_board = player2.board_playing_game
player2_game_board = player1.board_playing_game
player1_attack_choice = []
player2_attack_choice = []
# Getting all the ships locations of player1 in one board by using combine_pieces
player1_piece_location = combine_pieces(player1.aircraft_location, player1.destroyer_1_location,
                                        player1.destroyer_2_location, player1.battleship_location,
                                        player1.crusier_location)
# Getting all the ships locations of player2 in one board by using the combine_pieces
player2_piece_location = combine_pieces(player2.aircraft_location, player2.destroyer_1_location,
                                        player2.destroyer_2_location, player2.battleship_location,
                                        player2.crusier_location)
game_complete = False
player1_winner = False
player2_winner = False
while game_complete == False:

    player1_turn = True
    player2_turn = True
    while player1_turn == True:
        # During the turn of player1 displaying the guess board of player2
        player2_turn = True
        print("-------------------------------------------------------------------------")
        print_updated_board(board2, player1_game_board)
        # for displaying the alive or sunk ships status to player1
        ship_statues(player2)
        print(p1name + "'s Turn")
        grid_choice1 = input("Pick Tile to Attack: ").upper()
        # user entered choice exists in the board
        if grid_choice1 in board:
            # player1 entered valid new grid_choice
            if grid_choice1 not in player1_attack_choice:
                # Displaying x if player1 choice is correct
                if grid_choice1 in player2_piece_location:
                    player1_attack_choice.append(grid_choice1)
                    player2_piece_location[player2_piece_location.index(grid_choice1)] = "X"
                    player1_game_board[player1_game_board.index(grid_choice1)] = "X"
                    print(word_hit)
                    player1_turn = False
                # Displaying 0 if attacker choice is incorrect
                else:
                    player1_attack_choice.append(grid_choice1)
                    player1_game_board[player1_game_board.index(grid_choice1)] = "O"
                    print(word_miss)
                    player1_turn = False
            # When player1 gives the already taken grid value
            else:
                print("Tile Already Attacked, Try Again")
        # user entered choice  not existed in the board
        else:
            print("Invalid Entry, Try Again")

    check_suken_ship(player2, player1_attack_choice)
    player1_winner = check_winner(player2)
    if player1_winner == True:
        game_complete = True
        break

    while player2_turn == True:
        # During the turn of player2 displaying the guess board of player1
        player1_turn = True
        print("-------------------------------------------------------------------------")
        print_updated_board(board1, player2_game_board)
        # for displaying the alive or sunk ships status to player2
        ship_statues(player1)
        print(p2name + "'s Turn")
        # Getting the user input to start the attack
        grid_choice2 = input("Pick Tile to Attack: ").upper()
        # user entered choice exists in the board
        if grid_choice2 in board:
            # player2 entered valid new grid_choice
            if grid_choice2 not in player2_attack_choice:
                # Displaying x if player2 choice is correct
                if grid_choice2 in player1_piece_location:
                    player2_attack_choice.append(grid_choice2)
                    player1_piece_location[player1_piece_location.index(grid_choice2)] = "X"
                    player2_game_board[player2_game_board.index(grid_choice2)] = "X"
                    print(word_hit)
                    player2_turn = False
                # Displaying 0 if attacker choice is incorrect
                else:
                    player2_attack_choice.append(grid_choice2)
                    player2_game_board[player2_game_board.index(grid_choice2)] = "O"
                    print(word_miss)
                    player2_turn = False
            # When player2 gives the already taken grid value
            else:
                print("Tile Already Attacked, Try Again")
        # user entered choice  not existed in the board
        else:
            print("Invalid Entry, Try Again")

    check_suken_ship(player1, player2_attack_choice)
    player2_winner = check_winner(player1)
    if player2_winner == True:
        game_complete = True
        break

######## END GAME ########
# displaying the player1 name if he is winner and printing his name in txt file
if player1_winner == True:
    print(p1name + " Wins!")
    # Opening and writing winner player1 name in the txt file
    with open("battelship_text.txt", "a") as o:
        o.write(player_1_name)
        o.close()
# displaying the player2 name if he is winner
else:
    print(p2name + " Wins!")
    # Opening and writing winner player2 name in the txt file
    with open("battleship_text.txt", "a") as o:
        o.write(player_2_name)
        o.close()

# Final display of the both player boards to eachother
final_answer = input("View Boards? y or n: ").upper()
final_answer_done = False
while final_answer_done == False:
    # when user enter to view the board as Y the list of boards displays
    if final_answer == "Y":
        print(p1name + "'s Board")
        print_updated_board(board1, player1_board_list)
        print(p2name + "'s Board")
        print_updated_board(board2, player2_board_list)
        final_quit = input("Press Enter to Quit the game")
        final_answer_done = True
    elif final_answer == "N":
        final_answer = True
        break
    # when user enter to view the board as N
    else:
        print("Invalid Input Try Again")
print("GAME OVER")
