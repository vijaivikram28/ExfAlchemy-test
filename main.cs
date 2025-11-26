                        u
s
i
n
g
 
S
y
s
t
e
m
;


u
s
i
n
g
 
M
i
c
r
o
s
o
f
t
.
E
x
t
e
n
s
i
o
n
s
.
L
o
g
g
i
n
g
;




p
u
b
l
i
c
 
c
l
a
s
s
 
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


{


 
 
 
 
p
r
i
v
a
t
e
 
r
e
a
d
o
n
l
y
 
I
L
o
g
g
e
r
<
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
>
 
_
l
o
g
g
e
r
;




 
 
 
 
p
u
b
l
i
c
 
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
(
I
L
o
g
g
e
r
<
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
>
 
l
o
g
g
e
r
)


 
 
 
 
{


 
 
 
 
 
 
 
 
_
l
o
g
g
e
r
 
=
 
l
o
g
g
e
r
 
?
?
 
t
h
r
o
w
 
n
e
w
 
A
r
g
u
m
e
n
t
N
u
l
l
E
x
c
e
p
t
i
o
n
(
n
a
m
e
o
f
(
l
o
g
g
e
r
)
)
;


 
 
 
 
}




 
 
 
 
p
u
b
l
i
c
 
v
o
i
d
 
P
r
i
n
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
(
)


 
 
 
 
{


 
 
 
 
 
 
 
 
t
r
y


 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
_
l
o
g
g
e
r
.
L
o
g
I
n
f
o
r
m
a
t
i
o
n
(
"
A
t
t
e
m
p
t
i
n
g
 
t
o
 
p
r
i
n
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
 
m
e
s
s
a
g
e
"
)
;


 
 
 
 
 
 
 
 
 
 
 
 
C
o
n
s
o
l
e
.
W
r
i
t
e
L
i
n
e
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
"
)
;


 
 
 
 
 
 
 
 
 
 
 
 
_
l
o
g
g
e
r
.
L
o
g
I
n
f
o
r
m
a
t
i
o
n
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
 
m
e
s
s
a
g
e
 
p
r
i
n
t
e
d
 
s
u
c
c
e
s
s
f
u
l
l
y
"
)
;


 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 
c
a
t
c
h
 
(
E
x
c
e
p
t
i
o
n
 
e
x
)


 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
_
l
o
g
g
e
r
.
L
o
g
E
r
r
o
r
(
e
x
,
 
"
A
n
 
e
r
r
o
r
 
o
c
c
u
r
r
e
d
 
w
h
i
l
e
 
p
r
i
n
t
i
n
g
 
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
 
m
e
s
s
a
g
e
"
)
;


 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
;


 
 
 
 
 
 
 
 
}


 
 
 
 
}




 
 
 
 
p
u
b
l
i
c
 
v
o
i
d
 
E
x
e
c
u
t
e
(
)


 
 
 
 
{


 
 
 
 
 
 
 
 
t
r
y


 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
P
r
i
n
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
(
)
;


 
 
 
 
 
 
 
 
}


 
 
 
 
 
 
 
 
c
a
t
c
h
 
(
E
x
c
e
p
t
i
o
n
 
e
x
)


 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
_
l
o
g
g
e
r
.
L
o
g
C
r
i
t
i
c
a
l
(
e
x
,
 
"
U
n
h
a
n
d
l
e
d
 
e
x
c
e
p
t
i
o
n
 
i
n
 
E
x
e
c
u
t
e
 
m
e
t
h
o
d
"
)
;


 
 
 
 
 
 
 
 
 
 
 
 
E
n
v
i
r
o
n
m
e
n
t
.
E
x
i
t
(
1
)
;


 
 
 
 
 
 
 
 
}


 
 
 
 
}


}

                        EOF
                        
