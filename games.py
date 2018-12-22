AA = 'Adam'
Aaron = ASU = 'Aaron S'
Ajay = AJAY = 'Ajay'
Alex = A = ALEX = AJ = 'Alex'
ANDREW = AH = 'Andrew H'
Andy = ANDY = AN = AD = 'Andy'
AL = ANGELO = 'Angelo'
ARM = ARMIJIT = 'Armijit'
Brendan = B = BR = BRENDAN = BD = R = 'Brendan'
CC = 'Chloe'
Craig = K = CW = CRAIG = KRAG = KRAIG = CR = CRAG = KW = KV = KR = 'Craig'
Damian = DAM = 'Damian'
Dylan = DYL = DY = DN = 'Dylan'
ED = 'Ed'
Elliot = E = ELLIOT = EC = EL = EG = 'Elliot'
Greg = G = GH = GR = GRE = GREG = 'Greg'
Jack = JACK = JW = 'Jack'
Jamie = JA = JAMIE = JH = H = JAM = JN = JM = 'Jamie'
JC = 'Justin'
JK = 'Jordan'
JOSH = JS = 'Josh'
JON = 'Jonathon'
Jingbo = J = JING = JB = JI = JINGBO = JIN = JJ = 'Jingbo'
LAX = LK = 'Lakshey'
Maya = M2 = MA = MAYA = MJ = MAJ = 'Maya'
Michael = M = MC = CABS = 'Michael C'
MichaelLee = ML = MLE = L = 'Michael L'
Milos = D = MD = MI = MIL = MILOS = 'Milos'
Muhammad = MU = 'Muhammad'
Nick = N = NICK = NICHOLAS = NC = NI = NG = 'Nick C'
NW = 'Nick W'
Omid = O = OM = OV = 'Omid'
RAJ = 'Rajan'
S = 'Scott'
Simon = SH = 'Simon H'
SimonL = SL = SLG = SIML = SIMONL = SLE = SIMON = SLC = SIM = 'Simon L'
TIM = 'Tim'
Will = W = WD = WILL = 'Will D'
V = VS = 'Vorakot'

# Unknown players.
AW = 'AW'
AS = 'AS'
ER = 'ER'
KN = 'KN'
NE = 'NE'
HW = 'HW'
HS = 'HS'
SF = 'SF'

inActivePlayers = [AA, Aaron, ANDREW, Andy, CC, DAM, DYL, JK, JON, LK, MAYA, ML, NW, RAJ, S, SH, TIM, WILL, V, AW, AS, ER, KN, NE, HW, HS, SF]

