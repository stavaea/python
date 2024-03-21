function [fre_meas,amp_meas,coll] = spec_coll(N9020A,len_coll)
coll = zeros(1,len_coll);
	for i = 1:len_coll
        pause(0.3)
		fprintf(N9020A,'CALC:MARK1:MAX');
		fprintf(N9020A,'CALC:MARK1:X?');fre_meas=str2double(fscanf(N9020A));
		fprintf(N9020A,'CALC:MARK1:Y?');coll(i)=str2double(fscanf(N9020A));
	end
	amp_meas = mean(coll,'all');
end