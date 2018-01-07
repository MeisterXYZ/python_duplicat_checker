filea='generatedTestData'; 
filee='_0.01dupFac_AimeeMann.txt'; 

for run in {1..50}
    do 
    let res=$run*1000; 
    file=$filea$res$filee; 
    python 1_pyCollHand.py $file; 
    done