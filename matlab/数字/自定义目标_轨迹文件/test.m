clear all;
clc;

count=5; %检测车辆数
count1=uint32(count);
count2=int32(count);
M =5; %车道数
L =1000; %车道长度
d =10; %车道宽度
m1 = [3 3 3 3 3];%车道号
m2 = [3 3 3 3 3]; %驶入车道
% R1a = [0 69 50 104 0]; %起始纵坐标
% R1b = [68 50 30 49 45]; %结束纵坐标
R1a = [0 69 50 104 0]; %起始纵坐标
R1b = [10 50 30 49 45]; %结束纵坐标
V1a =[-10 10 6 17 -13]; %初始速度
V1b =[-10 10 6 17 -13]; %结束速度
v2 =[-10 10 6 17 -13];  %转弯速度
V3a =[-10 10 6 17 -13];  %第三阶段初始速度
V3b =[-10 10 6 17 -13];  %第三阶段结束速度
R3 = [100 0 0 0 59];
R2 = R1b+v2./abs(v2).*abs(m2-m1);  %转弯结束纵坐标
t=0.0010;  %单位s 精度0.1ms
RCS=[10 10 10 10 10 5+rand*(20.0-5.0) 5+rand*(20.0-5.0) 5+rand*(20.0-5.0) 5+rand*(20.0-5.0) 5+rand*(20.0-5.0)];
% RCS=30;


t1000=t.*10000;
t1001=t.*1000;
V1a=-V1a;V1b=-V1b;v2=-v2;V3a=-V3a;V3b=-V3b;


if count>=1
fidout1=fopen('SelfDefineTarget1.txt','w');
end
if count>=2
fidout2=fopen('SelfDefineTarget2.txt','w');
end
if count>=3
fidout3=fopen('SelfDefineTarget3.txt','w');
end
if count>=4
fidout4=fopen('SelfDefineTarget4.txt','w');
end
if count>=5
fidout5=fopen('SelfDefineTarget5.txt','w');
end

fidout6=fopen('SelfDefineTarget0.txt','w');%标校目标产生时 目标数只能是1
fidout7=fopen('SelfDefineTarget0.dat','w');
fprintf(fidout6,'有效目标数：\n %d\n',count1);
fwrite(fidout7,count2,'int32');

