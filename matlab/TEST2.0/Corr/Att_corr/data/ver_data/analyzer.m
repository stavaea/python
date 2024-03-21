clc ; clear ; close all
%% Load Data
data = load("20240304_145852_Ver_coll.mat");
%% 数据处理
att_77 = data.amp_meas(:,:,1);
att_79 = data.amp_meas(:,:,2);
att_80 = data.amp_meas(:,:,3);

att_77 = att_77 - att_77(:,1);
att_79 = att_79 - att_79(:,1);
att_80 = att_80 - att_80(:,1);

att_error_77 = att_77 + data.Att;
att_error_79 = att_79 + data.Att;
att_error_80 = att_80 + data.Att;

error_range_77 = range(att_error_77');
error_range_79 = range(att_error_79');
error_range_80 = range(att_error_80');

%% 画图
[row, col] = size(att_77);
x = data.Att;
% for i = 1:row
%     figure('Name','衰减修正','NumberTitle','off','Position',[-1919 1 1920 1002],'Color',[1 1 1]);
%     subplot(121)
%     plot(x,att_77(i,:));
%     hold on
%     plot(x,att_79(i,:));
%     plot(x,att_80(i,:));
%     xlabel('Set Att (dB)','FontSize',15);
%     ylabel('Coll Power (dBm)','FontSize',15);
%     title(sprintf('%3.0f MHz 衰减曲线',data.fre_set(i)),'FontSize',15);
%     grid minor
%     legend(['本振77000MHZ';'本振79000MHZ';'本振80000MHZ']);
%     subplot(122)
%     plot(x,att_error_77(i,:));
%     hold on
%     plot(x,att_error_79(i,:));
%     plot(x,att_error_80(i,:));
%     xlabel('Set Att (dB)','FontSize',15);
%     ylabel('Att Error (dB)','FontSize',15);
%     title(sprintf('%3.0f MHz 衰减误差曲线',data.fre_set(i)),'FontSize',15);
%     grid minor
%     legend(['本振77000MHZ';'本振79000MHZ';'本振80000MHZ']);
%     close all
% end

%%
for i = 1:row
%     figure('Name','衰减修正','NumberTitle','off','Position',[-1919 1 1920 1002],'Color',[1 1 1]);
%     plot(x,att_error_77(i,:));
%     plot(x,att_error_79(i,:));
    plot(x,att_error_80(i,:));
    hold on
    xlabel('Set Att (dB)','FontSize',15);
    ylabel('Att Error (dB)','FontSize',15);
%     title(sprintf('%3.0f MHz 衰减误差曲线',data.fre_set(i)),'FontSize',15);
    set(gcf,'Color',[1 1 1]);
    set(gcf,'Position',[1 1 1920 1002]);
    grid minor
end
    get_line(-0.3);
    get_line(0.3);