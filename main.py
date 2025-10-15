                        i
m
p
o
r
t
 
l
o
g
g
i
n
g


f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
L
i
s
t




c
l
a
s
s
 
F
i
b
o
n
a
c
c
i
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
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
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
i
n
g
.
g
e
t
L
o
g
g
e
r
(
_
_
n
a
m
e
_
_
)


 
 
 
 
 
 
 
 
l
o
g
g
i
n
g
.
b
a
s
i
c
C
o
n
f
i
g
(
l
e
v
e
l
=
l
o
g
g
i
n
g
.
I
N
F
O
)




 
 
 
 
d
e
f
 
g
e
n
e
r
a
t
e
_
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
(
s
e
l
f
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
 
=
 
[
0
,
 
1
]


 
 
 
 
 
 
 
 
 
 
 
 
w
h
i
l
e
 
l
e
n
(
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
)
 
<
 
1
0
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
n
e
x
t
_
n
u
m
b
e
r
 
=
 
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
[
-
1
]
 
+
 
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
[
-
2
]


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
.
a
p
p
e
n
d
(
n
e
x
t
_
n
u
m
b
e
r
)


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
E
x
c
e
p
t
i
o
n
 
a
s
 
e
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
l
o
g
g
e
r
.
e
r
r
o
r
(
f
"
E
r
r
o
r
 
g
e
n
e
r
a
t
i
n
g
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
:
 
{
e
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e




 
 
 
 
d
e
f
 
p
r
i
n
t
_
f
i
b
o
n
a
c
c
i
(
s
e
l
f
)
 
-
>
 
N
o
n
e
:


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
q
u
e
n
c
e
 
=
 
s
e
l
f
.
g
e
n
e
r
a
t
e
_
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
(
)


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
n
u
m
b
e
r
 
i
n
 
s
e
q
u
e
n
c
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
n
u
m
b
e
r
)


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
E
x
c
e
p
t
i
o
n
 
a
s
 
e
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
l
o
g
g
e
r
.
e
r
r
o
r
(
f
"
E
r
r
o
r
 
p
r
i
n
t
i
n
g
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
:
 
{
e
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e




 
 
 
 
d
e
f
 
g
e
t
_
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
(
s
e
l
f
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
n
e
r
a
t
e
_
f
i
b
o
n
a
c
c
i
_
s
e
q
u
e
n
c
e
(
)


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
E
x
c
e
p
t
i
o
n
 
a
s
 
e
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
l
o
g
g
e
r
.
e
r
r
o
r
(
f
"
E
r
r
o
r
 
r
e
t
r
i
e
v
i
n
g
 
F
i
b
o
n
a
c
c
i
 
s
e
q
u
e
n
c
e
:
 
{
e
}
"
)


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e




d
e
f
 
m
a
i
n
(
)
:


 
 
 
 
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
 
F
i
b
o
n
a
c
c
i
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
)


 
 
 
 
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
.
p
r
i
n
t
_
f
i
b
o
n
a
c
c
i
(
)




i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
"
_
_
m
a
i
n
_
_
"
:


 
 
 
 
m
a
i
n
(
)

                        EOF
                        
