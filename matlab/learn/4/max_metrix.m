function[max_A,position] = max_metrix(A);
[y,i] = max(A);
[max_A,j] = max(y);
position=[i(j),j];