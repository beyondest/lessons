#basic notes
a=pi        %pi=3.14~

1 is row
2 is column
index begin from 1
add ; at end to disable print while making values
add ; also to write two command in one line
add , same as above but will not print
#math or logic signs
1==1        %equal
1~=1        %not equal
1 && 0      %and
1 || 0      %or
xor(1,0)    %xor yihuo


#common used command
PS1('>> ');                             %change ui 
disp(sprintf('%0.2f',a))                %format print
disp('string')
disp(a)
format long                             %print long bits of float
format short                            %print short bits of float
cd .. //cd dataset
pwd                                     %show present file way
who                                     %return 1*m matrix, each value is value name up to now, include dataset
whos                                    %return details of each value
clear valua_name
clear                                   %clear all value_names


#load and save dat or txt
#notice present dir
load('D:/pycv/lessons/dataset/test.dat')%create a value named test, test is matrix writed in test.dat
load D:/pycv/lessons/dataset/test.dat   %also work

save hello.dat x                        %make file in pwd to save value x
save hello.txt x -ascii                 %make in txt,txt is bigger than dat





#create matrix
x=0:0.01:1=[0:0.01:1]%usually used to create x variable to plot
a=[1,2,3]           %make row_vector
a=[1;2;3]           %make colunm_vector
A=[1 2;
3 4;
5 6]
B=ones(m,n)
C=zeros(m,n)
D=rand(m,n)         %all values range is (0,1)
E=randn(m,n)        %all values obeys Guassian function
F=eye(m,n) or eye(m)         %make unit matrix



#get info of matrix
size(A)         %return row_vector||A.shape
size(A,x)       %return num||A.shape[x-1]
length(v)       %return size of vector, if v is matrix, return biggest dimension size
A(x,y)          %A_xy,x is row,y is column,notice x>0,y>0
B=A(row_begin:row_end,column_begin:column_end)      %get slice of A, notice ',' not ';'
B=A([row_1 row_5],:)       %get row 1 and row 5 of A
A=[A,colunm_vector]                                 %expand matrix
A=[A;row_vector]
a=A(:)          %put all values of A into column vector a
C=[A B]=[A,B]   %vstack two matrix
C=[A;B]         %hstack two matrix



#complicate calculate
A*B             
A+B
A.*B                %multiply corresponding elements
A+1                 %each one add 1
A+ones(size(A))     %same as A+1
A^2                 %A*A
A.^2                %each one turns into square
A'                  %Transpose of A
pinv(A)             %pinverse of A,works well even A is singular
inv(A)              %inverse of A



#useful function
exp(A)              %get each exp
abs(A)              %get each abs
log(A)              %get each ln
max(a)              %get max in vector
[val,ind]=max(a)    %val=max(a),ind=index(val)
max(A)=max(A,[],1)  %return row_vector,each is max of column vector in A
max(A,[],2)         %return column_vector,each is max of row vector in A
max(max(A))=max(A(:))%return max num in A
A<3                 %compare each value in A
magic(dimension)    %for fun
[row_index,column_index]=find(A<4)     %return rows and columns of element that smaller than 4
sum(A)              %sum all num in A
sum(A,1)            %sum all num in columns in A, return row_vector
sum(A,2)            %sum all num in row in A
prod(A)             %product of all num in A
floor(A)            %round down
ceil(A)             %round up
flipud(A)           %flip in horizon line


#visualization
x=row_vector
y=sin(x)
figure(1);          %picture number 1
plot(x,y);          %create picture
xlabel('time');
ylabel('value');
title('name');
legend('sin');
close or close(figure_num)               %close only after above is done
subplot(1,3,2)      %create 1*3 parts in one window and now use 2th part to draw picture
axis([0.5 1 -1 1])  %set x axis range(0.5,1) and set y axis range(-1,1)
imagesc(A)          %show A in colors in image
imagesc(A);colorbar;colormap gray;%show A in gray_image
hist(matrix,nums of squares)            %show histogram picture of matrix

setenv('http_proxy','http://127.0.0.1:7890')
setenv('https_proxy','http://127.0.0.1:7890')
