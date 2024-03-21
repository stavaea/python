function Creat_File(File)
% CREAT_FILE 主要用于创建保存数据的文件夹
    result = dir(File); % 调用dir函数获取该文件夹信息
    if isempty(result) % 如果返回结果为空，则表示文件夹不存在
        mkdir(File);
    end
end