fprintf(fidout6,'轨迹总点数：\n %d\n',5000);
fprintf(fidout6,'参数更新间隔m/s：\n %d\n',t1001);
fwrite(fidout7,5000,'int32');
fwrite(fidout7,t1000,'int32');
fprintf(fidout6,'径向距离/m   运动方向/°  径向速度/ms      角度/° \t     RCS/dBsm \n');
for n1=1:1:5000
fprintf(fidout6,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', 56.550,0.000,0.000,0.000,16.0);
end
for n1=1:1:5000

fwrite(fidout7,56550,'int32');
fwrite(fidout7,0,'int32');
fwrite(fidout7,5250,'int32');
fwrite(fidout7,0,'int32');
fwrite(fidout7,160,'int32');
end
fclose(fidout6);
fclose(fidout7);


fidout8=fopen('SelfDefineTarget.dat','w');
if count>=1
fprintf(fidout1,'有效目标数：\n %d\n',count1);
end
if count>=2
fprintf(fidout2,'有效目标数：\n %d\n',count1);
end
if count>=3
fprintf(fidout3,'有效目标数：\n %d\n',count1);
end
if count>=4
fprintf(fidout4,'有效目标数：\n %d\n',count1);
end
if count>=5
fprintf(fidout5,'有效目标数：\n %d\n',count1);
end

fwrite(fidout8,count2,'int32');



    D1 = abs(R1a-R1b);
    a1=V1b./abs(V1b).*(V1b.*V1b-V1a.*V1a)./2./D1;
    t1=abs(2.*D1./(V1a+V1b));
    N1=t1/t;




    D2 = 2^0.5 .*v2./abs(v2).*abs(m2-m1);

    t2 = abs(D2./v2);
    N2 = t2/t;




    D3 =abs(R2-R3);
    a3 =V3b./abs(V3b).*(V3b.*V3b-V3a.*V3a)./2./D3;
    t3 =abs(2.*D3./(V3a+V3b));
    N3 =t3/t;


    N=floor(N1)+floor(N2)+floor(N3);
    Ntest=0;
    for i=1:count
        if N(i)>=Ntest
            Ntest=N(i);
        end
    end



    Nn=int32(Ntest);





if (1<Ntest)&&(Ntest<208000)
    if count>=1
fprintf(fidout1,'轨迹总点数：\n %d\n',Ntest);

fprintf(fidout1,'参数更新间隔/ms：\n %d\n',t1001);
    end
if count>=2
fprintf(fidout2,'轨迹总点数：\n %d\n',Ntest);
fprintf(fidout2,'参数更新间隔/ms：\n %d\n',t1001);
end
if count>=3
fprintf(fidout3,'轨迹总点数：\n %d\n',Ntest);
fprintf(fidout3,'参数更新间隔/ms：\n %d\n',t1001);
end
if count>=4
fprintf(fidout4,'轨迹总点数：\n %d\n',Ntest);
fprintf(fidout4,'参数更新间隔/ms：\n %d\n',t1001);
end
if count>=5
fprintf(fidout5,'轨迹总点数：\n %d\n',Ntest);
fprintf(fidout5,'参数更新间隔/ms：\n %d\n',t1001);
end
else
    fprintf(fidout1,'error');
    fprintf(fidout2,'error');
    fprintf(fidout3,'error');
    fprintf(fidout4,'error');
    fprintf(fidout5,'error');
end

fwrite(fidout8,Nn,'int32');
    fwrite(fidout8,t1000,'int32');
    if count>=1
fprintf(fidout1,'当前目标编号：\n %d\n',1);
end
if count>=2
fprintf(fidout2,'当前目标编号：\n %d\n',2);
end
if count>=3
fprintf(fidout3,'当前目标编号：\n %d\n',3);
end
if count>=4
fprintf(fidout4,'当前目标编号：\n %d\n',4);
end
if count>=5
fprintf(fidout5,'当前目标编号：\n %d\n',5);
end



    if count>=1
fprintf(fidout1,'径向距离/m   运动方向/°  径向速度/m/s      角度/° \t    RCS/dBsm \n');
    end
if count>=2
fprintf(fidout2,'径向距离/m   运动方向/°  径向速度/m/s      角度/° \t    RCS/dBsm \n');
end
if count>=3
fprintf(fidout3,'径向距离/m   运动方向/°  径向速度/m/s      角度/° \t    RCS/dBsm \n');
end
if count>=4
fprintf(fidout4,'径向距离/m   运动方向/°  径向速度/m/s      角度/° \t    RCS/dBsm \n');
end
if count>=5
fprintf(fidout5,'径向距离/m   运动方向/°  径向速度/m/s      角度/° \t    RCS/dBsm \n');
end
det=[0 0 0 0 0];
angBAY=[0 0 0 0 0];
angBAY2=[0 0 0 0 0];
angBAY3=[0 0 0 0 0];
if count>=1
for n1=1:1:N1(1)


    x1= (m1-1/2-M/2).*d;
    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(1);y1(1)];
    B=[x1(1);y1next(1)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY(1)=0.000;
        else
            angBAY(1)=180.000;
        end
        elseif AB(1) > 0
    angBAY(1) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(1) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end


if y1(1)==0
    if x1(1)==0
        det(1)=0.000;
    elseif x1(1)>0
            det(1)=90.000;

    elseif x1(1)<0
          det(1)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);


     fprintf(fidout1,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R1tn(1),angBAY(1),V1nt(1),det(1),RCS(1));

end
end
if count>=2
for n1=1:1:N1(2)


    x1= (m1-1/2-M/2).*d;

    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(2);y1(2)];
    B=[x1(2);y1next(2)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;

    if AB(1) == 0
        if AB(2)>=0
            angBAY(2)=0.000;
        else
            angBAY(2)=180.000;
        end
        elseif AB(1) > 0
    angBAY(2) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(2) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y1(2)==0
    if x1(2)==0
        det(2)=0.000;
    elseif x1(2)>0
            det(2)=90.000;

    elseif x1(2)<0
          det(2)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);
fprintf(fidout2,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R1tn(2),angBAY(2),V1nt(2),det(2),RCS(2));

end
end
if count>=3
for n1=1:1:N1(3)


    x1= (m1-1/2-M/2).*d;

    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(3);y1(3)];
    B=[x1(3);y1next(3)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY(3)=0.000;
        else
            angBAY(3)=180.000;
        end
        elseif AB(1) > 0
    angBAY(3) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(3) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y1(3)==0
    if x1(3)==0
        det(3)=0.000;
    elseif x1(3)>0
            det(3)=90.000;

    elseif x1(3)<0
          det(3)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);
