function [jval,gradient] =  costFunction(theta)
    jval=(theta(1)-3)^2+(theta(2)-5)^2;
    gradient=zeros(2,1);
    gradient(1)=2*(theta(1)-3);
    gradient(2)=2*(theta(2)-5);
endfunction
options=optimset('GradObj','on','MaxIter','1000');
initialTheta=zeros(2,1);
[optTheta,functionVal,exitFlag]=fminunc(@costFunction,initialTheta,options)



