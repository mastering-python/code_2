
long sum_of_squares(long n){
    long total = 0;

    /* The actual summing code */
    for(int i=0; i<n; i++){
        if((i * i) < n){
            total += i * i;
        }else{
            break;
        }
    }

    return total;
}
