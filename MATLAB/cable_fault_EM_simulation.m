clc;
clear;
close all;

%% ================================================
% NON-INVASIVE CABLE FAULT DETECTION
% ELECTROMAGNETIC FIELD SIMULATION
% ================================================

fs = 10000;

t = 0:1/fs:0.01;


%% ================================================
% NORMAL CABLE SIGNAL
% ================================================

normal_signal = sin(2*pi*1000*t);


%% ================================================
% NORMAL EMI
% ================================================

normal_emi = 0.5 * sin(2*pi*2500*t);


%% ================================================
% FAULT EMI
% ================================================

fault_emi = 1.5 * sin(2*pi*2500*t);


%% ================================================
% RECEIVED SIGNALS
% ================================================

normal_received = ...
    normal_signal + normal_emi;

fault_received = ...
    normal_signal + fault_emi;


%% ================================================
% NORMAL CONDITION
% ================================================

figure;

plot( ...
    t, ...
    normal_received, ...
    'LineWidth', ...
    1.5 ...
);

title( ...
    'Normal Cable Electromagnetic Signal' ...
);

xlabel('Time (s)');
ylabel('Amplitude');

grid on;


%% ================================================
% FAULT CONDITION
% ================================================

figure;

plot( ...
    t, ...
    fault_received, ...
    'LineWidth', ...
    1.5 ...
);

title( ...
    'Faulty Cable Electromagnetic Signal' ...
);

xlabel('Time (s)');
ylabel('Amplitude');

grid on;


%% ================================================
% FFT ANALYSIS
% ================================================

N = length(fault_received);

Y = fft(fault_received);

P2 = abs(Y/N);

P1 = P2(1:N/2+1);

P1(2:end-1) = ...
    2*P1(2:end-1);

f = fs*(0:(N/2))/N;


figure;

plot( ...
    f, ...
    P1, ...
    'LineWidth', ...
    1.5 ...
);

title( ...
    'Frequency Spectrum - Fault Condition' ...
);

xlabel('Frequency (Hz)');
ylabel('Magnitude');

grid on;

xlim([0 5000]);


%% ================================================
% RESULT
% ================================================

disp('==========================================');
disp(' EM SIMULATION COMPLETE');
disp('==========================================');

disp('Normal signal frequency: 1000 Hz');
disp('Normal EMI frequency: 2500 Hz');
disp('Fault EMI amplitude: Increased');

disp('==========================================');