fprintf(fidout3,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R1tn(3),angBAY(3),V1nt(3),det(3),RCS(3));

end
end
if count>=4
for n1=1:1:N1(4)


    x1= (m1-1/2-M/2).*d;

    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(4);y1(4)];
    B=[x1(4);y1next(4)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY(4)=0.000;
        else
            angBAY(4)=180.000;
        end
        elseif AB(1) > 0
    angBAY(4) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(4) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y1(4)==0
    if x1(4)==0
        det(4)=0.000;
    elseif x1(4)>0
            det(4)=90.000;

    elseif x1(4)<0
          det(4)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);
fprintf(fidout4,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R1tn(4),angBAY(4),V1nt(4),det(4),RCS(4));

end
end
if count>=5
for n1=1:1:N1(5)


    x1= (m1-1/2-M/2).*d;

    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(5);y1(5)];
    B=[x1(5);y1next(5)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY(5)=0.000;
        else
            angBAY(5)=180.000;
        end
        elseif AB(1) > 0
    angBAY(5) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(5) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y1(5)==0
    if x1(5)==0
        det(5)=0.000;
    elseif x1(5)>0
            det(5)=90.000;

    elseif x1(5)<0
          det(5)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);
fprintf(fidout5,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R1tn(5),angBAY(5),V1nt(5),det(5),RCS(5));

end
end




if count>=1
for n2=1:1:N2(1)
   if N2(1)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(1);y2(1)];
    B=[x2next(1);y2next(1)];
    AB=(B-A);
   C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(1)=0.000;
        else
            angBAY2(1)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(1) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(1) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y2(1)==0
    if x2(1)==0
        det(1)=0.000;
    elseif x2(1)>0
            det(1)=90.000;

    elseif x2(1)<0
          det(1)=-90.000;

    end

else
det = atan(x2./y2);
end
v21 = -v2;
V2nt = v21.*cos(det);


    fprintf(fidout1,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R2tn(1),angBAY2(1),V2nt(1),det(1),RCS(1));


end
end
if count>=2
for n2=1:1:N2(2)
   if N2(2)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(2);y2(2)];
    B=[x2next(2);y2next(2)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(2)=0.000;
        else
            angBAY2(2)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(2) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(2) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y2(2)==0
    if x2(2)==0
        det(2)=0.000;
    elseif x2(2)>0
            det(2)=90.000;

    elseif x2(2)<0
          det(2)=-90.000;

    end

else
det = atan(x2./y2);
end
v21 = -v2;
V2nt = v21.*cos(det);


    fprintf(fidout2,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R2tn(2),angBAY2(2),V2nt(2),det(2),RCS(2));

end
end
if count>=3
for n2=1:1:N2(3)
   if N2(3)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(3);y2(3)];
    B=[x2next(3);y2next(3)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(3)=0.000;
        else
            angBAY2(3)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(3) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(3) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y2(3)==0
    if x2(3)==0
        det(3)=0.000;
    elseif x2(3)>0
            det(3)=90.000;

    elseif x2(3)<0
          det(3)=-90.000;

    end

else
det = atan(x2./y2);
end
v21 = -v2;
V2nt = v21.*cos(det);


    fprintf(fidout3,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R2tn(3),angBAY(3),V2nt(3),det(3),RCS(3));


end
end
if count>=4
for n2=1:1:N2(4)
   if N2(4)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(4);y2(4)];
    B=[x2next(4);y2next(4)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(4)=0.000;
        else
            angBAY2(4)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(4) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(4) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y2(4)==0
    if x2(4)==0
        det(4)=0.000;
    elseif x2(4)>0
            det(4)=90.000;

    elseif x2(4)<0
          det(4)=-90.000;

    end

else
det = atan(x2./y2);
end
v21 = -v2;
V2nt = v21.*cos(det);


    fprintf(fidout4,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n', R2tn(4),angBAY(4),V2nt(4),det(4),RCS(4));


end
end
if count>=5
for n2=1:1:N2(5)
   if N2(5)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(5);y2(5)];
    B=[x2next(5);y2next(5)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(5)=0.000;
        else
            angBAY2(5)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(5) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(5) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y2(5)==0
    if x2(5)==0
        det(5)=0.000;
    elseif x2(5)>0
            det(5)=90.000;

    elseif x2(5)<0
          det(5)=-90.000;

    end

else
det = atan(x2./y2);
end
v21 = -v2;
V2nt = v21.*cos(det);


    fprintf(fidout5,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n',R2tn(5),angBAY(5),V2nt(5),det(5),RCS(5));

 end
end


if count>=1
for n3=1:1:N3(1)
    x3= (m2-1/2-M/2).*d;
    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
    y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(1);y3(1)];
    B=[x3(1);y3next(1)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(1)=0.000;
        else
            angBAY3(1)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(1) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(1) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y3(1)==0
    if x3(1)==0
        det(1)=0.000;
    elseif x3(1)>0
            det(1)=90.000;

    elseif x3(1)<0
          det(1)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);

    fprintf(fidout1,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(1),angBAY3(1),V3nt(1),det(1),RCS(1));
end

if Ntest>N(1)
    for i=1:1:(Ntest-N(1))
        fprintf(fidout1,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(1),angBAY3(1),0.000,det(1),RCS(1));
    end
end
end

if count>=2
for n3=1:1:N3(2)
    x3= (m2-1/2-M/2).*d;
    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
    y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(2);y3(2)];
    B=[x3(2);y3next(2)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(2)=0.000;
        else
            angBAY3(2)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(2) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(2) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y3(2)==0
    if x3(2)==0
        det(2)=0.000;
    elseif x3(2)>0
            det(2)=90.000;

    elseif x3(2)<0
          det(2)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);

    fprintf(fidout2,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(2),angBAY3(2),V3nt(2),det(2),RCS(2));

end
if Ntest>N(2)
    for i=1:1:(Ntest-N(2))
        fprintf(fidout2,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(2),angBAY3(2),0.000,det(2),RCS(2));
    end
end
end
if count>=3
for n3=1:1:N3(3)
    x3= (m2-1/2-M/2).*d;
    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
    y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(3);y3(3)];
    B=[x3(3);y3next(3)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(3)=0.000;
        else
            angBAY3(3)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(3) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(3) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y3(3)==0
    if x3(3)==0
        det(3)=0.000;
    elseif x3(3)>0
            det(3)=90.000;

    elseif x3(3)<0
          det(3)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);

    fprintf(fidout3,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(3),angBAY3(3),V3nt(3),det(3),RCS(3));

