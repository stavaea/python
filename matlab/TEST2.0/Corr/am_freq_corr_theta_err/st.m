a = 1:1:100;
power = a;
power = power - min (power);
power=10.^(power/20);
power=1./power;
power=power*32768;
power = fliplr(power')';
power = round(power);
for m = 1:length(power)
    if m > 1 && power(m) == 32768
        power(m) = power(m-1);
    end
end


power1 = a;
power1 = power1 - (min (power1)+5);
power1=10.^(power1/20);
power1=1./power1;
power1=power1*32768;
power1 = fliplr(power1')';
power1 = round(power1);
for m = 1:length(power1)
    if m > 1 && power1(m) == 32768
        power1(m) = power1(m-1);
    end
end
plot(power);hold on;
plot(power1)