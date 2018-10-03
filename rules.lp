
#show beat/6.

{beat(S,A,M,O,L,T) : agent(A) , beatt(S,A,M,O,L,T) , object(O),location(L)} =  1 :- T = 1..beatsnumber.
{at(A,L,T) : loc(A,L,T)} = 1 :- T = 1..beatsnumber.

agent(A) :- agent(A,_).
object(O):- agent(O,_).
location(L):- at(_,L,_).



%Supsense hill must climb before peak and fall after peak.
beatt(F,A,M,O,L,T) :- move(M,ST,A,O,L,T),F=S+ST,beat(S,_,_,_,_,T-1), S<=S+ST,1 <= T, T <= peak.
beatt(F,A,M,O,L,T):- move(M,ST,A,O,L,T),F=S+ST,beat(S,_,_,_,_,T-1), S>=S+ST, peak < T, T<= beatsnumber.

at(A,L,T) :- loc(A,L,T).



%move lists
move(follow,S,A,O,L,T),loc(A,L,T),loc(O,L,T):- agent(A,_), agent(O,_), A!=O, S=0, at(O,L,T-1). 
move(shoot,S,A,O,L,T),loc(A,L,T),loc(O,L,T) :- agent(A,hero), agent(O,villain),S=-10,at(A,L,T-1),at(O,L,T-1).
move(shoot,S,A,O,L,T),loc(A,L,T),loc(O,L,T)  :- agent(A,villain), agent(O,hero),S=10,at(A,L,T-1), at(O,L,T-1).

%Constraints
%End must contain no suspense
:- beat(S,A,M,O,L,beatsnumber), beatt(S,A,M,O,L,beatsnumber), S!=0.
%Peak must have suspense.
:- beat(S,A,M,O,L,peak), beatt(S,A,M,O,L,peak), S=0.
