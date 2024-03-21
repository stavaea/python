function get_line(number)
    y = yline(number);
    y.LineWidth = 1.5;
    y.FontSize = 15;
    y.Color = 'black';
    y.LineStyle = '-.';
    y.Label = sprintf('%3.3f dB',number);
    y.LabelHorizontalAlignment = 'left';
    y.LabelVerticalAlignment = 'top';
end