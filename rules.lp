
#show beat/5.

{beat(S,A,M,O,T) : agent(A) , move(M,ST,A,O) , object(O)} = 1 :- beatt(S,A,M,O,T),T = 1..beatsnumber.

agent(A) :- agent(A,_).
object(O):- agent(O,_).


beatt(F,A,M,O,T) :- move(M,ST,A,O),F=S+ST,beat(S,_,_,_,T-1), S<S+ST,1 <= T, T <= peak.

beatt(F,A,M,O,T) :- move(M,ST,A,O),F=S+ST,beat(S,_,_,_,T-1), S>S+ST, peak < T, T<= beatsnumber.

move(follow,S,A,O) :- agent(A,_), agent(O,_), A!=O, S=10. 

move(shoot,S,A,O) :- agent(A,hero), agent(O,villain),S=-10.
move(shoot,S,A,O) :- agent(A,villain), agent(O,hero),S=10.

