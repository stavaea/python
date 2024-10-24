function[target_range, angle_measure, target_v] = measure(R0,Azimuth,v)
c=3.0e8;
f0=77e9;
lamda=c/f0;
d=lamda/2;
T=100e-6;
B=150e6;
K=B/T;
fs=2e6;
ts=1/fs;
T_n = 100;
prf = 1/T;
t = 0:ts:T_n*T-ts;
fast_t = mod(t,T);
slow_t = t - fast_t;
R0 =100;
Azimuth = 30;
V=15;
range_N = 2*fs*T;
fd_N = 256;
time_delay = ( Rt+Rr1)/c;


reslution_v = prf/fd_N*lamda/2;
reslution_R = fs/range_N/K*c/2;

send=exp(j*2*pi*(f0*t+K*fast_t.*fast_t/2));

tar_x=R0*sind(Azimuth)*ones(size(t));
tar_y=R0*cosd(Azimuth)*ones(size(t))-V*t;

recieve1_x=-d/2;recieve1_y=0;
recieve2_x=d/2;recieve2_y=0;

RT = sqrt((tar_x).^2+(tar_y).^2);
R1 = sqrt((tar_x-recieve1_x).^2+(tar_y-recieve1_y).^2);
R2 = sqrt((tar_x-recieve2_x).^2+(tar_y-recieve2_y).^2);
time_delay1 = (RT + R1)/c;time_delay2 = (RT + R2)/c;

e1 = exp(-j*2*pi*(f0*(t-time_delay1)-K*(fast_t-time_delay1).*(fast_t-time_delay1)/2))
wg1=wgn(size(e1,1),size(e1,2),0,100,complex');
echo1=e1+wg1;
echo_baseband1 = send.*conj(echo1);
e2 = exp(-j*2*pi*(f0*(t-time_delay2)-K*(fast_t-time_delay2).*(fast_t-time_delay2)/2))
wg2=wgn(size(e2,1),size(e2,2),0,100,'complex');
echo2=e2+wg2;
echo_baseband2 = send.conj(echo2)