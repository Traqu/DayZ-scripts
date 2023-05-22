P='Script execution time:'
G=range
A=print
import time as B,keyboard as K,datetime as S,threading as T
Q=6.33
U=1.55
J=5
H=.6
V=.1
I=.0825
E='f'
L=None
def D():return S.datetime.now().time().strftime('%H:%M:%S')
def M(execution_time):A='{:.2f}'.format(execution_time);return A
def F(key,hold_time):
	if C.is_set():return
	K.press(key);B.sleep(hold_time);K.release(key);B.sleep(V)
def R():
	if C.is_set():return
	A(D()+'  From thousands to ones');B.sleep(H)
	for J in G(3):F(E,I)
def W():
	if C.is_set():return
	A(D()+'  From hundreeds to ones');B.sleep(H)
	for J in G(2):F(E,I)
def m():
	if C.is_set():return
	A(D()+'  From hundreeds to tens');B.sleep(H);F(E,I)
def X():
	if C.is_set():return
	A(D()+'  From tens to ones');B.sleep(H);F(E,I)
def Y():
	if C.is_set():return
	A(D()+'  From ones to tens');B.sleep(H)
	for J in G(3):F(E,I)
def Z():
	if C.is_set():return
	A(D()+'  From ones to hundreeds');B.sleep(H)
	for J in G(2):F(E,I)
def a():
	if C.is_set():return
	A(D()+'  From ones to thousands');B.sleep(H);F(E,I)
def N():
	if C.is_set():return
	A(D()+'  Increment');F(E,U)
def b():R()
def c(key,hold_time):
	if C.is_set():return
	A(D()+'  Checking ones');F(E,Q)
def d():
	for A in G(10):c(E,Q);Y();N();X()
def e():
	for A in G(10):Z();N();W();d()
def f():
	if C.is_set():return
	for A in G(10):
		if C.is_set():return
		a();N();R();e()
C=T.Event()
def g():C.set()
def h(event):
	A=event;global L
	if A.name=='a'or A.name=='w'or A.name=='s'or A.name=='d'or A.name=='esc'or A.name=='space'or A.name=='shift':L=A.name;g()
K.on_press(h)
def i():
	b();f()
	if C.is_set():A('\nScript has been cancelled due to - '+L.upper()+' - pressing\n');return
B.sleep(.6)
A('\nKeys that will terminate the script: ESC, SPACE, SHIFT, A, W, D, S')
B.sleep(1.4)
A('\n\nAwaiting to focus at DayZ...\nDo not perform any moves in game')
B.sleep(1.)
A('\nStarting in: ')
B.sleep(1)
for n in G(0,J):A(str(J)+'...');J=J-1;B.sleep(1)
B.sleep(.5)
A('\n'+D()+' EXECUTION START TIME - it might take up to 3 hours to fulfill\n\n\nCRACKING LOGS:\n')
j=B.time()
i()
k=B.time()
A(D()+'  Lock opening finished.\n')
O=k-j
l=M(O)
A(P,l,'sedonds')
A(P,M(O/60),'minutes (decimal)')
A(P,M(O/60/60),'hours (decimal)')