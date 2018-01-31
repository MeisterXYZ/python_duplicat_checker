#filea='AimeeMann_';
#filea='ThomasD_';
#filea='PinkFloyd_';
#filea='Vivaldi_';
#filea='Scooter_';
#filea='SarahConnor_';
#filea='TeganAndSara_';
#filea='Adele_';
#filea='Eminem_';
filea='Einaudi_';

filee='DS.txt'; 
for run in {1..50}
    do 
    let res=$run*20; 
    file=$filea$res$filee; 
    python 2_sequential.py $file; 
    done