end
if Ntest>N(3)
    for i=1:1:(Ntest-N(3))
        fprintf(fidout3,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(3),angBAY3(3),0,det(3),RCS(3));
    end
end
end
if count>=4
for n3=1:1:N3(4)
    x3= (m2-1/2-M/2).*d;
    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
    y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(4);y3(4)];
    B=[x3(4);y3next(4)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(4)=0.000;
        else
            angBAY3(4)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(4) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(4) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y3(4)==0
    if x3(4)==0
        det(4)=0.000;
    elseif x3(4)>0
            det(4)=90.000;

    elseif x3(4)<0
          det(4)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);

    fprintf(fidout4,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(4),angBAY3(4),V3nt(4),det(4),RCS(4));

end
if Ntest>N(4)
    for i=1:1:(Ntest-N(4))
        fprintf(fidout4,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(4),angBAY3(4),0,det(4),RCS(4));
    end
end
end
if count>=5
for n3=1:1:N3(5)
    x3= (m2-1/2-M/2).*d;
    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
    y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(5);y3(5)];
    B=[x3(5);y3next(5)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(5)=0.000;
        else
            angBAY3(5)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(5) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(5) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y3(5)==0
    if x3(5)==0
        det(5)=0.000;
    elseif x3(5)>0
            det(5)=90.000;

    elseif x3(5)<0
          det(5)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);

    fprintf(fidout5,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(5),angBAY3(5),V3nt(5),det(5),RCS(5));

end
if Ntest>N(5)
    for i=1:1:(Ntest-N(5))
        fprintf(fidout5,'%.3f      %.3f        %.3f       \t %.3f°     %.1f \n' ,R3tn(5),angBAY3(5),0,det(5),RCS(5));
    end
end
end

