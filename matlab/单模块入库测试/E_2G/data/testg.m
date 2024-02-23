clc ; clear ; close all
beipin = load("beipin.mat");
beihun = load("trace_beipin_hunpin.mat");
amp_1 = beipin.beipinqi;
amp_2 = beihun.amp_meas(1:20:end);
hunpinqi = amp_2 - amp_1;
plot(hunpinqi);