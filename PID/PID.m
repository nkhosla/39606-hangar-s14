function [vLinear, vTheta] = tethCont(vDist, theta, globVal)


eDOld = globVal.eDNew; eTOld = globVal.eTNew; %Advance variables

tNew = globVal.tNew; tOld = globVal.tOld;
intD = globVal.intD; intT = globVal.intT;

dt = tNew - tOld;

%Reference values
vDist0 = 0; % m
theta0 = 0; % rad

%Control Parameters for Distance and Angle
KpD = .1; KiD = 1;KdD = 10;
KpT = 1; KiT = 1;KdT = 1;

%Distance and Angle Errors
eDNew = vDist - vDist0; globVal.eDNew = eDNew;
eTNew = theta - theta0; globVal.eTNew = eTNew;

%Take integrals of error (Trap Rule)
intD = intD + (eDNew+eDOld)*dt/2; globVal.intD = intD;
intT = intT + (eTNew+eTOld)*dt/2; globVal.intT = intT;

%Take Derivatives of error (1st order backward)
dD = (eDNew-eDOld)/dt;
dT = (eTNew-eTOld)/dt;

%Control Function
uD = KpD*eDNew + KiD*intD + KdD*dD;
uT = KpT*eTNew + KiT*intT + KdT*dT;


vLinear = uD * vDist;
vTheta = uT * theta;

globVal.tOld = tNew;