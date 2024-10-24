%  a = rand(4, 4);
% [maxV, maxI] = max (a(:));
% [maxR, maxC] = max(maxI);
% sprintf('最大值为：%d,在第%d行，第%d列', maxV, maxR, maxC);

% % 生成一个 4*4 的二维随机数组
% randomArray = randn(4, 4);
%
% % 找出数组中的最大值及其位置
% [maxValue, maxIndex] = max(randomArray(:));
% [maxRow, maxCol] = ind2sub(size(randomArray), maxIndex);
%
% % 使用 sprintf 函数打印输出
% outputString = sprintf('二维数组中最大值为 %f，最大值出现在第 %d 行，第 %d 列', maxValue, maxRow, maxCol);
% disp(outputString);

a = rand(4,4);
[M,I] = max(a);
[N,J] = max(M);
% [I(J),J];
c = I(J);

% [x,y] = find(M);
sprintf('最大值为：%f,在第%d行，第%d列', N, c, J)

% % 使用 randn 函数创建一个4*4的二维随机数组
% A = randn(4,4)   ;
% % 使用 max 函数找出数组中的最大值
% max1 = max(A(:));
% % 使用 find 函数找出最大值所在的行列
% [row, col] = find(A == max1);
% % 使用 sprintf 函数创建字符串以打印输出
% output_string = sprintf('二维数组中的最大值为 %.2f，最大值出现在第 %d 行，第 %d 列', max1, row, col);
% % 打印输出结果
% disp(output_string);