for iii=1:count
for n1=1:1:N1(iii)


    x1= (m1-1/2-M/2).*d;

    y1 = R1a+V1a.*n1.*t+a1.*(n1.*t)^2/2;
    R1tn = (x1.*x1+y1.*y1).^(1/2);
    y1next=R1a+V1a.*(n1+1).*t+a1.*((n1+1).*t)^2/2;
    A=[x1(iii);y1(iii)];
    B=[x1(iii);y1next(iii)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY(iii)=0.000;
        else
            angBAY(iii)=180.000;
        end
        elseif AB(1) > 0
    angBAY(iii) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY(iii) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end

if y1(iii)==0
    if x1(iii)==0
        det(iii)=0.000;
    elseif x1(iii)>0
            det(iii)=90.000;

    elseif x1(iii)<0
          det(iii)=-90.000;

    end

else
det = atan(x1./y1);
end
V1n = -(V1a+a1.*n1.*t);
V1nt = V1n.*cos(det);



fwrite(fidout8,1000.*R1tn(iii),'int32');
fwrite(fidout8,1000.*angBAY(iii),'int32');
fwrite(fidout8,1000.*V1nt(iii),'int32');
fwrite(fidout8,1000.*det(iii),'int32');
fwrite(fidout8,10.*RCS(iii),'int32');
 end




for n2=1:1:N2(iii)
   if N2(iii)==0
       break;
   end

    x2= (m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    y2 = R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*n2.*t).*d;
    R2tn = (x2.*x2+y2.*y2).^(1/2);
    y2next=R1b+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    x2next=(m1-1/2-M/2).*d+(m2-m1)/abs(m2-m1).*(v2.*2^0.5.*(n2+1).*t).*d;
    A=[x2(iii);y2(iii)];
    B=[x2(iii);y2next(iii)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY2(iii)=0.000;
        else
            angBAY2(iii)=180.000;
        end
        elseif AB(1) > 0
    angBAY2(iii) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY2(iii) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y2(iii)==0
    if x2(iii)==0
        det(iii)=0.000;
    elseif x2(iii)>0
            det(iii)=90.000;

    elseif x2(iii)<0
          det(iii)=-90.000;

    end

else
det = atan(x2./y2);
end
V2nt = -v2.*cos(det);


fwrite(fidout8,1000.*R2tn(iii),'int32');
fwrite(fidout8,1000.*angBAY2(iii),'int32');
fwrite(fidout8,1000.*V2nt(iii),'int32');
fwrite(fidout8,1000.*det(iii),'int32');
fwrite(fidout8,10.*RCS(iii),'int32');
 end



for n3=1:1:N3(iii)


    x3= (m2-1/2-M/2).*d;

    y3 = R2+V3a.*n3.*t+a3.*(n3.*t)^2/2;
    R3tn = (x3.*x3+y3.*y3).^(1/2);
y3next=R2+V3a.*(n3+1).*t+a3.*((n3+1).*t)^2/2;
    A=[x3(iii);y3(iii)];
    B=[x3(iii);y3next(iii)];
    AB=(B-A);
    C = [0;1];
    A = [0;0];
    B = AB;
    if AB(1) == 0
        if AB(2)>=0
            angBAY3(iii)=0.000;
        else
            angBAY3(iii)=180.000;
        end
        elseif AB(1) > 0
    angBAY3(iii) = acosd((norm(A-B)^2+norm(A-C)^2-...
        norm(B-C)^2)/(2*(norm(A-B)*norm(A-C))));
elseif AB(1) < 0
    angBAY3(iii) = -acosd((norm(A-B)^2+norm(A+C)^2-...
        norm(B+C)^2)/(2*(norm(A-B)*norm(A+C))));
    end
if y3(iii)==0
    if x3(iii)==0
        det(iii)=0.000;
    elseif x3(iii)>0
            det(iii)=90.000;

    elseif x3(iii)<0
          det(iii)=-90.000;

    end

else
det = atan(x3./y3);
end
V3n = -(V3a+a3.*n3.*t);
V3nt = V3n.*cos(det);


fwrite(fidout8,1000.*R3tn(iii),'int32');
fwrite(fidout8,1000.*angBAY3(iii),'int32');
fwrite(fidout8,1000.*V3nt(iii),'int32');
fwrite(fidout8,1000.*det(iii),'int32');
fwrite(fidout8,10.*RCS(iii),'int32');
end

 if Ntest>N(iii)
    for i=1:1:(Ntest-N(iii))
fwrite(fidout8,1000.*R3tn(iii),'int32');
fwrite(fidout8,1000.*angBAY3(iii),'int32');
fwrite(fidout8,0,'int32');
fwrite(fidout8,1000.*det(iii),'int32');
fwrite(fidout8,10.*RCS(iii),'int32');

    end
 end
end

if count>=1
fclose(fidout1);
end
if count>=2
fclose(fidout2);
end
if count>=3
fclose(fidout3);
end
if count>=4
fclose(fidout4);
end
if count>=5
fclose(fidout5);
end
fclose(fidout8);





