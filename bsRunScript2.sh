filea='generatedTestData';
filee='_0.2dupFac_A.txt'; 
for run in {1..20}
    do 
    let res=$run*5000; 
    file=$filea$res$filee; 
    python 2_sequential.py $file; 
    done