# Games.
doubles = [
    [Elliot, JC, 7, Brendan, Maya, 10],
    [Elliot, JC, 10, Brendan, Maya, 8],

    # 1
    [Jamie, Milos, 7, Omid, Jingbo, 10],
    [Elliot, Jingbo, 6, Jamie, Milos, 10],
    [Nick, Brendan, 7, Jamie, Milos, 10],
    [Jingbo, JC, 3, Jamie, Brendan, 10],
    [JC, Michael, 2, Brendan, Jamie, 10],
    [Brendan, Jingbo, 10, Michael, JC, 8],
    [Brendan, Jingbo, 10, Michael, Elliot, 8],
    [Jingbo, Brendan, 10, Michael, Elliot, 6],
    [Jingbo, Brendan, 10, JC, Elliot, 8],
    [Jamie, Milos, 7, Omid, Jingbo, 10],
    [Elliot, Jingbo, 6, Jamie, Milos, 10],
    [Nick, Brendan, 7, Jamie, Milos, 10],
    [Jingbo, JC, 3, Jamie, Brendan, 10],
    [JC, Michael, 2, Brendan, Jamie, 10],
    [Brendan, Jingbo, 10, Michael, JC, 8],
    [Brendan, Jingbo, 10, Michael, Elliot, 8],
    [Jingbo, Brendan, 10, Michael, Elliot, 6],
    [Jingbo, Brendan, 10, JC, Elliot, 8],
    [Elliot, Brendan, 4, Jamie, Michael, 10],
    [Elliot, Michael, 2, Jamie, Jingbo, 10],
    [Michael, Jamie, 6, Brendan, Jingbo, 10],
    [Milos, Michael, 9, JC, M2, 10],
    [Jingbo, Brendan, 10, JC, M2, 3],

    # 2
    [Brendan, Jingbo, 10, Elliot, Milos, 1],
    [Brendan, Jingbo, 10, Elliot, Milos, 3],
    [Brendan, Jingbo, 10, Elliot, Milos, 3],
    [Jingbo, Michael, 10, Elliot, Brendan, 4],
    [Nick, Jamie, 7, Jingbo, Michael, 10],
    [MichaelLee, Brendan, 10, JC, Michael, 9],
    [Elliot, Jingbo, 10, Craig, Simon, 3],
    [Jamie, Milos, 10, JC, Michael, 7],
    [Elliot, Milos, 10, Brendan, MichaelLee, 7],
    [Jingbo, Milos, 10, Jamie, Brendan, 7],
    [Jamie, Michael, 10, Jingbo, Brendan, 7],
    [SimonL, Greg, 6, Jamie, JC, 10],
    [Michael, Greg, 10, Jamie, JC, 6],
    [Michael, Jingbo, 3, Jamie, JC, 7],

    # 3
    [Elliot, Brendan, 9, Jingbo, Michael, 10],
    [Jingbo, Michael, 8, Jamie, Brendan, 10],
    [MD, Michael, 10, JC, Omid, 9],
    [Elliot, Jamie, 10, Milos, Brendan, 5],
    [Elliot, Jamie, 8, Milos, Brendan, 10],
    [Michael, Jingbo, 9, Milos, Brendan, 10],
    [Michael, JC, 7, Elliot, Milos, 10],
    [Michael, JC, 10, Elliot, Milos, 8],
    [Elliot, Michael, 6, Jingbo, MA, 10],
    [Elliot, Michael, 10, Milos, Craig, 5],
    [Elliot, Brendan, 7, Milos, Jingbo, 10],
    [Elliot, JC, 6, Jingbo, Michael, 10],
    [Elliot, JC, 5, Jingbo, Michael, 10],
    [Jingbo, Michael, 10, Jamie, Brendan, 4],
    [Jamie, Brendan, 10, Jingbo, Michael, 3],
    [Michael, Jingbo, 10, Brendan, Elliot, 8],

    [Elliot, Jamie, 10, Nick, Greg, 4],
    [Elliot, Jamie, 10, Nick, Greg, 4],
    [Elliot, Jamie, 10, Brendan, Michael, 3],
    [Michael, Brendan, 1, Jamie, Craig, 10],
    [Craig, Elliot, 3, Brendan, Michael, 10],
    [Elliot, Nick, 7, Brendan, Michael, 10],
    [Elliot, Nick, 5, Brendan, Michael, 10],
    [Nick, Greg, 10, JC, Jamie, 8],
    [Nick, Greg, 6, JC, Jamie, 10],
    [Brendan, Elliot, 9, MI, ML, 10],
    [Brendan, Elliot, 10, MI, ML, 5],
    [Brendan, Elliot, 10, MI, ML, 8],
    [Jamie, Elliot, 10, Greg, Nick, 5],
    [Elliot, Jingbo, 10, Jamie, Omid, 7],
    [Elliot, Brendan, 10, Jamie, Milos, 9],
    [Jingbo, Nick, 6, Brendan, Elliot, 10],
    [Brendan, SL, 9, Michael, JC, 10],
    [Brendan, SL, 10, Michael, JC, 9],
    [Brendan, SL, 10, Michael, JC, 9],
    [Jamie, Maya, 10, Elliot, Jingbo, 9],
    [Elliot, Michael, 10, Maya, Jamie, 6],

    # 4
    [Elliot, Brendan, 10, Maya, Jingbo, 7],
    [Elliot, Jingbo, 10, Alex, Jamie, 3],
    [Michael, Milos, 5, Elliot, Jingbo, 10],
    [Michael, Milos, 10, Elliot, Jingbo, 9],
    [Jingbo, Michael, 10, Elliot, Maya, 5],
    [Elliot, Greg, 4, Jamie, Michael, 10],
    [Jingbo, Maya, 4, Elliot, Michael, 10],
    [Elliot, Michael, 10, Maya, Jingbo, 9],
    [Brendan, Jamie, 10, Elliot, Jingbo, 5],
    [Brendan, Jamie, 10, Elliot, Jingbo, 8],
    [MC, SLG, 10, JC, GH, 9],
    [MC, SLG, 10, Jingbo, GH, 9],
    [MC, SLG, 10, MLE, Milos, 7],
    [MC, Jingbo, 10, MLE, Milos, 8],
    [Elliot, JC, 7, Jamie, Michael, 10],
    [Brendan, Michael, 10, JC, Alex, 5],
    [Elliot, Will, 3, Brendan, Michael, 10],
    [Elliot, ML, 10, Michael, Milos, 5],
    [Elliot, ML, 4, Michael, Milos, 10],
    [Will, Elliot, 7, Michael, Craig, 10],

    # 5
    [E, M, 10, JA, B, 5],
    [G, B, 10, E, M, 8],
    [E, JC, 8, B, J, 10],
    [JH, Omid, 10, Milos, Craig, 1],
    [JH, Omid, 10, Milos, Craig, 4],
    [JH, Omid, 10, Milos, SLG, 4],
    [JH, Omid, 10, Milos, SLG, 6],
    [JH, JC, 10, B, Nick, 1],
    [JH, JC, 10, B, Nick, 3],
    [E, JA, 10, J, G, 5],
    [E, JA, 4, J, G, 10],
    [JA, Jack, 10, E, B, 1],
    [JH, Jack, 10, E, B, 5],
    [MI, JA, 10, B, N, 1],
    [JC, MC, 9, K, MD, 10],
    [JC, MC, 7, K, ML, 10],
    [JC, MC, 10, MD, ML, 6],
    [JC, MC, 10, O, MD, 7],
    [JC, MC, 10, O, MD, 8],
    [D, O, 10, M, JC, 8],
    [MA, E, 2, B, O, 10],

    # 6
    [E, JH, 10, N, G, 4],
    [E, JH, 10, N, G, 4],
    [E, JH, 10, B, M, 3],
    [MC, BR, 1, JH, K, 10],
    [K, E, 3, B, M, 10],
    [E, N, 7, B, M, 10],
    [E, N, 5, B, M, 10],
    [N, G, 10, JC, JAMIE, 8],
    [N, G, 6, JC, JAMIE, 10],
    [B, E, 9, MI, ML, 10],
    [B, E, 10, MI, ML, 5],
    [B, E, 10, MI, ML, 8],
    [JH, E, 10, GR, NICK, 5],
    [MAYA, E, 9, B, O, 10],
    [E, J, 10, JA, O, 7],
    [E, B, 10, JA, MI, 9],
    [J, N, 6, B, E, 10],
    [B, SL, 9, MC, JC, 10],
    [B, SL, 10, MC, JC, 9],
    [B, SL, 10, MC, JC, 7],
    [JA, MA, 10, E, J, 9],
    [E, M, 10, MA, JA, 6],

    # 7
    [G, M, 8, JC, H, 10],
    [G, M, 10, JC, H, 9],
    [E, L, 10, B, D, 9],
    [E, B, 10, E, JACK, 6],
    [D, J, 10, E, B, 2],
    [H, JC, 10, D, J, 9],
    [G, M, 10, D, JC, 3],
    [G, M, 10, H, JC, 2],
    [G, A, 10, B, JC, 4],
    [G, A, 10, B, JC, 4],
    [E, MAYA, 10, B, O, 3],
    [E, MAYA, 10, B, O, 4],
    [E, MAYA, 10, B, JACK, 8],
    [E, MAYA, 9, B, JACK, 10],
    [E, MAYA, 7, B, JACK, 10],
    [E, MAYA, 4, B, JACK, 10],
    [E, MAYA, 5, B, JACK, 10],
    [MC, MD, 10, JC, CW, 7],
    [MC, MD, 10, JC, CW, 3],
    [MC, MD, 4, MLE, H, 10],

    # 8
    [E, JA, 6, J, B, 10],
    [E, JA, 10, J, B, 8],
    [E, JA, 10, K, W, 2],
    [E, JA, 10, MI, B, 5],
    [B, MD, 10, G, A, 8],
    [WILL, H, 10, CRAIG, NICHOLAS, 4],
    [E, G, 7, J, MI, 10],
    [G, D, 10, B, L, 4],
    [G, D, 10, B, L, 1],
    [B, M, 10, ML, MIL, 8],

    # 9
    [JC, MI, 10, B, JACK, 9],
    [MI, ML, 10, B, JACK, 5],
    [MI, ML, 10, B, JACK, 4],
    [M, G, 10, ELLIOT, SIMONL, 6],
    [M, G, 10, ELLIOT, SIMONL, 8],
    [M, G, 10, JAMIE, JC, 6],
    [M, G, 4, JAMIE, JC, 10],
    [E, MI, 3, J, MLE, 10],
    [G, MI, 10, JC, SLG, 1],
    [G, MI, 10, JC, SLG, 1],
    [B, N, 10, E, J, 3],
    [JAMIE, DYL, 10, B, MD, 9],
    [E, JC, 10, B, DY, 7],
    [E, JC, 3, B, JAMIE, 10],
    [E, JC, 2, B, JAMIE, 10],
    [E, B, 0, JC, JAMIE, 10],
    [G, ANDY, 10, WILL, JK, 3],
    [E, J, 1, B, N, 10],
    [E, J, 9, B, N, 10],
    [E, B, 7, MI, J, 10],
    [JAM, E, 10, B, G, 9],
    [JAM, MD, 10, JC, SLG, 7],
    [E, JAM, 4, J, B, 10],
    [E, JAM, 2, J, B, 10],
    [B, K, 4, JC, DY, 10],
    [MD, JING, 10, B, NICK, 4],
    [MD, JING, 10, B, NICK, 2],
    [B, ED, 10, E, KRAG, 5],
    [SIML, MD, 10, ML, OM, 4],
    [B, E, 10, A, MI, 5],
    [B, E, 6, J, MI, 10],
    [B, E, 8, J, MI, 10],
    [MA, E, 2, JAM, N, 10],
    [E, JACK, 10, N, A, 5],
    [G, ALEX, 10, SLG, NICK, 1],
    [MLE, JACK, 10, ALEX, SIML, 7],
    [JAM, SLG, 10, GRE, NICK, 9],
    [JAM, GRE, 10, J, E, 7],
    [E, J, 10, MAYA, JAM, 6],

    # 10
    [SLG, MD, 10, JC, ML, 6],
    [JC, ML, 10, SLG, MD, 3],
    [JC, MD, 10, DN, NW, 4],
    [JC, MD, 10, AJ, DN, 4],
    [JC, JH, 10, MD, DN, 5],
    [JC, JH, 10, EC, DN, 2],
    [JC, JH, 10, EC, DN, 3],
    [JC, JH, 10, JB, AJ, 3],
    [J, D, 10, A, E, 3],
    [JAM, E, 9, J, JC, 10],
    [A, RAJ, 10, MAYA, V, 5],
    [E, B, 10, G, N, 7],
    [JH, JC, 10, NC, B, 2],
    [JH, JC, 10, NC, B, 2],
    [SLG, MIL, 10, B, NI, 5],
    [SLG, MIL, 8, B, NI, 10],
    [G, JAMIE, 10, J, B, 3],
    [G, JAMIE, 9, J, B, 10],
    [JC, JAMIE, 10, MI, G, 7],
    [J, N, 9, SLG, MIL, 10],
    [JAM, J, 10, E, MAYA, 5],
    [MA, G, 3, E, J, 10],
    [E, J, 10, JC, JAM, 9],
    [E, J, 9, JC, JAM, 10],
    [N, G, 3, B, J, 10],
    [N, G, 5, B, J, 10],
    [JC, JH, 10, GH, NC, 3],
    [JC, JH, 10, GH, NC, 4],
    [JC, JH, 10, GH, NC, 5],

    [MILOS, SLG, 10, NICK, BRENDAN, 6],
    [MILOS, SLG, 10, NICK, BRENDAN, 7],
    [MILOS, SLG, 10, NICK, JAMIE, 6],

    # 11
    [E, B, 10, JC, N, 7],
    [B, JW, 10, JC, N, 8, ],
    [E, MA, 8, JACK, MLE, 10],
    [MLE, JACK, 3, JC, NICK, 10],
    [MLE, JACK, 10, JC, NICK, 6],
    [MLE, JACK, 6, JC, NICK, 10],
    [E, B, 10, JC, NICK, 8],
    [E, B, 10, JC, NICK, 5],
    [G, NICK, 10, MILOS, SLG, 8],
    [JAMIE, MC, 10, G, NICK, 6],
    [G, SLG, 9, JAMIE, NICK, 10],
    [G, SLG, 7, JAMIE, NICK, 10],
    [SLG, MI, 7, JI, N, 10],
    [EC, MC, 10, MD, NC, 7],
    [E, M, 10, K, N, 7],
    [E, M, 10, MI, N, 8],
    [NC, MD, 5, SLG, MC, 10],
    [NC, MD, 8, SLG, MC, 10],
    [E, JC, 10, MI, MLE, 6],
    [E, N, 3, MI, JC, 10],
    [J, MLE, 10, M, JC, 7],
    [E, B, 10, MC, MIL, 3],
    [E, B, 10, JA, JC, 6],
    [E, B, 10, M, SLG, 9],
    [JH, MC, 10, S, EC, 1],
    [E, B, 10, J, M, 7],

    # 12
    [J, MI, 10, E, B, 6],
    [J, MI, 10, E, B, 6],
    [G, SLG, 10, JAMIE, JC, 1],
    [G, SLG, 7, JAMIE, JC, 10],
    [B, J, 10, JC, JAMIE, 9],
    [B, J, 10, E, MAYA, 4],
    [E, B, 10, J, MA, 6],
    [G, SLG, 10, E, B, 5],
    [G, SLG, 10, E, B, 5],
    [G, SLG, 10, E, B, 5],
    [JC, EC, 10, BR, MC, 6],
    [JC, EC, 9, BR, MC, 10],
    [JC, EC, 1, BR, MC, 10],
    [JC, JH, 10, BR, MC, 6],
    [JC, JOSH, 4, BR, MC, 10],
    [MD, MC, 10, NC, SLG, 8],
    [MD, MC, 10, NC, SLG, 6],
    [MD, MC, 10, NC, SLG, 6],
    [MD, MC, 10, CW, NW, 2],
    [E, M, 8, D, JC, 10],
    [E, M, 10, D, JC, 6],
    [E, B, 10, MI, O, 4],
    [E, B, 10, MI, JACK, 8],
    [E, B, 9, MI, J, 10],
    [E, B, 10, N, J, 6],
    [E, B, 4, N, J, 10],
    [JC, N, 10, E, B, 8],

    # 13
    # SLC,GH,10,JC,
    [B, MC, 10, NC, JC, 1],
    [MD, JAMIE, 10, MC, B, 5],
    [GH, JC, 10, MC, MILOS, 3],
    [NC, B, 10, MC, MILOS, 7],
    [NC, EL, 9, MC, MILOS, 10],
    [GH, MC, 10, JACK, BRENDAN, 5],
    [GH, MC, 10, NC, MILOS, 3],
    [GH, E, 2, JINGBO, BRENDAN, 10],
    [JAMIE, MC, 8, JINGBO, BRENDAN, 10],
    [AW, MC, 10, CW, EC, 5],
    [SL, MD, 10, NC, JC, 6],
    [SL, MD, 10, NC, JC, 8],
    [E, B, 10, M, MA, 7],
    [BR, MJ, 4, MC, EC, 10],
    [BR, MJ, 8, MC, EC, 10],
    [BR, JAM, 10, JC, MD, 2],
    [BR, JAM, 10, NC, MC, 7],
    [MC, GH, 10, J, NC, 4],
    [MC, GH, 10, J, NC, 3],
    [MC, MD, 10, BR, AJ, 4],
    [MC, MD, 10, EC, JC, 7],
    [MC, AJ, 10, BR, JC, 8],
    [JC,B,10,J,CRAIG,7],
    [B,JOSH,10,A,E,9],
    [JC, G, 10, MAYA, JOSH, 3],
    [B, JH, 10, MD, MC, 7],
    [MILOS, J, 10, B, A, 4],
    [MILOS, J, 10, B, A, 3],
    [MD, J, 10, E, JACK, 8],
    [E, M, 10, G, SLE, 9],
    [E, MC, 10, BR, JC, 4],
    [E, MC, 6, JH, J, 10],
    [B, JC, 2, JH, J, 10],
    [E, M, 10, JC, B, 9],
    [E, M, 10, NC, SLE, 7],
    [JAMIE, MD, 10, GREG, BR, 9],
    [JAMIE, MD, 10, GREG, BR, 9],
    [JC, NC, 10, MLE, JW, 0],
    [J, MD, 6, E, G, 10],
    [J, MD, 10, E, G, 4],
    [J, MD, 10, JC, A, 4],

    # 14
    [E, B, 8, M, J, 10],
    [M, JAMIE, 10, GR, JC, 9],
    # MG?
    # [MC, JW, 10, HM, JI, 7],
    [J, JC, 10, JACK, M, 4],
    [J, E, 8, M, B, 10],
    [JC, JAMIE, 10, M, B, 9],
    [JC, SIMON, 4, NC, GH, 10],
    [JC, SIMON, 4, NC, GH, 10],
    [E, B, 7, NC, GH, 10],
    [JC, K, 10, E, B, 9],
    [MC, KRAIG, 7, B, MIL, 10],
    [MC, KRAIG, 4, B, MIL, 10],
    [MC, JC, 4, B, MIL, 10],
    # MC,JC,2,
    [ML, JC, 9, S, M, 10],
    [MD, NC, 4, S, M, 10],
    [J, B, 4, E, JH, 10],
    [J, B, 9, E, JH, 10],
    [J, B, 10, JH, JC, 9],
    [E, M, 10, K, V, 3],
    [E, K, 10, JC, M, 5],
    [E, K, 5, JC, M, 10],
    [E, JOSH, 10, CABS, JC, 9],
    [E, JOSH, 10, CABS, JC, 4],
    [E, JOSH, 5, CABS, JC, 10],
    [BR, MC, 10, MD, GH, 9],
    [MC, AJ, 10, BR, MC, 9],
    [ML, GH, 9, BR, MC, 10],
    [B, MILOS, 5, MC, AJ, 2],
    [J, MILOS, 10, B, MC, 6],
    [J, M, 10, JAMIE, NICK, 2],
    [E, JC, 6, MI, J, 10],
    [JC, MC, 10, SLG, GH, 8],
    [JC, MC, 6, N, JINGBO, 10],
    [G, CR, 9, N, JIN, 10],
    [G, SLG, 10, N, MC, 3],
    [G, SLG, 10, N, EC, 2],
    [G, SLG, 10, BRENDAN, EC, 5],
    [JC, MC, 10, EC, B, 5],
    [JC, MC, 6, AJ, B, 10],
    [G, EC, 10, MC, B, 5],
    [G, E, 10, M, B, 8],

    # 15
    [E, M, 10, B, JA, 6],
    [E, M, 10, MI, MLE, 7],
    [E, M, 10, MI, MLE, 4],
    [E, M, 4, JC, JAM, 10],
    [G, A, 10, JING, BRENDAN, 5],
    [G, A, 8, JAM, JC, 10],
    [BR, JW, 6, JAM, JC, 10],
    [BR, JC, 10, E, JW, 3],
    [GH, NC, 10, BR, JACK, 2],
    [GH, NC, 10, BR, JACK, 8],
    [MD, J, 9, E, B, 10],
    [MD, J, 10, B, E, 9],
    [MD, J, 10, ML, JACK, 8],
    [MD, J, 10, ML, JACK, 1],

    [SLG, JH, 10, EC, JOSH, 2],
    [SLG, JH, 10, EC, JOSH, 5],
    [JOSH, SL, 7, EC, J, 10],
    [B, JC, 10, EC, J, 8],
    [AN, N, 10, ALEX, CW, 7],
    [JC, J, 10, E, MD, 3],
    [JC, J, 10, E, MD, 5],
    [MD, J, 9, JH, G, 6],
    [J, E, 9, G, MC, 10],
    [B, MIL, 10, E, JC, 6],
    [J, MC, 10, BR, A, 3],
    [J, B, 10, MD, ML, 9],
    [ML, MD, 10, B, A, 5],

    [MD, N, 10, B, J, 9],
    # [MD,N,10,E],
    [MD, N, 10, JC, A, 6],
    [J, B, 10, E, A, 1],
    [J, A, 10, E, B, 8],
    [J, A, 10, E, B, 9],
    [GH, BR, 10, EC, JACK, 2],
    [GH, JACK, 10, EC, BR, 4],
    [GH, JACK, 10, EC, BR, 6],
    [JC, G, 10, NC, MD, 4],
    [J, MD, 10, B, AL, 4],
    [A, EL, 8, J, MD, 10],

    # 16
    [SLG, GH, 10, BD, ALEX, 4],
    [SLG, JC, 10, A, CRAG, 8],
    [GH, NC, 10, MD, MC, 6],
    [GH, JC, 10, MD, MC, 8],
    [GH, CC, 10, JC, MC, 4],
    [J, MD, 10, JW, B, 5],
    [J, MD, 10, JW, B, 2],
    [BR, JAMIE, 10, MC, JINGBO, 9],
    [BR, JAMIE, 10, EC, JACK, 3],
    [BR, JAMIE, 10, NC, SLG, 1],
    [BR, JAMIE, 10, NC, SLG, 4],
    [B, JW, 10, E, SLG, 9],
    [B, JW, 4, E, SLG, 10],
    [B, JW, 10, E, SLG, 8],
    [E, G, 10, E, M, 7],
    [E, G, 9, B, M, 10],

    [GH, MC, 10, JINGBO, MD, 6],
    [JW, AJ, 10, ML, MAYA, 7],
    [JAMIE, AJ, 10, BR, JW, 4],
    [JAMIE, AJ, 10, BR, JW, 9],
    [GH, SLG, 10, NC, MC, 6],
    [GH, SLC, 10, JAMIE, MC, 7],
    [GH, SLG, 10, BD, JW, 4],
    [AJ, N, 8, B, JW, 10],
    [JH, JC, 10, B, JW, 6],
    [JH, JC, 10, E, AJ, 4],
    [JH, JC, 10, E, AJ, 2],
    [GH, NC, 9, MC, SLG, 10],
    [M, J, 10, E, B, 7],
    [JC, SLG, 10, NC, GH, 8],
    [B, M, 10, MILOS, AJ, 3],
    [GH, SLG, 10, J, JC, 7],

    [B, MD, 10, E, MC, 9],
    [B, MD, 10, E, MC, 6],
    [GH, MC, 10, NC, BD, 2],
    [GH, MC, 10, SLG, JC, 8],
    [VS, SLG, 10, MJ, CC, 8],
    [MD, ML, 10, MC, JC, 5],
    [MD, ML, 10, MC, JC, 7],
    [E, MA, 10, JACK, B, 8],
    [J, ML, 6, JA, N, 10],
    [B, JW, 7, JA, N, 10],
    [E, MJ, 3, JA, N, 10],
    [J, MC, 6, JA, N, 10],
    [GH, SLG, 10, JAMIE, MD, 7],
    [GH, SLG, 10, JC, CRAG, 3],
    [MC, SLG, 6, JC, JAM, 10],
    [GH, SLG, 10, JINGBO, EC, 8],

    # 17
    [J, MD, 10, JC, JACK, 2],
    [J, MD, 10, E, ALEX, 8],
    [J, MD, 10, ML, B, 0],
    [J, MD, 8, JAMIE, JN, 10],
    [B, JACK, 10, E, AD, 6],
    [B, JACK, 10, E, AD, 3],
    [B, JACK, 10, E, AD, 9],
    [GH, ALEX, 10, JC, SLG, 7],
    [GH, ALEX, 10, JC, SLG, 3],
    [JC, G, 10, MD, N, 1],
    [GH, JW, 10, NC, JC, 4],
    [B, ML, 10, JW, MD, 7],
    [B, ML, 10, JW, MD, 7],

    [GH, NC, 10, JH, JC, 9],
    [JAM, AJ, 10, MD, JW, 2],
    [E, B, 10, JAM, A, 7],
    [GH, SF, 10, SLG, DN, 5],
    [GH, SF, 9, SLG, DN, 10],
    [E, B, 10, MI, MA, 0],
    [MD, JB, 10, E, B, 3],
    [GH, JC, 10, BR, MD, 4],
    [E, JC, 10, G, SIM, 7],
    [E, JC, 10, ED, AL, 7],
    [E, JC, 10, S, SLE, 4],
    [ML, AL, 10, JC, SLG, 8],
    [ML, AL, 5, JC, SLG, 10],
    [ML, MD, 10, B, JW, 6],
    [ML, MD, 6, E, JH, 10],
    [E, JH, 10, G, JIN, 9],

    [GH, SLG, 10, ML, MD, 6],
    [GH, SLG, 10, JC, JJ, 6],
    [GH, SLG, 10, JC, EC, 3],
    [GH, SLG, 10, JC, EC, 5],
    [SLG, MD, 10, GH, NC, 8],
    [GH, ML, 10, MD, BR, 6],
    [JH, JC, 10, MD, A, 2],
    [JH, ML, 10, BR, JW, 5],
    [JB, MD, 10, ML, EL, 8],
    [JC, SLG, 10, GH, NC, 9],
    [JW, J, 10, E, MAJ, 5],
    [JW, J, 10, E, MAJ, 3],
    [E, MI, 10, J, B, 3],
    [E, MI, 9, J, B, 3],
    [E, MI, 3, J, B, 10],

    # 18
    [GH, CW, 10, JC, JH, 7],
    [GH, JC, 10, BR, EC, 6],
    [JC, ML, 10, MD, N, 4],
    [BR, ML, 4, JAMIE, JINGBO, 10],
    [JC, GH, 10, BR, AJ, 4],
    [JC, GH, 10, BR, AJ, 3],
    [A, BR, 10, JACK, M, 8],
    [J, B, 10, JACK, E, 7],
    [J, B, 10, JACK, E, 2],
    [GH, SLG, 10, JACK, E, 8],
    [GH, MD, 10, JH, AD, 3],
    [GH, MD, 10, J, SH, 2],
    [MD, SH, 2, J, R, 10],
    [MD, J, 10, B, JW, 6],

    [MD, ML, 3, JW, B, 10],
    [JW, BR, 10, MILOS, AJ, 4],
    [JW, BR, 7, MILOS, AJ, 10],
    [J, E, 10, G, SL, 9],
    [JH, JC, 10, EC, MD, 1],
    [JH, JC, 10, BR, ANGELO, 5],
    [B, J, 10, MD, JW, 7],
    [A, ML, 4, MD, J, 10],
    [NICK, JC, 6, MD, J, 10],
    [NICK, JC, 8, MD, J, 10],
    [B, E, 6, JW, J, 10],
    [E, M, 3, JW, B, 10],
    [B, KV, 10, AJ, JACK, 5],
    [GH, SLG, 10, JC, NC, 6],
    [GH, NC, 10, JH, MD, 4],

    # GH,N,10,
    [B, MD, 10, JB, K, 3],
    [B, MD, 10, E, AJ, 4],
    [E, AL, 7, N, GH, 10],
    [GH, NC, 10, BR, AJ, 6],
    [GH, JC, 10, BR, EC, 4],
    [GH, JC, 10, BR, EC, 3],
    [GH, JC, 10, BR, EC, 5],
    [E, B, 10, AL, JC, 8],
    [B, AL, 10, E, JC, 7],
    [SLG, MD, 10, NC, GH, 9],
    [BR, JW, 10, GH, MD, 5],
    [BR, MD, 6, JH, JC, 10],
    [EC, A, 4, JH, JC, 10],
    [BR, MD, 9, JH, JC, 10],
    [MD, ML, 10, JW, J, 8],

    # 19
    [J, E, 10, JC, MD, 8],
    [GH, SLG, 10, NG, JH, 5],
    [GH, SLG, 10, BR, EC, 9],
    [E, JW, 10, B, A, 2],
    [E, JACK, 8, B, A, 10],
    [GH, BR, 10, EG, JACK, 5],
    [GH, BR, 10, EC, JACK, 3],
    [GH, BR, 10, MC, JACK, 5],
    [GH, BR, 10, MC, NC, 8],
    [JH, J, 10, BR, MC, 7],
    [JH, MC, 10, JW, MLE, 7],
    [NC, MD, 10, ML, JW, 0],
    [B, NICK, 10, MC, MD, 9],
    [JC, MIL, 9, BR, MC, 10],

    [JW, AJ, 6, JC, MC, 10],
    [NC, EC, 6, JC, MC, 10],
    [JW, AS, 6, JC, MC, 10],
    [EC, KW, 1, JC, ML, 10],
    [EC, KW, 4, JC, ML, 10],
    [NC, SLG, 4, JC, MC, 10],
    [NC, SLG, 9, JC, MC, 10],
    [JW, MD, 10, B, MC, 6],
    [JW, MD, 10, B, MC, 5],
    [GH, JC, 10, MD, JW, 1],
    [JACK, B, 10, JC, GH, 2],
    [BR, JW, 5, JC, JH, 10],
    [J, JW, 6, JH, JC, 10],
    [J, JH, 10, MC, E, 4],
    [MC, JC, 8, SLG, GH, 10],

    [J, JH, 10, JC, MC, 5],
    [AJ, JW, 2, GH, SLG, 10],
    [J, JC, 10, G, SL, 4],
    [J, JC, 10, G, N, 8],
    [JC, MC, 10, MD, EC, 8],
    [JC, MC, 9, MD, J, 10],
    [J, ED, 10, MD, JW, 9],
    [J, ED, 10, MD, JW, 9],
    [E, B, 10, MC, JW, 3],
    [E, G, 10, B, JACK, 8],
    [JW, B, 10, JC, ML, 6],
    [JW, B, 10, JC, ML, 4],
    [GH, NC, 10, J, MC, 9],
    [MC, JC, 10, GH, SLG, 1],

    # 20
    [E, J, 10, JW, B, 6],
    [E, J, 10, JW, B, 3],
    [E, J, 10, JW, B, 9],
    [GH, MD, 10, JC, ML, 4],
    [JC, EC, 10, M, JW, 9],
    [JC, J, 10, MD, JW, 7],
    [JC, SLG, 10, GH, NC, 7],
    [B, JACK, 10, GH, NC, 4],
    [B, E, 3, J, HW, 10],
    [B, ED, 4, J, R, 10],
    [B, JW, 10, J, E, 8],
    [B, E, 4, J, JW, 10],
    [B, J, 9, JW, E, 10],
    [GH, JH, 10, MD, JC, 5],
    [GH, NC, 10, MD, JC, 7],

    [E, B, 10, NC, SLG, 4],
    [JC, GH, 10, BR, MD, 3],
    [J, E, 10, G, JC, 6],
    # [J, E, 4, G, JC, 4]
    [J, JC, 10, B, JW, 4],
    [J, JC, 8, B, JW, 10],
    [J, JC, 10, B, JW, 8],
    [J, JC, 10, B, JW, 7],
    [J, JC, 10, B, JW, 5],
    [J, JC, 10, B, JW, 9],
    [GH, JACK, 10, BR, JOSH, 3],
    [GH, JACK, 10, BR, JC, 7],
    [J, MD, 10, BR, JW, 6],
    [JC, SLG, 10, GH, NC, 1],
    [JC, J, 10, E, JW, 7],

    [JC, J, 10, B, JW, 9],
    [JC, J, 3, JM, G, 10],
    [JC, SLG, 10, EC, BR, 8],
    [JC, SLG, 10, EC, BR, 9],
    [J, MD, 10, JC, ML, 4],
    [J, MD, 8, JW, G, 10],
    [E, JC, 10, R, SLE, 6],
    [E, JC, 5, R, SLE, 10],
    [E, JC, 5, R, SLE, 10],
    [E, MAYA, 4, B, SLE, 10],
    [E, MAYA, 5, B, SLE, 10],
    [GH, NC, 10, JC, SLG, 9],
    [B, J, 10, E, MJ, 2],
    [E, J, 10, B, MJ, 6],

    # 21
    [GH, JC, 10, MD, J, 8],
    [BR, EC, 10, MC, GH, 3],
    [BR, EC, 10, MC, GH, 7],
    [B, JW, 4, J, E, 10],
    [B, JW, 10, J, JC, 5],
    [JH, MC, 10, MD, J, 8],
    [GH, MC, 10, JH, JC, 7],
    [MD, MC, 10, BR, JW, 7],
    [J, MC, 10, JC, G, 6],
    [J, MC, 2, B, JW, 10],
    [J, MC, 10, B, JW, 7],
    [J, MC, 10, JC, N, 5],
    [J, MC, 10, JC, N, 7],
    [GH, JC, 10, MD, MC, 5],
    [B, JH, 10, G, JC, 7],

    [NE, AJ, 6, SLG, MD, 10],
    [MD, SLG, 10, JC, MC, 6],
    [MD, SLG, 10, JC, MC, 8],
    [B, J, 10, JC, MD, 5],
    [MC, MD, 10, BR, JW, 8],
    [B, JW, 9, E, J, 10],
    [E, J, 7, G, JC, 10],
    [E, JW, 10, AJ, MI, 9],
    [E, B, 6, JW, JH, 10],
    [B, J, 8, JW, GH, 10],
    [B, E, 3, JW, J, 10],
    [B, E, 5, JW, J, 10],
    [CW, J, 10, V, MC, 7],
    [E, B, 7, J, KN, 10],
    [J, G, 6, MC, JH, 10],

    [JC, SLG, 10, GH, MD, 8],
    [GH, MC, 10, EC, M, 6],
    [GH, ER, 10, MC, AJ, 2],
    [GH, MC, 10, CW, EC, 3],
    [JW, MD, 10, J, B, 6],
    [JW, MD, 3, J, B, 10],
    [JW, MD, 6, J, B, 10],
    [JH, EC, 10, BR, MJ, 2],
    [GH, BR, 10, JC, EC, 1],
    [GH, EC, 10, BR, JC, 7],
    [BR, SLG, 10, E, KR, 2],
    [E, MC, 8, JW, JC, 10],
    [BR, MC, 10, JW, MC, 9],
    [BR, MC, 10, JW, E, 7],
    [B, MC, 7, J, G, 10],

    # 22
    [MC, G, 10, E, MI, 3],
    [MC, G, 10, E, MI, 4],
    [G, MC, 10, B, J, 8],
    [G, MC, 10, SLG, MD, 5],
    [E, ED, 10, MC, BR, 5],
    [MC, BR, 10, EC, MD, 4],
    [MC, BR, 5, EC, MD, 10],
    [MC, BR, 10, EC, MD, 8],
    [AJ, JW, 10, NC, JC, 9],
    [AJ, JW, 10, BR, EC, 2],
    [JC, JH, 10, MC, MD, 4],
    [J, MD, 10, MC, JC, 8],
    [JH, EC, 10, BR, JW, 2],

    [MC, JW, 10, JC, SLG, 8],
    [GH, JACK, 10, BR, EC, 2],
    [EC, MC, 10, BR, JW, 7],
    [GH, JS, 10, MC, MD, 8],
    [J, MC, 10, MD, ML, 9],
    [J, MC, 10, E, B, 6],
    [J, MC, 10, E, B, 4],
    [GH, NC, 10, JW, AL, 4],
    [JC, BR, 10, GH, AL, 8],
    [JC, SLG, 4, MC, MD, 10],
    [JC, NC, 10, MC, MD, 9],
    [JC, GH, 10, MC, MD, 4],
    [JC, MD, 6, MC, GH, 10],
    [BR, MC, 10, MD, AW, 6],
    [BR, MC, 10, MD, AW, 6],

    [JC, JH, 10, EC, J, 9],
    [E, J, 10, JW, M, 5],
    [J, JC, 10, MC, B, 5],
    [J, JC, 8, MC, B, 10],
    [J, JC, 10, MC, B, 9],
    [GH, BR, 10, MC, JH, 3],
    [GH, BR, 10, MC, JH, 1],
    [MJ, JC, 10, EC, MC, 9],
    [E, JC, 10, M, MI, 5],
    [B, MD, 10, JC, MC, 7],
    [A, GR, 5, J, B, 10],
    [MD, SLG, 10, EC, MC, 7],
    [MD, SLG, 10, EC, MC, 2],
    [MD, SLG, 10, NC, JC, 4],
    [J, MD, 10, B, MC, 3],

    # 23
    [JC, BR, 10, JACK, EC, 8],
    [E, NC, 2, JACK, BR, 10],
    [E, MD, 5, JACK, BR, 10],
    [MC, JB, 10, JW, E, 2],
    [E, MC, 10, JW, MJ, 6],
    [E, JW, 10, MC, MJ, 9],
    [E, JW, 10, MC, MJ, 5],
    [E, JW, 10, K, JC, 1],
    [E, JW, 10, K, JC, 6],
    [MD, JW, 7, JB, B, 10],
    [JB, MD, 9, JW, B, 10],
    [JC, MC, 5, JW, B, 10],
    [MC, ML, 7, J, AJ, 10],
    [JB, A, 10, E, JW, 7],

    [JB, A, 9, E, JW, 10],
    [JW, MC, 9, JW, JH, 10],
    [E, JW, 10, B, J, 9],
    [JW, JH, 10, MC, J, 8],
    [MD, JW, 7, MC, J, 10],
    [E, JH, 10, MC, J, 6],
    [AJ, MD, 8, B, JW, 10],
    [AJ, MD, 10, B, JW, 9],
    [B, MD, 10, E, JW, 4],
    [B, EC, 6, JW, AJ, 10],
    [LK, EC, 4, JW, AJ, 10],
    [AW, EC, 10, AJ, MC, 4],
    [AW, EC, 8, AJ, MC, 10],

    # 24
    [GH, JACK, 10, EC, JC, 3],
    [BR, MD, 10, JW, MC, 6],
    [BR, MD, 5, JC, GH, 10],
    [BR, JW, 10, AL, ML, 5],
    [BR, AJ, 10, JW, ML, 6],
    [BR, AJ, 10, MC, JC, 3],
    [BR, JW, 10, MC, AJ, 5],
    [BR, AJ, 10, MC, JC, 8],
    [BR, JW, 10, MC, AJ, 5],
    [JH, NC, 10, EC, JW, 6],
    [MC, AJ, 10, MD, ER, 5],
    [MC, AJ, 9, MD, ER, 10],
    [JC, JACK, 7, MD, ER, 10],
    [GH, JACK, 10, MD, MC, 7],

    [JC, BR, 10, GH, NC, 3],
    [JC, BR, 10, GH, NC, 4],
    [JC, BR, 8, GH, NC, 10],
    [JC, AJ, 8, MC, MD, 10],
    [JH, AJ, 10, MC, MD, 6],
    [BR, MD, 10, E, JINGBO, 8],
    [BR, MD, 10, ER, AJ, 6],
    [BR, MD, 10, NICK, MC, 7],
    [BR, MC, 10, EC, ER, 3],
    [BR, MC, 10, JINGBO, MD, 8],
    [MD, ML, 10, JC, NC, 7],
    [MD, MC, 10, J, BR, 9],
    [MD, MC, 7, JW, E, 10],
    [JH, JC, 10, JW, E, 5],
    [JB, JC, 10, EC, JACK, 3],

    [LAX, MC, 4, E, JW, 10],
    [E, JW, 10, M, B, 9],
    [E, JW, 5, M, B, 10],
    [E, JW, 10, M, B, 7],
    [E, JW, 9, M, B, 10],
    [B, AJ, 10, MC, MD, 8],
    [MD, EL, 10, MC, NC, 9],
    [J, JOSH, 10, B, MC, 8],
    [J, MC, 10, NC, JOSH, 1],
    [E, JW, 10, B, Aaron, 2],
    [E, BR, 10, JW, Aaron, 4],
    [E, JW, 10, MC, JI, 8],
    [E, JW, 6, MC, JI, 10],
    [JW, JH, 10, BR, MC, 4],
    [JW, MC, 10, BR, AJ, 5],
    [BR, J, 9, MC, MD, 10],
    [BR, J, 8, MC, MD, 10],
    [JW, E, 10, MC, MD, 1],
    [JW, E, 10, B, ASU, 4],
    [JW, E, 10, B, ASU, 5],
    [JW, E, 10, AJ, MC, 7],
    [ASU, E, 6, JH, MLE, 7],
    [AJ, JH, 9, MC, GH, 10],
    [E, JW, 10, M, JI, 6],
    [E, JW, 7, M, JI, 10],
    [AJ, ASU, 10, M, E, 2],
    [G, AJ, 10, E, JW, 6],
    [E, JH, 10, G, AJ, 9],
    [E, JW, 10, W, AJ, 5],
    [GH, MC, 10, B, JW, 8],
    [WD, MC, 10, EC, JW, 5],
    [E, ML, 10, MC, AJ, 7],
    [B, G, 10, E, ML, 2],
    [B, G, 10, AJ, MC, 1],
    [B, J, 5, JH, MC, 10],
    [B, J, 6, JH, MC, 10],
    [MC, GH, 10, AJ, AH, 1],
    [E, AJ, 9, B, ANDREW, 1],
    [E, WD, 1, AJ, BR, 10],
    [E, AJ, 1, WD, BR, 10],
    [E, JW, 10, ASU, ML, 2],
    [GH, SLG, 10, MC, MLE, 7],
    [GH, MC, 10, JC, JH, 5],
    [GH, MC, 10, EC, JW, 8],
    [GH, AJ, 10, MC, JW, 8],



    [GH, MC, 6, B, JW, 10],
    [AJ, MC, 8, B, JW, 10],
    [GH, MC, 10, B, JW, 7],
    [B, JH, 5, J, MC, 10],
    [B, JH, 10, J, MC, 5],
    [B, JH, 6, GH, JW, 10],
    [B, MC, 8, GH, JW, 10],
    [B, MC, 3, GH, JW, 10],
    [J, AJ, 8, GH, JW, 10],
    [G, MC, 10, E, JW, 8],
    [G, MC, 10, E, JW, 9],
    [J, JH, 10, G, JW, 7],
    [AJ, JOSH, 1, G, JW, 10],
    [GH, MC, 10, WD, BD, 5],
    [GH, WD, 10, BD, MC, 8],
    [B, JH, 10, E, J, 4],
    [GH, MC, 10, B, EC, 5],
    [GH, MC, 10, BR, AJ, 6],
    [J, JH, 10, BR, JW, 7],
    [GH, AJ, 10, EC, JW, 5],
    [J, JC, 10, A, MC, 6],
    [J, JC, 10, A, MC, 9],
    [E, JW, 10, AJ, MC, 7],
    [MC, JC, 10, E, JW, 9],
    [MC, JC, 10, E, JW, 6],
    [J, B, 10, E, ASU, 1],
    [J, B, 10, JH, MC, 9],
    [J, B, 8, G, MC, 8],
    [J, ASU, 4, MC, E, 10],
    [J, MC, 10, E, ASU, 0],
    [B, JW, 10, MC, AJ, 7],
    [B, JW, 10, MC, AJ, 3],
    [B, JW, 10, MC, J, 5],
    [B, JW, 10, MC, J, 7],
    [E, JW, 10, B, AJ, 9],
    [JC, MC, 10, JW, J, 9],
    [JC, MC, 6, JW, B, 10],
    [E, JW, 10, B, ASU, 7],
    [MC, J, 10, B, MD, 1],
    [MC, J, 10, B, MD, 9],
    [MC, J, 10, JOSH, JW, 5],
    [E, AJ, 10, B, W, 9],
    [B, WD, 10, E, G, 2],
    [J, JW, 3, B, G, 10],
    [E, ASU, 1, B, G, 10],

    # 25
    # 19 Sep
    [EC, GH, 10, WD, AJ, 2],
    [GH, BR, 10, MC, JW, 7],
    [GH, MC, 10, EC, JW, 9],
    [MD, JB, 10, EC, JW, 6],
    [GH, DAM, 10, WD, AJ, 5],
    [E, JW, 10, J, AJ, 7],
    [E, JW, 10, J, MC, 9],
    [MC, J, 10, JW, E, 5],
    [MC, J, 9, JW, E, 10],
    [MC, J, 10, JW, E, 5],
    [GH, B, 10, E, JIN, 2],
    [GH, MC, 10, JOSH, BR, 7],
    [J, MC, 7, JOSH, BR, 10],
    [GH, BR, 10, NC, JH, 0],
    [GH, BR, 10, NC, JH, 1],
    [BR, JC, 10, E, GH, 9],
    [E, JW, 10, BR, J, 9],
    ### double check this one ###
    # [B, JW, 10, MC, GH, 6],
    ######################
    [B, JW, 10, MC, GH, 4],
    [B, JW, 10, MC, GH, 6],
    [GH, EC, 10, BR, JW, 2],
    [GH, EC, 8, BR, JW, 10],
    [EC, JW, 10, BR, ASU, 3],
    [EC, JW, 10, MC, MU, 5],
    [B, MC, 10, JH, J, 7],
    [B, MD, 10, GH, MC, 6],
    [AJ, B, 7, JW, E, 10],
    [AJ, B, 9, JW, E, 10],
    [AJ, B, 9, JW, E, 10],
    [AJ, B, 8, JW, E, 10],
    [MU, B, 2, JW, E, 10],
    [MU, B, 10, JW, E, 8],
    [MU, B, 7, JW, E, 10],
    [MC, B, 10, GH, AJ, 8],
    [GH, B, 10, AJ, MC, 3],
    [GH, JC, 10, B, MC, 3],
    [JOSH, SLG, 10, B, AH, 9],
    [J, MD, 7, B, AJ, 10],
    ### Maya ?? ###
    # [MA, MC, 10, B, AJ, 7],
    [JW, E, 10, MU, B, 8],
    [B, MC, 10, E, JW, 8],
    [B, J, 10, E, JW, 9],
    [B, GH, 9, E, JW, 10],
    [B, GH, 10, E, JW, 3],

    # 26
    [JW, E, 10, B, MU, 4],
    [J, VS, 4, JW, E, 10],
    [MD, MU, 4, JW, E, 10],
    [GH, AJ, 10, JW, E, 8],
    [B, J, 10, G, MU, 5],
    [B, J, 10, G, MU, 9],
    [B, J, 6, G, MC, 10],
    [E, JW, 9, G, MC, 10],
    [E, JW, 6, G, BR, 10],
    [E, JW, 10, B, J, 6],
    [E, JW, 9, B, J, 10],
    [B, J, 10, E, MU, 2],
    [B, MU, 10, J, Aaron, 8],
    [B, MU, 10, AJ, WD, 3],
    [B, MU, 10, E, AJ, 4],

    [B, MU, 10, E, MC, 4],
    [B, MU, 4, AJ, MC, 10],
    [B, MU, 10, AJ, MC, 4],
    [E, JW, 10, B, MU, 1],
    [E, MD, 10, B, MC, 7],
    [B, J, 10, MC, G, 9],
    [E, JW, 9, MC, G, 10],
    [E, JW, 10, G, MU, 5],
    [BR, MC, 10, JW, EC, 8],
    [GH, JC, 10, BR, AJ, 4],
    [GH, MU, 3, BR, AJ, 10],
    [GH, MU, 8, BR, AJ, 10],
    [JW, J, 10, BR, MU, 5],
    [JW, E, 8, B, J, 10],

    [BR, MD, 9, JW, MC, 10],
    [BR, MD, 8, JW, MC, 10],
    [JW, BR, 10, MC, MD, 3],
    [JW, BR, 10, MC, MD, 4],
    [MU, BR, 10, E, J, 3],
    [GH, MD, 10, J,  AJ, 4],
    [MU, BR, 10, E, MC, 9],
    [J, E, 10, B, MU, 8],
    [J, E, 6, B, MU, 10],
    [J, E, 5, B, MU, 10],
    [B, MU, 6, E, JW, 10],
    [B, MU, 10, E, JW, 4],
    [B, MU, 10, E, JW, 5],
    [G, JW, 10, B, MD, 4],
    [B, MU, 10, E, MC, 9],
    [MC, GH, 10, BR, E, 6],
    [MC, GH, 10, BR, E, 8],
    [MC, GH, 10, BR, E, 7],

    # 27
    [E, JW, 10, B, MU, 8],
    [E, JW, 10, B, MU, 8],
    [E, JW, 10, B, MU, 8],
    [B, MU, 10,  EC, MD, 4],
    [B, MU, 10,  EC, MC, 9],
    [B, MU, 10,  J, JW, 5],
    [E, JW, 10, ED, JOSH, 1],
    [B, MU, 10, E, AJ, 4],
    [B, AJ, 6, E, MU, 10],
    [B, AJ, 10, E, MU, 6],
    [JC, MD, 10, B, MU, 6],
    [JW, MD, 10, B, MU, 8],
    [G, MC, 8, E, JW, 10],
    [B, JC, 10, E, JW, 7],
    [B, JC, 10, E, JW, 8],
    [B, N, 10, E, TIM, 3],
    [B, N, 10, E, TIM, 4],

    # 28
    [B, JW, 10, E, AJ, 4],
    [B, MC, 2, E, JW, 10],
    [B, N, 6, JC, JW, 10],
    [E, G, 10, B, A, 6],
    [E, G, 10, B, A, 4],
    [BR, MC, 10, JW, JC, 7],
    [BR, MC, 10, MU, MD, 6],
    [BR, MC, 10, JW, MU, 9],
    [BR, MU, 7, MC, JW, 10],
    [EC, JH, 10, B, MU, 5],
    [EC, JH, 10, B, MU, 6],
    [EC, MC, 10, B, MU, 8],
    [EC, MC, 2, B, MU, 10],
    [EC, MC, 6, B, MU, 10],
    [E, JW, 6, B, MC, 10],
    [E, JW, 7, B, MC, 10],
    [GH, JC, 7, B, MC, 10],
    [GH, JC, 8, B, MC, 10],
    [E, JW, 10, B, AJ, 8],
    [BR, MC, 10, JW, JC, 8],
    [BR, MC, 10, G, SLG, 7],
    [BR, MC, 10, JC, N, 9],
    [BR, MC, 9, E, JW, 9],


    #29
    [B, MU, 2, JW, JC, 10],
    [MC, JW, 10, BR, MU, 6],
    [JH, JW, 10, BR, MU, 5],
    [JW, MD, 6, BR, MU, 8],
    [MC, AJ, 10, BR, MU, 8],
    [MC, AJ, 10, BR, MU, 9],
    # [JW, JOSH, , BR, MU, 10],
    [JW, AL, 6, BR, NC, 10],
    [JW, AL, 6, BR, NC, 10],
    [JW, AL, 9, BR, NC, 10],
    [GH, MC, 6, MU, JW, 10],
    [MC, JW, 10, AJ, MU, 2],
    [MC, AJ, 6, MU, JW, 10],
    [MC, MD, 7, JW, JC, 10],
    [MC, MD, 7, JW, JC, 10],

    [GH, JH, 10, JW, MU, 5],
    [GH, JH, 10, JW, MU, 4],
    [B, MU, 10, AJAY, J, 5],
    [B, MU, 10, AJAY, J, 2],
    [B, MU, 10, E, MC, 7],
    [B, MU, 7, E, MC, 10],
    [B, MU, 10, E, MC, 7],
    [GH, MU, 10, E, MC, 9],
    [B, MU, 10, JC, JW, 9],
    [B, MU, 7, JC, JW, 10],
    [B, MU, 2, JC, JW, 10],
    [B, JC, 10, MC, JOSH, 4],
    [B, MU, 7, JW, MC, 10],
    [B, MU, 6, JW, MD, 10],
    [B, MU, 6, JW, MD, 10],

    [GH, JH, 10, MC, BR, 8],
    [GH, EC, 10, BR, MD, 3],
    [GH, EC, 10, MC, MU, 7],
    [GH, EC, 10, BR, JC, 8],
    [GH, MU, 10, MC, JH, 1],
    [EC, JW, 10, B, MU, 8],
    [EC, JW, 10, B, MU, 4],
    [GH, JC, 10, B, JH, 6],
    [MC, MU, 10, EC, JW, 9],
    [EC, JW, 10, J, GH, 6],
    [EC, JW, 6, MU, GH, 10],
    [JW, MC, 9, MU, GH, 10],
    [JH, JC, 10, MC, MD, 7],
    [JH, JC, 3, BR, GH, 10],
    [E, JW, 10, BR, GH, 6],
    [E, JW, 7, BR, MU, 10],

    [JC, BR, 10, MD, MU, 5],
    [JC, BR, 10, MC, MU, 4],
    [E, B, 10, MI, MC, 4],

    # 30
    [E, JW, 10, B, MC, 2],
    [J, B, 10, E, AJ, 4],
    [JW, JC, 10, B, NC, 6],
    [E, G, 10, B, A, 6],
    [E, G, 10, B, A, 4],
    [BR, MC, 10, JW, JC, 7],
    [BR, MC, 10, MA, MD, 6],
    [BR, MC, 10, JW, MA, 9],
    [MC, JW, 10, BR, MA, 7],
    [EC, JH, 10, BR, MA, 5],
    [EC, JH, 10, BR, MA, 6],
    [E, MC, 10, MU, B, 8],
    [E, MC, 2, MU, B, 10],
    [E, MC, 6, MU, B, 10],

    [GH, JC, 7, BR, MC, 10],
    [GH, JC, 8, BR, MC, 10],
    [E, JW, 10, B, AJ, 8],
    [BR, MC, 10, JW, JC, 8],
    [B, MC, 10, G, SLG, 7],
    [B, MC, 10, JC, N, 9],
    [B, MC, 9, E, JW, 10],
    [NC, JC, 6, E, JW, 10],
    [NC, JC, 9, E, JW, 10],
    [MC, MD, 10, EC, JW, 9],
    [MC, JW, 10, BR, MU, 4],
    [JW, E, 10, BR, MU, 7],
    [JW, JC, 10, BR, MC, 8],
    [MU, MC, 10, BR, EC, 5],

    [BR, MC, 3, GH, EC, 10],
    [BR, MC, 6, GH, EC, 10],
    [BR, MU, 8, JW, E, 10],
    [BR, MU, 7, JW, E, 10],
    [BR, MU, 10, MC, AJ, 9],
    [BR, MU, 2, MC, JH, 10],
    [BR, MU, 9, MC, JH, 10],
    [BR, MU, 9, JW, MD, 10],
    [MC, JW, 10, JC, AJ, 5],
    [MC, JW, 10, ED, GH, 8],
    [MC, MD, 10, BR, MA, 9],
    [MC, JH, 10, BR, MA, 4],
    [MC, JH, 10, BR, MA, 6],
    [B, MU, 10, N, SLG, 9],
    [B, MU, 10, JW, AJAY, 4],

    [E, JW, 6, BR, MC, 10],
    [E, JW, 7, BR, MC, 10],
    [JC, MC, 5, GH, EC, 10],

    # 31
    [E, MC, 10, MU, AJ, 7],
    [E, MC, 8, MU, AJ, 10],
    [E, MC, 10, MU, AJ, 8],
    [MD, JW, 10, BR, JC, 9],
    [MD, JW, 10, BR, JC, 9],
    [E, JW, 10, MU, JC, 2],
    [E, JW, 10, MU, G, 7],
    [JC, MC, 5, MU, J, 10],
    [EC, JW, 6, MU, J, 10],
    [MC, JW, 10, MU, J, 8],
    [MC, JW, 10, MU, J, 7],
    [JW, E, 10, J, MU, 7],
    [JW, E, 7, J, MU, 10],
    [B, JC, 10, MC, MD, 6],
    [B, JC, 10, MC, MD, 6],
    [B, JC, 10, MC, MD, 9],

    [B, AJ, 8, JW, MU, 10],
    [B, MU, 10, E, J, 5],
    [B, MU, 10, MC, MD, 4],
    [MC, MU, 10, B, EC, 1],
    [MC, MU, 7, B, EC, 10],
    [MC, MU, 10, B, JH, 9],
    [MC, MU, 1, MD, J, 10],
    [GH, B, 10, MD, J, 9],
    [GH, B, 10, MC, MU, 5],
    [MU, B, 6, JW, E, 10],
    [MD, B, 6, JW, MC, 10],
    [MD, B, 7, JW, MC, 10],
    [B, MC, 5, JW, MD, 10],
    [B, MU, 10, MC, EC, 5],
    [B, MU, 10, MC, JW, 10],

    [MU, EC, 10, MC, ALEX, 4],
    [MU, EC, 4, MC, ALEX, 10],
    [MU, EC, 10, MC, ALEX, 5],
    [B, MU, 10, EC, JW, 7],
    [B, MU, 10, MC, MD, 8],
    [B, MU, 10, MC, MD, 8],
    [B, MU, 5, JW, E, 10],
    [MD, J, 8, JW, JH, 10],
    [MC, MU, 10, JW, GR, 9],
    [B, AJ, 10, MU, MC, 6],
    [JC, JW, 10, BR, MC, 9],
    [JC, JW, 10, BR, MC, 9],
    [JW, E, 10, JC, GREG, 6],
    [JC, MD, 5, GH, MC, 10],
    [JC, MD, 10, GH, MC, 9],

    [GH, JC, 10, BR, MU, 9],
    [JC, MC, 10, BR, MU, 9],
    [B, MU, 10, MC, EC, 7],
    [B, MU, 10, MC, GH, 8],
    [B, MU, 10, G, JOSH, 8],
    [B, MU, 10, JW, MD, 6],

    #32
    [WD, GH, 8, AJ, JW, 10],
    [B, MU, 10, E, MD, 1],
    # AB ?
    # [MD, MU, 10, AJ, AB, 9],
    [MD, MU, 10, BR, MC, 7],
    [E, JON, 3, MD, MU, 10],
    [B, G, 10, MD, MU, 6],
    [B, G, 10, AJ, EC, 3],
    [JON, MU, 10, EC, AJAY, 5],
    [E, JW, 10, B, MU, 7],
    [E, MC, 5, B, MU, 10],
    [E, AJ, 2, B, MU, 10],
    [MC, GH, 2, EC, MU, 0],
    [MD, JW, 10, B, MU, 2],
    [MD, JW, 9, B, MU, 10],
    [E, G, 9, B, MU, 10],

    [B, JW, 10, JC, MC, 9],
    [JW, MU, 10, JC, AJ, 3],
    [JW, E, 10, JC, MU, 9],
    [B, MU, 10, MD, JC, 2],
    [B, MU, 6, JW, J, 10],
    [GH, MD, 10, JW, EC, 5],
    [B, MU, 10, JW, EC, 4],
    [B, MU, 10, JW, EC, 6],
    [MU, GH, 10, JW, EC, 5],
    [GH, BR, 10, JW, J, 7],
    [GH, BR, 10, JC, MD, 3],
    [GH, BR, 10, MD, MU, 3],
    [GH, MC, 10, JC, SLG, 7],
    [MC, MD, 10, BR, MU, 6],

    [MC, MD, 6, BR, MU, 10],
    [EC, MD, 6, BR, MU, 10],
    [MC, N, 3, BR, MU, 10],
    [JC, NC, 10, AJ, CW, 0],
    [JC, NC, 2, GH, MU, 10],
    [B, MC, 10, GH, MU, 8],
    [B, MC, 10, GH, MU, 4],
    [B, MC, 10, AJ, E, 8],
    [B, MU, 10, JW, MC, 9],
    [B, MU, 10, JC, N, 6],
    [B, MU, 10, N, MC, 4],
    [B, MU, 10, MC, MD, 5],
    [E, JW, 10, AA, GH, 6],
    [E, JW, 10, B, JI, 9],
    [E, JW, 10, MC, MU, 6],

    [BR, GH, 10, MU, MC, 4],
    [BR, GH, 10, EC, MC, 4],
    [BR, MU, 10, E, JW, 5],
    [BR, MU, 10, AJ, MD, 5],
    [B, MU, 10, MC, JC, 9],
    # [GH, ??, 10, BR, MU, 6],


    # 33
    [B, MU, 10, E, JW, 7],
    [GH, MU, 10, JW, EC, 2],
    [GH, MU, 10, JW, JC, 9],
    [B, MU, 10, MD, MC, 6],
    [B, JC, 6, MD, MC, 10],
    [B, JC, 10, MD, MC, 4],
    [J, JH, 10, JW, MD, 4],
    [J, JW, 6, B, MU, 10],
    [B, MU, 10, JW, JH, 6],
    [JC, GH, 10, EC, JW, 7],
    # [JC, GH, 10, AJ, ?, 0],
    [E, JI, 10, JC, NC, 3],
    [JC, MU, 10, EC, OV, 3],

    [GH, OV, 10, BR, EC, 9],
    [B, GH, 10, JW, E, 9],
    [B, GH, 10, MC, MD, 4],
    [SLG, JC, 6, JW, MD, 10],
    [EC, MU, 10, JW, JC, 9],
    [MC, CW, 0, JW, JC, 10],
    [B, N, 9, J, E, 10],
    [B, MD, 10, Omid, MU, 7],
    [B, Omid, 10, MD, MU, 9],
    [B, MU, 10, MD, ARM, 1],
    [B, MU, 10, JC, MC, 4],
    [B, MU, 10, JW, MD, 5],
    [B, MU, 10, JW, MD, 6],
    [GH, NC, 10, JC, MU, 9],
    [GH, NC, 9, JC, MU, 10],

    [MU, JC, 10, B, EC, 7],
    [B, MU, 10, JW, MC, 8],
    [B, MU, 10, MD, MC, 3],
    [B, MU, 10, MD, MC, 6],
    [B, MC, 10, MD, JW, 9],
    [E, JW, 10, MU, MC, 6],
    [BR, MU, 10, OV, JH, 4],
    [BR, MU, 10, OV, JH, 6],
    [GH, JING, 9, JW, JC, 10],
    [AJ, MU, 4, JW, JC, 10],
    [BR, MD, 6, JW, JC, 10],
    [BR, MD, 10, MD, JING, 6],
    [BR, MD, 6, MD, JING, 10],
    [EC, MU, 10, JW, JC, 3],
    [EC, MU, 4, JW, JC, 10],

    #34
    [JC, JW, 6, MU, EC, 10],
    [B, MU, 10, MD, MC, 9],
    [B, MU, 9, MD, MC, 10],
    [GH, JC, 10, BR, MC, 6],
    [JC, MU, 10, JW, GH, 9],
    [BR, AJ, 4, JW, GH, 10],
    [B, MU, 8, JH, E, 10],
    [B, MU, 10, JH, E, 5],
    [B, MU, 10, E, MC, 2],
    [MU, MC, 5, B, G, 10],
    [MU, MC, 5, B, E, 10],
    [JC, MD, 9, B, MC, 10],
    [JC, MD, 10, B, MC, 9],
    [JC, MD, 10, B, MC, 9],

    [GH, CW, 10, NC, JH, 4],
    [GH, CW, 10, NC, JH, 5],
    [B, EC, 4, MU, MC, 10],
    [B, EC, 10, MU, MC, 7],
    [BR, MU, 3, JC, MC, 10],
    [BR, AJ, 10, EC, MU, 7],
    [MU, JC, 10, BR, AJ, 8],
    [MU, EC, 10, JC, OV, 4],
    [MU, EC, 10, BR, OV, 7],
    [MU, EC, 10, BR, OV, 5],
    [MU, EC, 1, MC, JC, 10],
    [MU, JC, 10, AJ, MD, 5],
    [MC, JC, 8, JW, SLG, 10],

    [B, MU, 10, MD, JW, 9],
    [B, MU, 10, JC, JH, 3],
    [B, MU, 10, MD, JW, 6],
    [B, AJAY, 10, E, AJ, 9],
    [JC, JH, 10, MC, MA, 2],
    [JC, JH, 10, MC, MA, 4],
    [B, MU, 10, MD, MC, 3],
    [B, MU, 10, MD, MC, 5],
    [B, MU, 10, N, JC, 5],
    [B, MU, 10, N, JC, 3],
    [B, MU, 10, JC, SLG, 8],
]

singles = [
    [Elliot, 6, Brendan, 10],

    [JA, 10, E, 3],
    [J, 10, E, 6],
    [G, 10, J, 5],

    [GREG, 10, ELLIOT, 6],

    [B, 10, E, 1],
]
