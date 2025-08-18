function factorial(n) {
    if (n < 0) return { error: "Negative numbers not allowed" };
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return { number: n, factorial: result };
}