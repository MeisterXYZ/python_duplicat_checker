#file='AimeeMann.txt';
#file='ThomasD.txt';
#file='PinkFloyd.txt';
#file='Vivaldi.txt';
#file='Scooter.txt';
#file='SarahConnor.txt';
file='TeganAndSara.txt';
#file='Adele.txt';
#file='Eminem.txt';
#file='Einaudi.txt';

for run in {1..50}
    do 
    let res=$run*2000; 
    python cutToLen.py $file $res; 
    done