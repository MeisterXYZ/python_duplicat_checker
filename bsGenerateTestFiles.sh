for run in {1..50} 
    do 
    let res=$run*1000;
    python testDataGenerator.py $res 0.01 AimeeMann; 
    done
