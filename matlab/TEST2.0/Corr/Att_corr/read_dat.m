function data = read_dat(File)
%     File = 'read_table\dca_cont.dat';
    f = fopen(File,"r");
    data = fread(f,inf,"uint32");
    fclose(f);
%     data = dec2hex(data_load);
end