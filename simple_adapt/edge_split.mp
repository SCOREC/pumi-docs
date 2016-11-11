outputformat := "png";
outputtemplate := "%j.%o";
prologues := 3;
hppp := 0.25;
vppp := 0.25;

beginfig(1);
path diamond;
diamond = ((1,0)--(2,1)--(1,2)--(0,1)--cycle) scaled 40;
picture bound;
bound = image(
  draw diamond;
  for i=0 upto length diamond:
    draw (point i of diamond) withpen (pencircle scaled 4);
  endfor
);
path horiz;
horiz = ((0,1)--(2,1)) scaled 40;
path vert;
vert = ((1,0)--(1,2)) scaled 40;
draw bound;
draw horiz;
draw bound shifted (130,0);
draw horiz shifted (130,0);
draw vert shifted (130,0);
draw (((1,1) scaled 40) shifted (130,0)) withpen (pencircle scaled 4);
picture arrow;
arrow = image(drawarrow (0,0)--(10,0););
draw arrow scaled 3 shifted (90,40);
endfig;

end.
