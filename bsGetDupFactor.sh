filea='AimeeMann_'; 
filee='DS.txt'; 

for run in {1..50}
    do 
    let res=$run*1000; 
    file=$filea$res$filee; 
    python GetDupFactor.py $file; 
    done