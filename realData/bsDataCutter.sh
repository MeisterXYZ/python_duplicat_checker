file='AimeeMann.txt'; 

for run in {1..50}
    do 
    let res=$run*1000; 
    python cutToLen.py $file $res; 
    done