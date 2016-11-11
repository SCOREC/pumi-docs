outputformat := "png";
outputtemplate := "%j.%o";
prologues := 3;
hppp := 0.25;
vppp := 0.25;

beginfig(1);
picture common;
common = image(
  for i=0 upto 6:
    draw ((0,1) scaled 40 rotated (60 * i)) withpen (pencircle scaled 4);
    draw ((0,1) scaled 40 rotated (60 * i)) --
         ((0,1) scaled 40 rotated (60 * (i + 1)));
  endfor
);
picture before;
before = image(
  draw common;
  for i=0 upto 6:
    draw (0,0)--((0,1) scaled 40 rotated (60 * i));
  endfor
  draw (0,0) withpen (pencircle scaled 4);
);
picture after;
after = image(
  draw common;
  for i=1 upto 5:
    draw ((0,1)--((0,1) rotated (60 * i))) scaled 40;
  endfor
);
draw before;
draw (after shifted (130,0));
picture arrow;
arrow = image(drawarrow (0,0)--(10,0););
draw arrow scaled 3 shifted (50,0);
endfig;

end.

