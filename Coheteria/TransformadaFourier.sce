sample_rate=1000
loadmatfile("test.txt")
s=mtlb(test)
size_A=length(s);
x=s(1:size_A,1);
t = (0:1:size(s)(1)-1)'/sample_rate;
N=size(t,'*'); //number of samples
X=fft(x);
f=sample_rate*(0:(N/2))'/N; //associated frequency vector

n=size(f,'*');
//plot(t,x)
plot(f,abs(X(1:n)))
title('Ensayo 1')
xlabel('Frecuencias [Hz]')
ylabel('Ganancia')
