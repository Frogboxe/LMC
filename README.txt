
LMC notes:

The LMC I've written is a little different from other LMC implementations. It works by the same fundemental priciples,
but code in any other LMC will not work in this one.

Following is a list of all the commands currently implemented. N represents a memory address and T represents a tag number:

SET x; Sets the accumulator to value x. 
STA N; Sets N's value to the accumulator
LDA N; Sets the accumulator to N's value
BRA T; Branch to tag T.
BRP T; Branch to tag T when the accumulator is zero or greater than zero
BRZ T; Branch to tag T when the accumulator equals zero
ADD N; Adds N's value to the accumulator
SUB N; Takes N's value from the accumulator
INP  ; Sets accumulator to user input
OUT  ; Outputs the accumulator value
HLT  ; Stops execution.
Line tags are declared with T; like, for example, tag 0 is declared 0;. Simple. Now when you do BRA 0; the next line the LMC will
execute is the line immediately after the declaration of the tag ("0;")

N is an integer between 0 and ADDRESS_MAX. I have not restricted use of negative addresses. So you CAN use -1 as an address... not 
that you should, but you can. T is an integer. Tags CANNOT be strings. They are numbers. This will be imporved later on to allow 
more readable tags. Also, tags will be extended to work with memory addresses too.

The LMC completely ignores all forms of white-space. Spaces and NewLines are removed pre-compilation.

Here is a demonstration of tags:

INP;
OUT;
BRA 0;
OUT;
0;
HLT;

This will output the input ONCE. This is because once the LMC reaches BRA 0; it jumps to 0;, skipping the second instance
of the keyword "OUT" thereby only outputting the input once.

Here is a demonstration of multiplication in this LMC:

SET 1;
STA 81;

INP;
STA 1;
STA 3;
INP;
STA 2;
SUB 81;
STA 4;

0;
LDA 4;
BRZ 1;
LDA 1;
ADD 3;
STA 1;
LDA 4;
SUB 81;
STA 4;
BRA 0;


1;
LDA 1;
OUT;
HLT;

Feel free to send in extra code and/or fixes or what-have-you.

