data=load('20231217_125658_ubw衰减指标测试.mat');

a = data.amp_meas;  %(1:4:374)

amp1=a(:,1:4:121);
amp2=a(:,126:4:374);
amp_range=[amp1 amp2];
% aa=a(0:5:374);
amp  = amp_range-amp_range(:,1);
att = [0:0.25:30 30:0.25:93];
att1=att(1:4:121);
att2=att(126:4:374);
att_range=[att1 att2];
fre=data.fre_set;
for i = 1:length(fre)
    err  = amp(i,:)+att_range;
    plot(att_range,err,'.-');
end
% y=zeros(length(err),length(err));
% for k = 1:length(err)
%     for j = 1:k-1
%         y(k, j) = y(k) - y(j);
%     end
% end
xlim([5 30])
xlabel('Att (dB)','FontSize',20);
ylabel('Att Error (dB)','FontSize',20);
minn = min(err);
maxx = max(err);
grid on ; hold on;
%
%
x1 = yline(maxx);
x1.LineWidth = 1.5;
x1.FontSize = 10;
x1.Color = 'black';
x1.LineStyle = '-.';
x1.Label = sprintf('Max Att %.5f dB',maxx);
x1.LabelHorizontalAlignment = 'left';
x1.LabelVerticalAlignment = 'top';
x2 = yline(minn);
x2.LineWidth = 1.5;
x2.FontSize = 10;
x2.Color = 'black';
x2.LineStyle = '-.';
x2.Label = sprintf('Min Att %.5f dB',minn);
x2.LabelHorizontalAlignment = 'left';
x2.LabelVerticalAlignment = 'bottom';

