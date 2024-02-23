% close all;clear all;clc;
%
data=load('20231217_125658_ubw衰减指标测试.mat');

a = data.amp_meas;
amp  = data.amp_meas-data.amp_meas(:,1);
att = [0:0.25:30 30:0.25:93];
% err  = data.amp_meas(i,:)+att;

for i = 1:length(data.fre_set)
    err  = amp(i,:)+att;
    plot(att,err,'.-');
end
% xlabel('Att (dB)');
% ylabel('Att Error (dB)');



% clc ; clear ; close all
% data = load("20231217_125658_ubw衰减指标测试.mat");
% att1 = 0:0.25:30;
% att2 = data.att;
% att = [att1 att2+att1(end)];
% power = data.amp_meas;
% power = power - power(:,1);
% fig = figure;
% fig.Color = [1 1 1];
% % fig.Position = [-1919 1 1920 1002];
% for i = 1:length(data.fre_set)
% % plot(att,power(i,:));
%     att_error = power(i,:) + att;
%     plot(att,att_error);
% end

xlabel('Att (dB)');
ylabel('Att Error (dB)');
minn = min(err);
maxx = max(err);
grid on ; hold on;


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