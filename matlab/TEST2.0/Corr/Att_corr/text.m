x = 0:5:100;
y = 1:5:101;
x1 = 0:0.5:127.5;
% y11 = repmat(y,1,20);
y11 = repmat(y,20,1);
% y1 = zeros(20,256);
x11 = repmat(x,20,1);
y111 = zeros(20,256);
for i = 1:1:20
    y111(i,:) = interp1(x11(i,:),y11(i,:),x1,'linear','extrap');
end