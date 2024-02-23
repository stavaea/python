function myplot_att(x,y,title,xl,yl)
    fig = figure;
    fig.Position = [-1919 1 1920 1002];
    maxx = max(y);
    minn = min(y);
    t = maxx - minn;
    t = t*0.05;
    fig.Color = [1 1 1];
    plot(x,y);
    grid minor;
    xlabel(xl,FontSize=15);
    ylabel(yl,FontSize=15);
    axis ([min(x)-1 max(x)+1 min(y)-t max(y)+t]);
%     title()
    x1 = yline(maxx);
    x1.LineWidth = 1.5;
    x1.FontSize = 15;
    x1.Color = 'black';
    x1.LineStyle = '-.';
    x1.Label = sprintf('Max Power %.3f dB',maxx);
    x1.LabelHorizontalAlignment = 'left';
    x1.LabelVerticalAlignment = 'top';
    x2 = yline(minn);
    x2.LineWidth = 1.5;
    x2.FontSize = 15;
    x2.Color = 'black';
    x2.LineStyle = '-.';
    x2.Label = sprintf('Min Power %.3f dB',minn);
    x2.LabelHorizontalAlignment = 'left';
    x2.LabelVerticalAlignment = 'bottom';
end