PATH= 'C:\Users\Admin\Desktop\leetcode\'; % path, where data are saved  
PATH1='C:\Users\Admin\Desktop\leetcode\'


PATHmat = strcat(PATH,'\*.mat');
files = dir(PATHmat);%�����ļ����е�������
for fileIndex = 1 : 1%length(files)
     DATAFILE = files(fileIndex).name;
     PATHmat = strcat(PATH1,DATAFILE);
 load (PATHmat); %��heart_scale_inst���浽heart_scale_inst.txt�ļ���
    Nametxt = strcat(PATH,'.txt');
    save(Nametxt,'val','-ASCII');
end