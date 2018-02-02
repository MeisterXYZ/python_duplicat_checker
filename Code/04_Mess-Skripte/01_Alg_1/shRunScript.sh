implementation='1_dictLike_measure.py'
filea='generatedTestData10000_0.9dupFac_';

filee='DS.txt'; 
for run in {1..50}
    do 
    let res=$run*20; 
    file=$filea$res$filee; 
    python $implementation $file; 
    done