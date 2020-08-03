#include <iostream>
 
int main(void) {
    unsigned long long u, v;
    scanf("%llu %llu", &u, &v);
    if(u > v) {
        printf("-1\n");
        return 0;
    } else if((v-u)%2 == 1) {
        printf("-1\n");
        return 0;
    }
    unsigned long long a, b;
    a = (v - u) / 2;
    b = u;
    if(u ==0 && v == 0) {
        printf("0\n");
    } else if(u == v) {
        printf("1\n%llu\n", a+b);
    } else if((a+b)==(a^b)) {
        printf("2\n%llu %llu\n", a, a+b);
    } else {
        printf("3\n%llu %llu %llu\n", a, a, b);
    }
    return 0;
}