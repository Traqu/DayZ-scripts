P ='Script execution time:'#line:1
G =range #line:2
A =print #line:3
import time as B ,keyboard as K ,datetime as S ,threading as T #line:4
Q =6.33 #line:5
U =1.55 #line:6
J =5 #line:7
H =.6 #line:8
V =.1 #line:9
I =.0825 #line:10
E ='f'#line:11
L =None #line:12
def D ():return S .datetime .now ().time ().strftime ('%H:%M:%S')#line:13
def M (O00O0OOO0OO0O0000 ):O000O000O0O000000 ='{:.2f}'.format (O00O0OOO0OO0O0000 );return O000O000O0O000000 #line:14
def F (O0OO0O00O0O0O0O00 ,O0O0OOOO00OOOOO00 ):#line:15
	if C .is_set ():return #line:16
	K .press (O0OO0O00O0O0O0O00 );B .sleep (O0O0OOOO00OOOOO00 );K .release (O0OO0O00O0O0O0O00 );B .sleep (V )#line:17
def R ():#line:18
	if C .is_set ():return #line:19
	A (D ()+'  From thousands to ones');B .sleep (H )#line:20
	for OOOOO000O0OOO0000 in G (3 ):F (E ,I )#line:21
def W ():#line:22
	if C .is_set ():return #line:23
	A (D ()+'  From hundreeds to ones');B .sleep (H )#line:24
	for OO0000OO00O000OOO in G (2 ):F (E ,I )#line:25
def m ():#line:26
	if C .is_set ():return #line:27
	A (D ()+'  From hundreeds to tens');B .sleep (H );F (E ,I )#line:28
def X ():#line:29
	if C .is_set ():return #line:30
	A (D ()+'  From tens to ones');B .sleep (H );F (E ,I )#line:31
def Y ():#line:32
	if C .is_set ():return #line:33
	A (D ()+'  From ones to tens');B .sleep (H )#line:34
	for OO0000O0000O00OOO in G (3 ):F (E ,I )#line:35
def Z ():#line:36
	if C .is_set ():return #line:37
	A (D ()+'  From ones to hundreeds');B .sleep (H )#line:38
	for O0OO0OO00000OOOOO in G (2 ):F (E ,I )#line:39
def a ():#line:40
	if C .is_set ():return #line:41
	A (D ()+'  From ones to thousands');B .sleep (H );F (E ,I )#line:42
def N ():#line:43
	if C .is_set ():return #line:44
	A (D ()+'  Increment');F (E ,U )#line:45
def b ():R ()#line:46
def c (O00OOO000OO0O00O0 ,O00OO00O0O0OOOOO0 ):#line:47
	if C .is_set ():return #line:48
	A (D ()+'  Checking ones');F (E ,Q )#line:49
def d ():#line:50
	for O000O0OO0OO0O0000 in G (10 ):c (E ,Q );Y ();N ();X ()#line:51
def e ():#line:52
	for OO0OOO0O0O0000OOO in G (10 ):Z ();N ();W ();d ()#line:53
def f ():#line:54
	if C .is_set ():return #line:55
	for O0OO000O00OOO0OOO in G (10 ):#line:56
		if C .is_set ():return #line:57
		a ();N ();R ();e ()#line:58
C =T .Event ()#line:59
def g ():C .set ()#line:60
def h (O00000OO00O0OO00O ):#line:61
	O000O0O00O00OOO0O =O00000OO00O0OO00O ;global L #line:62
	if O000O0O00O00OOO0O .name =='a'or O000O0O00O00OOO0O .name =='w'or O000O0O00O00OOO0O .name =='s'or O000O0O00O00OOO0O .name =='d'or O000O0O00O00OOO0O .name =='esc'or O000O0O00O00OOO0O .name =='space'or O000O0O00O00OOO0O .name =='shift':L =O000O0O00O00OOO0O .name ;g ()#line:63
K .on_press (h )#line:64
def i ():#line:65
	b ();f ()#line:66
	if C .is_set ():A ('\nScript has been cancelled due to - '+L .upper ()+' - pressing\n');return #line:67
B .sleep (.6 )#line:68
A ('\nKeys that will terminate the script: ESC, SPACE, SHIFT, A, W, D, S')#line:69
B .sleep (1.4 )#line:70
A ('\n\nAwaiting to focus at DayZ...\nDo not perform any moves in game')#line:71
B .sleep (1. )#line:72
A ('\nStarting in: ')#line:73
B .sleep (1 )#line:74
for n in G (0 ,J ):A (str (J )+'...');J =J -1 ;B .sleep (1 )#line:75
B .sleep (.5 )#line:76
A ('\n'+D ()+' EXECUTION START TIME - it might take up to 3 hours to fulfill\n\n\nCRACKING LOGS:\n')#line:77
j =B .time ()#line:78
i ()#line:79
k =B .time ()#line:80
A (D ()+'  Lock opening finished.\n')#line:81
O =k -j #line:82
l =M (O )#line:83
A (P ,l ,'sedonds')#line:84
A (P ,M (O /60 ),'minutes (decimal)')#line:85
A (P ,M (O /60 /60 ),'hours (decimal)')