implementation='1_dictLike_measure.py'
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