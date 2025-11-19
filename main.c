                                                #
i
n
c
l
u
d
e
 
<
s
t
d
i
o
.
h
>


#
i
n
c
l
u
d
e
 
<
s
t
d
l
i
b
.
h
>


#
i
n
c
l
u
d
e
 
<
s
y
s
l
o
g
.
h
>




#
d
e
f
i
n
e
 
M
A
X
_
M
E
S
S
A
G
E
_
L
E
N
G
T
H
 
5
0




t
y
p
e
d
e
f
 
s
t
r
u
c
t
 
{


 
 
 
 
c
h
a
r
 
m
e
s
s
a
g
e
[
M
A
X
_
M
E
S
S
A
G
E
_
L
E
N
G
T
H
]
;


}
 
H
e
l
l
o
W
o
r
l
d
C
o
n
t
r
o
l
l
e
r
;




v
o
i
d
 
i
n
i
t
i
a
l
i
z
e
_
l
o
g
g
i
n
g
(
)
 
{


 
 
 
 
o
p
e
n
l
o
g
(
"
H
e
l
l
o
W
o
r
l
d
A
p
p
"
,
 
L
O
G
_
P
I
D
,
 
L
O
G
_
U
S
E
R
)
;


}




v
o
i
d
 
c
l
e
a
n
u
p
_
l
o
g
g
i
n
g
(
)
 
{


 
 
 
 
c
l
o
s
e
l
o
g
(
)
;


}




i
n
t
 
e
x
e
c
u
t
e
_
h
e
l
l
o
_
w
o
r
l
d
(
H
e
l
l
o
W
o
r
l
d
C
o
n
t
r
o
l
l
e
r
*
 
c
o
n
t
r
o
l
l
e
r
)
 
{


 
 
 
 
i
f
 
(
c
o
n
t
r
o
l
l
e
r
 
=
=
 
N
U
L
L
)
 
{


 
 
 
 
 
 
 
 
s
y
s
l
o
g
(
L
O
G
_
E
R
R
,
 
"
N
u
l
l
 
c
o
n
t
r
o
l
l
e
r
 
p
a
s
s
e
d
 
t
o
 
e
x
e
c
u
t
i
o
n
 
f
u
n
c
t
i
o
n
"
)
;


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
E
X
I
T
_
F
A
I
L
U
R
E
;


 
 
 
 
}




 
 
 
 
s
n
p
r
i
n
t
f
(
c
o
n
t
r
o
l
l
e
r
-
>
m
e
s
s
a
g
e
,
 
s
i
z
e
o
f
(
c
o
n
t
r
o
l
l
e
r
-
>
m
e
s
s
a
g
e
)
,
 
"
H
e
l
l
o
 
W
o
r
l
d
!
"
)
;




 
 
 
 
r
e
t
u
r
n
 
E
X
I
T
_
S
U
C
C
E
S
S
;


}




v
o
i
d
 
d
i
s
p
l
a
y
_
m
e
s
s
a
g
e
(
c
o
n
s
t
 
H
e
l
l
o
W
o
r
l
d
C
o
n
t
r
o
l
l
e
r
*
 
c
o
n
t
r
o
l
l
e
r
)
 
{


 
 
 
 
i
f
 
(
c
o
n
t
r
o
l
l
e
r
 
=
=
 
N
U
L
L
)
 
{


 
 
 
 
 
 
 
 
s
y
s
l
o
g
(
L
O
G
_
E
R
R
,
 
"
N
u
l
l
 
c
o
n
t
r
o
l
l
e
r
 
p
a
s
s
e
d
 
t
o
 
d
i
s
p
l
a
y
 
f
u
n
c
t
i
o
n
"
)
;


 
 
 
 
 
 
 
 
r
e
t
u
r
n
;


 
 
 
 
}




 
 
 
 
p
r
i
n
t
f
(
"
%
s
\
n
"
,
 
c
o
n
t
r
o
l
l
e
r
-
>
m
e
s
s
a
g
e
)
;


}




i
n
t
 
m
a
i
n
(
)
 
{


 
 
 
 
i
n
i
t
i
a
l
i
z
e
_
l
o
g
g
i
n
g
(
)
;




 
 
 
 
H
e
l
l
o
W
o
r
l
d
C
o
n
t
r
o
l
l
e
r
 
c
o
n
t
r
o
l
l
e
r
;


 
 
 
 


 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
e
x
e
c
u
t
e
_
h
e
l
l
o
_
w
o
r
l
d
(
&
c
o
n
t
r
o
l
l
e
r
)
;


 
 
 
 
i
f
 
(
r
e
s
u
l
t
 
!
=
 
E
X
I
T
_
S
U
C
C
E
S
S
)
 
{


 
 
 
 
 
 
 
 
s
y
s
l
o
g
(
L
O
G
_
C
R
I
T
,
 
"
F
a
i
l
e
d
 
t
o
 
e
x
e
c
u
t
e
 
h
e
l
l
o
 
w
o
r
l
d
 
l
o
g
i
c
"
)
;


 
 
 
 
 
 
 
 
c
l
e
a
n
u
p
_
l
o
g
g
i
n
g
(
)
;


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
E
X
I
T
_
F
A
I
L
U
R
E
;


 
 
 
 
}




 
 
 
 
d
i
s
p
l
a
y
_
m
e
s
s
a
g
e
(
&
c
o
n
t
r
o
l
l
e
r
)
;




 
 
 
 
c
l
e
a
n
u
p
_
l
o
g
g
i
n
g
(
)
;


 
 
 
 
r
e
t
u
r
n
 
E
X
I
T
_
S
U
C
C
E
S
S
;


}

                        EOF
                        
#
i
n
c
l
u
d
e
 
<
s
t
d
i
o
.
h
>




i
n
t
 
m
a
i
n
(
)
 
{


 
 
 
 
p
r
i
n
t
f
(
"
H
e
l
l
o
 
W
o
r
l
d
!
\
n
"
)
;


 
 
 
 
r
e
t
u
r
n
 
0
;


}

                        EOF
                        
