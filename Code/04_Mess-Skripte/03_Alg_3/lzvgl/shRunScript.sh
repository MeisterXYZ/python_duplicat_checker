implementation='3_pyDict_measure.py'
#filea='AimeeMann_';
#filea='ThomasD_';
#filea='PinkFloyd_';
#filea='Vivaldi_';
#filea='Scooter_';
#filea='SarahConnor_';
#filea='TeganAndSara_';
#filea='Adele_';
#filea='Eminem_';
#filea='Einaudi_';

#filea='AimeeMann_'
#filea='PinkFloyd_'
filea='TeganAndSara_'


filee='DS.txt'; 
for run in {1..50}
    do 
    let res=$run*2000; 
    file=$filea$res$filee; 
    python $implementation $file; 
    done