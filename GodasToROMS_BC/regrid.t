// supply one array A(N,N) defined on the grid [0,N-1]x[0,N-1], 
// return another array defined on the rotated 45 degree grid
// the initial array is one period of a periodic function
//
// the initial unit vector \hat{i} and \hat{j} is in the x, y directions.
// transformed into on \hat{u}=\hat{i}+\hat{j} and \hat{v}=-\hat{i}+\hat{j}
// (i,j)->(u,v)=((i+j)/2, (-i+j)/2)
// (u,v)->(i,j)=(u-v, u+v)
// they are all periodic over the first and second index
//
function [y]=rotate45(A, d1, d2)
/*  rotate the array A anticlockwise 45 degree on the plane (d1,d2)
    where d1<d2 is two indices and they form a xy coordinates.
    the origin of the rotation is the (1,1) point of (d1,d2)
    the axis is rotated clockwise 45 degrees
    y is undefined if 
    1: arguments error, A is not an array, or A does not have d1 or d2 
       dimension, or d1>=d2
    2: d1 or d2 does not have the same length
*/
{
  if ( !isint(d1) || !isint(d2) || !isarray(A) ) return;
  r=rank(A);
  if ( d1>r || d1<0 ) return;
  if ( d2>r || d2<0 || d2<=d1 ) return;
  V=size(A);
  if ( V[d1]!=V[d2] ) return;
  N=V[d1];

  // reshape to a[v1,v[d1],v2,v[d2],v3)
  v1=1; v2=1; v3=1;
  foreach (i=1:d1-1)
    v1*=V[i];
  foreach (i=d1+1:d2-1)
    v2*=V[i];
  foreach (i=d2+1:r)
    v3*=V[i];
  a=reshape(A, v1, N, v2, N, v3);

  if ( isint(a) ) y=izeros(v1,N,v2,N,v3)
  else if ( isfloat(a) ) y=zeros(v1,N,v2,N,v3)
  else y=czeros(v1,N,v2,N,v3); 

  // now real rotation stuff
  foreach (u=0:N-1)
    foreach (v=0:N-1)
      {
        i=(u-v) mod N;
        if (i<0) i+=N;
        j=(u+v) mod N;
        y[v1,u+1,v2,v+1,v3]=a[v1,i+1,v2,j+1,v3];
      };

  // shape back
  y=reshape(y,V);
};
 
function [y]=rotateNeg45(A, d1, d2)
/*  rotate the array A anticlockwise -45 degree on the plane (d1,d2)
    where d1<d2 is two indices and they form a xy coordinates.
    the origin of the rotation is the (1,1) point of (d1,d2)
    the axis is rotated clockwise -45 degrees
    y is undefined if 
    1: arguments error, A is not an array, or A does not have d1 or d2 
       dimension, or d1>=d2
    2: d1 or d2 does not have the same length
*/
{
  if ( !isint(d1) || !isint(d2) || !isarray(A) ) return;
  r=rank(A);
  if ( d1>r || d1<0 ) return;
  if ( d2>r || d2<0 || d2<=d1 ) return;
  V=size(A);
  if ( V[d1]!=V[d2] ) return;
  N=V[d1];

  // reshape to a[v1,v[d1],v2,v[d2],v3)
  v1=1; v2=1; v3=1;
  foreach (i=1:d1-1)
    v1*=V[i];
  foreach (i=d1+1:d2-1)
    v2*=V[i];
  foreach (i=d2+1:r)
    v3*=V[i];
  a=reshape(A, v1, N, v2, N, v3);

  if ( isint(a) ) y=izeros(v1,N,v2,N,v3)
  else if ( isfloat(a) ) y=zeros(v1,N,v2,N,v3)
  else y=czeros(v1,N,v2,N,v3); 

  // now real rotation stuff
  // (i,j)->(u,v)=((i-j)/2, (i+j)/2)
  // (u,v)->(i,j)=(u+v,-u+v)
  foreach (u=0:N-1)
    foreach (v=0:N-1)
      {
        i=(u+v) mod N;
        j=(-u+v) mod N;
        if (j<0) j+=N;
        y[v1,u+1,v2,v+1,v3]=a[v1,i+1,v2,j+1,v3];
      };

  // shape back
  y=reshape(y,V);
};
 
function [y]=rotate45(A, d1, d2)
/*  rotate the array A anticlockwise 45 degree on the plane (d1,d2)
    where d1<d2 is two indices and they form a xy coordinates.
    the origin of the rotation is the (1,1) point of (d1,d2)
    the axis is rotated clockwise 45 degrees. The lengths of d1, d2 
    can be different
    y is undefined if 
    arguments error, A is not an array, or A does not have d1 or d2 
    dimension, or d1>=d2
*/
{
  if ( !isint(d1) || !isint(d2) || !isarray(A) ) return;
  r=rank(A);
  if ( d1>r || d1<0 ) return;
  if ( d2>r || d2<0 || d2<=d1 ) return;
  V=size(A);
  if ( V[d1]!=V[d2] ) return;
  N=V[d1];

  // reshape to a[v1,v[d1],v2,v[d2],v3)
  v1=1; v2=1; v3=1;
  foreach (i=1:d1-1)
    v1*=V[i];
  foreach (i=d1+1:d2-1)
    v2*=V[i];
  foreach (i=d2+1:r)
    v3*=V[i];
  a=reshape(A, v1, N, v2, N, v3);

  if ( isint(a) ) y=izeros(v1,N,v2,N,v3)
  else if ( isfloat(a) ) y=zeros(v1,N,v2,N,v3)
  else y=czeros(v1,N,v2,N,v3); 

  // now real rotation stuff
  foreach (u=0:N-1)
    foreach (v=0:N-1)
      {
        i=(u-v) mod N;
        if (i<0) i+=N;
        j=(u+v) mod N;
        y[v1,u+1,v2,v+1,v3]=a[v1,i+1,v2,j+1,v3];
      };

  // shape back
  y=reshape(y,V);
};

