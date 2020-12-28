function factor(n) {
    if(n == 0) {
        return 1;
    } else {
        return n * factor(n-1);
    }
}

console.log(factor(10));
