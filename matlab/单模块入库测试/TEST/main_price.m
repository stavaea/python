instrreset;
clc ; clear ; close all;



old_pin = [164.16, 170.64, 12.93, 23.59, 18.36, 19.44, 25.92];
% old_pin = 15.1;
old_dan = old_pin+2;

for i = length(old_pin)

    new_pin = old_pin*0.3+old_pin;
    new_dan = old_dan*0.3+old_dan;
end
new_pin = round(new_pin,2)
new_dan = round(new_dan,2)

instrreset;