# p1 and p2: compute de max/min of 3 numbers;
# verify if a number is prime, compute gcd of 2 numbers,
# compute the solutions for a 2nd order equation, aso
#
# p3: compute the sum of n numbers, computer the max/min of n numbers

#P1: starts here
##Compute max/min
HereWeGoAgain

int vara
int varc
int varb
StayHere ( vara ) #(read)
varb = 5
StayHere ( varc ) #(read)
if ( vara >= varb )
    varb = vara
if( varb >= varc )
   varc = varb
ShowMe ( "Max is:", varc )

StayHere ( vara )
varb = 123
StayHere ( varc )
if ( varb <= varc )
    varc = varb
if ( varc <= vara )
    vara = varc
ShowMe ( "Min is:", vara )

PainEndsHere 0


#P2:
##Verify if a number is prime

HereWeGoAgain
int varFirstNum
int vari
StayHere ( varFirstNum )
for ( vari = 2 ; vari <= varFirstNum / 2 ; vari = vari + 1 )
    if ( varFirstNum % vari == 0 )
        ShowMe ( "The number enter is not prime!" )
        PainEndsHere 0
ShowMe ( "The number entered is prime!" )
PainEndsHere 0

#P3: sum of 50 numbers
HereWeGoAgain

array [ 100 ] of int varVector
int vari
int varSuma = 0
for ( vari = 0 ; vari < 50 ; vari = vari + 1 )
    StayHere ( varVector [ vari ] )
for ( vari = 0 ; vari < 50 ; vari = vari + 1 )
    varSuma = varSuma + varVector [ vari ]
ShowMe ( "THE SUM IS:" , varSuma )

PainEndsHere 0


#P.ERROR:
HereWeGoAgain

int varb
StayHere ( vara )  # vara is not declared
varb = varb + vara
varb = varb * 5
ShowMe ( varb )
ShowMe ( varb // vara ) # // operator is not defined
PainEndsHere 0

